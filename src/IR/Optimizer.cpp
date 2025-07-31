#include "mutable/util/macro.hpp"
#include <mutable/IR/Optimizer.hpp>

#include <algorithm>
#include <mutable/catalog/Catalog.hpp>
#include <mutable/IR/Operator.hpp>
#include <mutable/Options.hpp>
#include <mutable/parse/AST.hpp>
#include <mutable/storage/Store.hpp>
#include <numeric>
#include <tuple>
#include <vector>
#include <queue>
#include <unordered_set>
#include <cassert>
#include <sys/param.h>

using namespace m;
using namespace m::ast;

/*======================================================================================================================
 * Helper functions
 *====================================================================================================================*/

struct WeighExpr
{
private:
    unsigned weight_ = 0;

public:
    operator unsigned() const { return weight_; }

    void operator()(const cnf::CNF &cnf)
    {
        for (auto &clause : cnf)
            (*this)(clause);
    }

    void operator()(const cnf::Clause &clause)
    {
        for (auto pred : clause)
            (*this)(*pred);
    }

    void operator()(const ast::Expr &e)
    {
        visit(overloaded{
                  [](const ErrorExpr &)
                  { M_unreachable("no errors at this stage"); },
                  [this](const Designator &d)
                  {
                      if (auto cs = cast<const CharacterSequence>(d.type()))
                          weight_ += cs->length;
                      else
                          weight_ += 1;
                  },
                  [this](const Constant &e)
                  {
                      if (auto cs = cast<const CharacterSequence>(e.type()))
                          weight_ += cs->length;
                      // fixed-size constants are considered free, as they may be encoded as immediate constants in the instr
                  },
                  [this](const FnApplicationExpr &)
                  {
                      weight_ += 1;
                  },
                  [this](const UnaryExpr &)
                  { weight_ += 1; },
                  [this](const BinaryExpr &)
                  { weight_ += 1; },
                  [this](const QueryExpr &)
                  { weight_ += 1000; } // XXX: this should never happen because of unnesting
              },
              e, tag<ConstPreOrderExprVisitor>{});
    }
};

std::vector<cnf::CNF> Optimizer::optimize_filter(cnf::CNF filter)
{
    constexpr unsigned MAX_WEIGHT = 12; // equals to 4 comparisons of fixed-length values
    M_insist(not filter.empty());

    /* Compute clause weights. */
    std::vector<unsigned> clause_weights;
    clause_weights.reserve(filter.size());
    for (auto &clause : filter)
    {
        WeighExpr W;
        W(clause);
        clause_weights.emplace_back(W);
    }

    /* Sort clauses by weight using an index vector. */
    std::vector<std::size_t> order(filter.size(), 0);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&clause_weights](std::size_t first, std::size_t second) -> bool
              { return clause_weights[first] < clause_weights[second]; });

    /* Dissect filter into sequence of filters. */
    std::vector<cnf::CNF> optimized_filters;
    unsigned current_weight = 0;
    cnf::CNF current_filter;
    for (std::size_t i = 0, end = filter.size(); i != end; ++i)
    {
        const std::size_t idx = order[i];
        cnf::Clause clause(std::move(filter[idx]));
        M_insist(not clause.empty());
        const unsigned clause_weight = clause_weights[idx];

        if (not current_filter.empty() and current_weight + clause_weight > MAX_WEIGHT)
        {
            optimized_filters.emplace_back(std::move(current_filter)); // empties current_filter
            current_weight = 0;
        }

        current_filter.emplace_back(std::move(clause));
        current_weight += clause_weight;
    }
    if (not current_filter.empty())
        optimized_filters.emplace_back(std::move(current_filter));

    M_insist(not optimized_filters.empty());
    return optimized_filters;
}

std::vector<Optimizer::projection_type>
Optimizer::compute_projections_required_for_order_by(const std::vector<projection_type> &projections,
                                                     const std::vector<order_type> &order_by)
{
    std::vector<Optimizer::projection_type> required_projections;

    /* Collect all required `Designator`s which are not included in the projection. */
    auto get_required_designator = overloaded{
        [&](const ast::Designator &d) -> void
        {
            if (auto t = std::get_if<const Expr *>(&d.target()))
            { // refers to another expression?
                /*----- Find `t` in projections. -----*/
                for (auto &[expr, _] : projections)
                {
                    if (*t == &expr.get())
                        return; // found
                }
            }
            /*----- Find `d` in projections. -----*/
            for (auto &[expr, alias] : projections)
            {
                if (not alias.has_value() and d == expr.get())
                    return; // found
            }
            required_projections.emplace_back(d, ThreadSafePooledOptionalString{});
        },
        [&](const ast::FnApplicationExpr &fn) -> void
        {
            /*----- Find `fn` in projections. -----*/
            for (auto &[expr, alias] : projections)
            {
                if (not alias.has_value() and fn == expr.get())
                    throw visit_skip_subtree(); // found
            }
            required_projections.emplace_back(fn, ThreadSafePooledOptionalString{});
            throw visit_skip_subtree();
        },
        [](auto &&) -> void { /* nothing to be done */ },
    };
    /* Process the ORDER BY clause. */
    for (auto [expr, _] : order_by)
        visit(get_required_designator, expr.get(), m::tag<m::ast::ConstPreOrderExprVisitor>());

    return required_projections;
}

/*======================================================================================================================
 * Optimizer_ResultDB
 *==============================================================    return PT.======================================================*/

double SemiJoinCostFunction::estimate_semi_join_costs(const CardinalityEstimator &CE, const DataModel &left, const DataModel &right)
{
    return estimate_semi_join_hash_costs(CE, right) + estimate_semi_join_probe_costs(CE, left);
}

double SemiJoinCostFunction::estimate_semi_join_probe_costs(const CardinalityEstimator &CE, const DataModel &model)
{
    return static_cast<double>(CE.predict_cardinality(model));
}

double SemiJoinCostFunction::estimate_semi_join_hash_costs(const CardinalityEstimator &CE, const DataModel &model)
{
    return 3 * static_cast<double>(CE.predict_cardinality(model));
}

void TreeEnumerator::determine_reduced_models(QueryGraph &G, AdjacencyMatrix &adj_matrix, const CardinalityEstimator &CE, card_order_t card_orders[], std::vector<std::unique_ptr<DataModel>> &base_models)
{
    auto rec = [&](std::size_t parent, std::size_t node, auto &&rec)
    {
        /* Check whether the current parent/subtree pair was already evaluated at some point */
        if (auto it = parent_node_model(parent, node); it != model_end(parent))
        {
            return it;
        }

        auto node_model = CE.copy(*base_models[node]);

        /* Account for bottom-up and top-down semi-joins */
        for (std::size_t child : adj_matrix.neighbors(Subproblem::Singleton(node)))
        {
            /* Ignore parent */
            if (child == parent)
                continue;
            auto it_model = rec(node, child, rec);
            node_model = CE.estimate_semi_join(G, *node_model, *it_model->second, {});
        }

        update_model_table(parent, node, std::move(node_model));
        return parent_node_model(parent, node);
    };

    /* Enumerate trough each possible root node */
    for (const auto &root : G.sources())
    {
        /* The hack requires all nodes to still exist in the table, to filter out invalid ones, we have to check their
        * entry in the matrix */
        if (adj_matrix[root->id()].empty()) continue;
        rec(root->id(), root->id(), rec);
        compute_cardinality_order(G, adj_matrix, CE, root->id(), card_orders[root->id()], base_models);
    }
}

void TreeEnumerator::compute_cardinality_order(const QueryGraph &G, AdjacencyMatrix &adj_matrix, const CardinalityEstimator &CE, std::size_t node, std::vector<std::size_t> &card_order, std::vector<std::unique_ptr<DataModel>> &base_models)
{
    std::unordered_map<size_t, size_t> cardinalities;
    const auto node_problem = Subproblem::Singleton(node);
    const auto node_model = CE.copy(*base_models[node]);
    /* Add all neighbors to the vector */
    for (auto neighbor : adj_matrix.neighbors(node_problem))
    {
        card_order.emplace_back(neighbor);
        const auto neighbor_model = parent_node_model(node, neighbor);
        const auto neighbor_cardinality = CE.predict_cardinality(*(CE.estimate_semi_join(G, *node_model, *neighbor_model->second, {})));
        cardinalities[neighbor] = neighbor_cardinality;
    }

    auto cmp = [&cardinalities](const std::size_t a, const std::size_t b)
    {
        return cardinalities[a] < cardinalities[b];
    };
    std::ranges::sort(card_order, cmp);
}

std::pair<std::size_t, double> TreeEnumerator::find_best_root(QueryGraph &G, std::unordered_set<std::size_t> &required_reductions, AdjacencyMatrix &adj_matrix, const CardinalityEstimator &CE, SemiJoinCostFunction &SJ, card_order_t card_orders[], std::vector<std::unique_ptr<DataModel>> &base_models)
{
    std::vector<semi_join_order_t> semi_join_reduction_order;
    double lowest_costs = std::numeric_limits<double>::infinity();
    std::unordered_map<std::size_t, std::unordered_map<std::size_t, std::unique_ptr<DataModel>>> reduced_models;
    std::size_t best_root = 0; // First node

    determine_reduced_models(G, adj_matrix, CE, card_orders, base_models);

    auto estimate_subtree_costs = [&](std::size_t parent, std::size_t node, auto &&estimate_subtree_costs)
    {
        /* Check whether the current parent/subtree pair was already evaluated at some point */
        if (auto it = parent_node_costs(parent, node); it != cost_end(parent))
        {
            return it;
        }

        auto node_model = CE.copy(*base_models[node]);
        auto node_fully_reduced_model = CE.estimate_full_reduction(G, *node_model);
        bool reduction_required = required_reductions.contains(node);
        double costs = 0;

        /* Account for bottom-up and top-down semi-joins */
        for (std::size_t child : card_orders[node])
        {
            /* Ignore parent */
            if (child == parent)
                continue;
            /* Recursively evaluate the child subtree */
            auto it_costs = estimate_subtree_costs(node, child, estimate_subtree_costs);
            auto it_model = parent_node_model(node, child);
            costs += it_costs->second.first +                                         // Recursive Tree costs
                     SJ.estimate_semi_join_costs(CE, *node_model, *it_model->second); // Bottom-up Semi-join costs between node and child
            node_model = CE.estimate_semi_join(G, *node_model, *it_model->second, {});
            if (it_costs->second.second && parent != node)
            {
                // Top-down Semi-join costs between child and node
                costs += SJ.estimate_semi_join_costs(CE, *it_model->second, *node_fully_reduced_model);
                reduction_required = true;
            }
        }

        update_cost_table(parent, node, costs, reduction_required);
        return parent_node_costs(parent, node);
    };

    /* Enumerate trough each possible root node to find the best one */
    for (const auto &root : G.sources())
    {
        /* Ignore invalid roots */
        if (adj_matrix[root->id()].empty()) continue;

        /* Folded node id */
        if (card_orders[root->id()].empty())
        {
            continue;
        }

        auto it = estimate_subtree_costs(root->id(), root->id(), estimate_subtree_costs);
        if (it->second.first < lowest_costs)
        {
            best_root = root->id();
            lowest_costs = it->second.first;
        }
    }

    return std::make_pair(best_root, lowest_costs);
}

DataSource &Optimizer_ResultDB_utils::choose_root_node(QueryGraph &G, SemiJoinReductionOperator &op)
{
    const Schema &S = op.schema();
    std::size_t current_root_idx = -1UL;
    for (std::size_t idx = 0; idx < G.sources().size(); ++idx)
    {
        auto intersection = S & op.child(idx)->schema();
        if (not intersection.empty())
        { // contained in projections
            if (current_root_idx == -1UL or (G.sources()[idx]->joins().size() > G.sources()[current_root_idx]->joins().size()))
                current_root_idx = idx;
        }
    }
    if (current_root_idx == -1UL)
    { // no relation found that is part of the projections (likely SELECT *)
        current_root_idx = 0;
        for (std::size_t idx = 1; idx < G.sources().size(); ++idx)
        { // fallback to highest degree
            if (G.sources()[idx]->joins().size() > G.sources()[current_root_idx]->joins().size())
                current_root_idx = idx;
        }
    }
    return *G.sources()[current_root_idx];
}

/** Identifies a set of joins that have to be computed such that the join graph becomes acyclic. Currently, the
 * implementation heuristically chooses the node `x` with the highest degree first and subsequently, identifies the node
 * `y` with the highest degree from the neighbors of `x`. The rationale behind this is that nodes with a high degree are
 * more likely to be part of a cycle.
 *
 * TODO: Instead of repeatedly choosing two nodes heuristically and checking if the resulting graph is acyclic, we can
 * use Tarjans bridge-finding algorithm:
 * https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29#Tarjan's_bridge-finding_algorithm
 * Using this, we can successively remove bridges (i.e. joins that are not part of a cycle) and with that, narrow down
 * the set of relations such that we know that the resulting nodes are part a cycle.
 * Note, the query graph could only have joins that are part of a cycle, i.e. the algorithm would not be able to remove
 * any edges. In this case, it might still matter which folds are computed.
 */
std::vector<Optimizer_ResultDB::fold_t> Optimizer_ResultDB_utils::compute_folds(const QueryGraph &G)
{
    M_insist(G.is_cyclic(), "join graph must be cyclic");
    M_insist(G.num_sources() > 2, "join graph with two or less data sources cannot be cyclic");

    /*----- Get the ids of the data sources in `G` and put them in individual sets. -----*/
    std::vector<fold_t> folds;
    for (auto &ds : G.sources())
        folds.push_back({ds->id()});

    /*----- Compute the folds of the query graph. -----*/
    AdjacencyMatrix mat(G.adjacency_matrix()); // copy the query graphs adjacency matrix
    do
    {
        /*----- Compute `x` and `y` using the adjacency matrix. -----*/
        std::size_t x_id = mat.highest_degree_node(SmallBitset::All(folds.size()));
        std::size_t y_id = mat.highest_degree_node(mat.neighbors(SmallBitset::Singleton(x_id)));
        if (y_id < x_id)
            std::swap(x_id, y_id); // `x_id` contains the smaller id

        /*----- Merge the two folds. -----*/
        folds[x_id].merge(folds[y_id]);
        folds.erase(folds.begin() + y_id);

        mat = mat.merge_nodes(x_id, y_id); // merge the two nodes of the adjacency matrix
    } while (mat.is_cyclic());

    return folds;
}

/** Modify the `QueryGraph` based on the folds. Concretely, the data sources that are part of a fold are put together in
 * a (nested) query and the joins are adapted accordingly. */
void Optimizer_ResultDB_utils::fold_query_graph(QueryGraph &G, std::vector<fold_t> &folds)
{
    auto &C = Catalog::Get();

    /* Retrieve and reset data sources and joins in `G`. */
    const auto joins = std::exchange(G.joins(), std::vector<std::unique_ptr<Join>>());
    const auto sources = std::exchange(G.sources(), std::vector<std::unique_ptr<DataSource>>());

    /* Create a new `BaseTable` or `Query` with the same information as the data source at position `ds_id_in_G` in
     * `sources` and add it to the query graph `G`. Returns the id of the newly inserted data source. */
    auto add_ds_to_query_graph = [&sources](QueryGraph &G, std::size_t ds_id_in_G) -> std::size_t
    {
        auto &ds = sources[ds_id_in_G];
        auto new_id = G.sources().size();
        if (auto bt = cast<BaseTable>(ds.get()))
        {
            auto &new_bt = G.add_source(bt->name(), bt->table());
            new_bt.update_filter(std::move(bt->filter()));
        }
        else
        {
            auto &Q = as<Query>(*ds);
            auto &new_Q = G.add_source(Q.name(), Q.extract_query_graph());
            new_Q.update_filter(std::move(Q.filter()));
        }
        return new_id;
    };

    /* The `mod_nested_id` data structure stores the following information:
     *      (data source id in modified `G`, data source id in `G_nested` of modified `G`)
     * The index into the array corresponds to the id of the original data source in `G`.
     * The second value does not hold any meaning for base tables. */
    std::pair<std::size_t, std::size_t> ds2mod_nested_id[sources.size()];
    /*----- Create new data sources for the modified query graph. -----*/
    for (auto fold : folds)
    {
        if (fold.size() == 1)
        { // base table
            auto id = *fold.begin();
            auto ds_id = add_ds_to_query_graph(G, id);
            ds2mod_nested_id[id] = std::make_pair(ds_id, 0);
        }
        else
        { // nested query
            /*----- Create new `QueryGraph` and add as `DataSource` to `G`. -----*/
            auto G_nested = std::make_unique<QueryGraph>();
            G_nested->transaction(G.transaction()); // nested query requires same transaction ID
            auto ds_id_in_G_mod = G.sources().size();
            std::ostringstream oss;
            oss << '$';
            std::size_t count = 0;
            for (auto ds_id_in_G : fold)
            { // add data sources
                if (count != 0)
                    oss << '_';
                oss << sources[ds_id_in_G]->name();
                auto ds_id_in_G_nested = add_ds_to_query_graph(*G_nested, ds_id_in_G);
                ds2mod_nested_id[ds_id_in_G] = std::make_pair(ds_id_in_G_mod, ds_id_in_G_nested);
                ++count;
            }
            G.add_source(C.pool(oss.str().c_str()), std::move(G_nested));
        }
    }

    /*----- Create joins between the new data sources in `G`. -----*/
    for (auto &join : joins)
    {
        M_insist(join->sources().size() == 2);
        /*----- Create new `Join` and add to corresponding data source. -----*/
        auto G_lhs_id = join->sources()[0].get().id();
        auto G_rhs_id = join->sources()[1].get().id();

        auto [mod_lhs_id, nested_lhs_id] = ds2mod_nested_id[G_lhs_id];
        auto [mod_rhs_id, nested_rhs_id] = ds2mod_nested_id[G_rhs_id];
        auto &mod_lhs_ds = *G.sources()[mod_lhs_id];
        auto &mod_rhs_ds = *G.sources()[mod_rhs_id];

        auto add_join = [&join](QueryGraph &G, DataSource &lhs_ds, DataSource &rhs_ds)
        {
            /*----- Create new joins sources. -----*/
            Join::sources_t new_join_sources;
            new_join_sources.push_back(lhs_ds);
            new_join_sources.push_back(rhs_ds);

            /*----- Construct new join and add to `G`. -----*/
            auto &new_join = G.emplace_join(std::move(join->condition()), std::move(new_join_sources));

            /*----- Add new join to its respective data sources. -----*/
            lhs_ds.add_join(new_join);
            rhs_ds.add_join(new_join);
        };

        if (mod_lhs_id == mod_rhs_id)
        { // both data sources have the same `id` in `G` -> join inside nested query
            auto &Q_nested = as<Query>(mod_lhs_ds);
            auto &G_nested = Q_nested.query_graph();

            auto &nested_lhs = *G_nested.sources()[nested_lhs_id];
            auto &nested_rhs = *G_nested.sources()[nested_rhs_id];
            Join::sources_t nested_sources;
            nested_sources.push_back(nested_lhs);
            nested_sources.push_back(nested_rhs);
            add_join(G_nested, nested_lhs, nested_rhs);
            continue;
        }

        /*----- Check if this join already exists in `G`. -----*/
        auto it = std::find_if(G.joins().begin(), G.joins().end(), [&mod_lhs_ds, &mod_rhs_ds](auto &j)
                               {
            M_insist(j->sources().size() == 2);
            return (j->sources()[0].get() == mod_lhs_ds and j->sources()[1].get() == mod_rhs_ds) or
                   (j->sources()[1].get() == mod_lhs_ds and j->sources()[0].get() == mod_rhs_ds); });

        if (it != G.joins().end()) // already in `G` -> update condition
            (*it)->update_condition(std::move(join->condition()));
        else // construct new join and add to `G`
            add_join(G, mod_lhs_ds, mod_rhs_ds);
    }
}

/** If the `QueryGraph` contains multiple joins between two specific data sources, combine them into *one* join that
 * concatenates the individual conditions using a logical AND operation. */
void Optimizer_ResultDB_utils::combine_joins(QueryGraph &G)
{
    std::vector<std::unique_ptr<Join>> modified_joins;
    for (auto &j : G.joins())
    {
        auto it = std::find_if(modified_joins.cbegin(), modified_joins.cend(), [&j](auto &mod_j)
                               {
            M_insist(j->sources().size() == 2);
            M_insist(mod_j->sources().size() == 2);
            return (j->sources()[0].get() == mod_j->sources()[0] and j->sources()[1].get() == mod_j->sources()[1]) or
                   (j->sources()[1].get() == mod_j->sources()[0] and j->sources()[0].get() == mod_j->sources()[1]); });
        if (it != modified_joins.cend())
            (*it)->update_condition(j->condition()); // `j` is already in `modified_joins` -> update condition
        else
            modified_joins.push_back(std::move(j)); // `j` is not in `modified_joins` -> add
    }
    G.joins() = std::move(modified_joins);
}

std::vector<Optimizer_ResultDB::semi_join_order_t>
Optimizer_ResultDB_utils::compute_semi_join_reduction_order(QueryGraph &G, SemiJoinReductionOperator &op)
{
    std::vector<semi_join_order_t> semi_join_reduction_order;

    /*----- Choose root node that is part of the projections and has the highest degree. -----*/
    auto &root = choose_root_node(G, op);

    /*----- Compute BFS ordering starting at `root`. -----*/
    auto &mat = G.adjacency_matrix();
    std::unordered_set<std::reference_wrapper<DataSource>, DataSourceHash, DataSourceEqualTo> visited;
    std::queue<std::reference_wrapper<DataSource>> Q;
    std::vector<std::reference_wrapper<DataSource>> BFS_ordering;
    Q.push(root);

    while (not Q.empty())
    {
        auto x = Q.front();
        Q.pop();
        BFS_ordering.push_back(x);
        visited.insert(x);
        auto neighbors = mat.neighbors(SmallBitset::Singleton(x.get().id()));
        for (auto n_id : neighbors)
        {
            auto &n = *G.sources()[n_id];
            if (visited.contains(n))
                continue;
            Q.push(n);
        }
    }

    /*----- Use the BFS ordering of the data sources to construct the order in which the semi-joins are applied. -----*/
    std::unordered_set<std::reference_wrapper<Join>, JoinHash, JoinEqualTo> handled_joins;
    for (auto ds : BFS_ordering)
    {
        for (auto j : ds.get().joins())
        {
            if (not handled_joins.contains(j))
            {
                /*----- Check which join source (lhs or rhs) contains the current `ds` (closer to the root). -----*/
                using ds_it_t = decltype(j.get().sources().begin());
                auto [lhs, rhs] = [&j, &ds]() -> std::pair<ds_it_t, ds_it_t>
                {
                    M_insist(j.get().sources().size() == 2);
                    auto lhs = j.get().sources().begin();
                    auto rhs = std::next(lhs);
                    if (lhs->get() == ds.get())
                        return {lhs, rhs};
                    else
                        return {rhs, lhs};
                }();
                semi_join_reduction_order.emplace_back(*lhs, *rhs);
                handled_joins.insert(j);
            }
        }
    }
    return semi_join_reduction_order;
}

std::pair<std::vector<Optimizer_ResultDB::semi_join_order_t>, double>
Optimizer_ResultDB_utils::enumerate_semi_join_reduction_order(QueryGraph &G, std::unordered_set<std::size_t> required_reductions, AdjacencyMatrix &adj_matrix, const CardinalityEstimator &CE, std::vector<std::unique_ptr<DataModel>> &base_models)
{
    auto &C = Catalog::Get();
    auto SJ = SemiJoinCostFunction();

    /* Contains for each possible data source (id) the best order in which to apply
     * adjacent semi-joins */
    card_order_t card_orders[G.num_sources()];

    auto tree_enumerator = TreeEnumerator(G.num_sources());

    auto [best_root, costs] = tree_enumerator.find_best_root(G, required_reductions, adj_matrix, CE, SJ, card_orders, base_models);
    std::vector<Optimizer_ResultDB::semi_join_order_t> semi_join_reduction_order;

    /* Create semi-join order */
    auto construct_semi_join_order = [&](std::size_t parent, std::size_t node, auto &&construct_semi_join_order) -> void
    {
        /* Join with neighbors */
        for (auto it = card_orders[node].rbegin(); it != card_orders[node].rend(); it++)
        {
            if (parent == *it)
                continue;
            semi_join_reduction_order.emplace_back(G[node], G[*it]);
        }

        /* Recursive descent */
        for (auto it = card_orders[node].rbegin(); it != card_orders[node].rend(); ++it)
        {
            if (parent == *it)
                continue;
            construct_semi_join_order(node, *it, construct_semi_join_order);
        }
    };

    construct_semi_join_order(best_root, best_root, construct_semi_join_order);

    return std::make_pair(semi_join_reduction_order, costs);
}

Optimizer_ResultDB_utils::bc_forest_t Optimizer_ResultDB_utils::build_bc_forest(const std::vector<Subproblem> &blocks, const Subproblem &cut_vertices)
{
    bc_forest_t bc_forest;
    auto add_edge_to_forest = [&bc_forest](const Subproblem left, const Subproblem right)
    {
        auto it = bc_forest.find(left);
        if (it == bc_forest.end())
        {
            it = bc_forest.try_emplace(left).first;
        }
        it->second.emplace_back(right);
    };

    for (const auto block : blocks)
    {
        /* Add an edge between the block node and the cut vertex node */
        for (Subproblem block_cut_vertices = cut_vertices & block; const auto node_id : block_cut_vertices)
        {
            const auto node_problem = Subproblem::Singleton(node_id);
            /* Undirected graph */
            add_edge_to_forest(block, node_problem);
            add_edge_to_forest(node_problem, block);
        }
    }

    return bc_forest;
}

template <typename PlanTable>
Optimizer_ResultDB_utils::folding_table_entry_t Optimizer_ResultDB_utils::create_and_enumerate_problems(QueryGraph& G, AdjacencyMatrix& adj_matrix, std::unordered_map<Subproblem, Subproblem, SubproblemHash> folded_mapping, folding_table_t& folding_table, const folding_problem_t &folding_problem, std::unordered_map<Subproblem, double, SubproblemHash>& fold_costs, PlanTable& PT_order, bool use_tvc) {

    /* First, we need to identify all blocks in the problem */
    std::vector<Subproblem> blocks;
    Subproblem cut_vertices;
    adj_matrix.compute_blocks_and_cut_vertices(blocks, cut_vertices, folding_problem.second, 3);

    /* Use the blocks to create the bc forest */
    auto bc_forest = build_bc_forest(blocks, cut_vertices);

    /* Now create the required tree sets */
    auto tree_sets = create_tree_sets(bc_forest, blocks, folding_problem.second - folding_problem.first);

    /* Afterward, enumerate each tree set and find the best solution and corresponding costs, which we then just return */
    return enumerate_problems(G, adj_matrix, folded_mapping, folding_table, tree_sets, fold_costs, PT_order, use_tvc);

}

std::vector<Optimizer_ResultDB_utils::tree_problem_t> Optimizer_ResultDB_utils::create_tree_sets(bc_forest_t &bc_forest, const std::vector<Subproblem> &blocks, const Subproblem removed_cut_vertex)
{
    /* Determine trees within the bc_forest */
    std::vector<std::unordered_set<Subproblem, SubproblemHash>> trees;

    auto dfs = [&](Subproblem current_node, const Subproblem parent, auto &&callback, auto &&dfs) -> void
    {
        /* Go through each child and visit recursively */
        if (current_node.size() == 1)
        {
            /* Current node is a vertex node */
            for (auto child : bc_forest[current_node])
            {
                if (child == parent)
                    continue;
                callback(current_node, child);
                dfs(child, current_node, callback, dfs);
            }
        }
        else
        {
            /* Current node is a block node */
            for (auto child : bc_forest[current_node])
            {
                if (child == parent)
                    continue;
                dfs(child, current_node, callback, dfs);
            }
        }
    };

    /* Traverse each block in the bc blocks to obtain the trees */
    auto already_visited = Subproblem();
    for (const auto block : blocks)
    {
        if (not(block & already_visited).empty())
            /* Block already part of another tree */
            continue;

        /* Store next tree */
        std::unordered_set<Subproblem, SubproblemHash> next_tree{};

        /* Whenever a new block node is encountered, add it to the current tree */
        auto callback = [&](Subproblem, Subproblem block_node) -> void
        {
            already_visited |= block_node;
            next_tree.emplace(block_node);
        };
        callback(Subproblem(), block);

        /* Perform DFS */
        dfs(block, Subproblem(), callback, dfs);

        /* Store the tree */
        trees.emplace_back(next_tree);
    }

    std::vector<tree_problem_t> tree_problems;

    /* Create the folding problems by traversing through each tree */
    for (const auto& tree : trees)
    {
        tree_problem_t tree_problem;

        /* Create a problem set for each possible root in the tree
         * This only holds, if this is not within a recursive call. Otherwise,
         * only one root is allowed, namely the node that already lost its cut vertex!
         */
        for (auto root : tree)
        {
            if (not removed_cut_vertex.empty() and (root & removed_cut_vertex).empty())
                /* This is a recursive call and the root is not the one that lost its cut vertex */
                continue;
            problem_set_t problem_set = {std::make_pair(root - removed_cut_vertex, root)};
            auto callback = [&](const Subproblem vertex_node, const Subproblem block_node) -> void
            {
                problem_set.emplace_back(std::make_pair(block_node - vertex_node, block_node));
            };
            dfs(root, Subproblem(), callback, dfs);
            tree_problem.emplace_back(problem_set);
        }
        tree_problems.emplace_back(tree_problem);
    }

    return tree_problems;
}

template <typename PlanTable>
Optimizer_ResultDB_utils::folding_table_entry_t Optimizer_ResultDB_utils::enumerate_problems(QueryGraph &G, AdjacencyMatrix& adj_matrix, std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping, folding_table_t& folding_table, std::vector<tree_problem_t> &tree_problems, std::unordered_map<Subproblem, double, SubproblemHash>& fold_costs,PlanTable &PT_order, bool use_tvc)
{
    /* Find the best assignments for each tree */
    const auto best_solution = std::make_shared<std::pair<std::vector<Subproblem>, double>>(std::vector<Subproblem>{}, 0);

    for (const auto& tree_problem : tree_problems)
    {
        auto tree_solution = std::make_shared<std::pair<std::vector<Subproblem>, double>>(std::vector<Subproblem>{}, std::numeric_limits<double>::infinity());;

        /* Find the best assignment for the tree */
        for (auto &problem_set : tree_problem)
        {
            const auto curr_solution = std::make_shared<std::pair<std::vector<Subproblem>, double>>(std::vector<Subproblem>{}, 0);

            /* Find the best solution for each block problem */
            for (const auto& folding_problem : problem_set)
            {
                auto solution = enumerate_block_problem(G, adj_matrix, folded_mapping, folding_table, folding_problem, fold_costs, PT_order, use_tvc);
                for (auto &block : solution->first) curr_solution->first.emplace_back(block);
                curr_solution->second += solution->second;
            }

            /* Check whether current assignment allows for a better solution */
            if (curr_solution->second < tree_solution->second) tree_solution = curr_solution;
        }

        /* Add solution for this tree to the global solution */
        for (auto block : tree_solution->first) best_solution->first.emplace_back(block);
        best_solution->second += tree_solution->second;
    }

    return best_solution;
}

template <typename PlanTable>
Optimizer_ResultDB_utils::folding_table_entry_t Optimizer_ResultDB_utils::enumerate_block_problem(QueryGraph &G, AdjacencyMatrix& adj_matrix, std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping, folding_table_t& folding_table, folding_problem_t folding_problem, std::unordered_map<Subproblem, double, SubproblemHash>& fold_costs, PlanTable &PT_order, const bool use_tvc)
{
    const auto &C = Catalog::Get();
    const auto &CE = C.get_database_in_use().cardinality_estimator();

    /* Helper function to get the original relations for a given problem */
    auto get_original_problem = [&](const Subproblem problem) -> Subproblem {
        if (use_tvc) {
            return problem;
        }
        if (folded_mapping.contains(problem)) {
             return folded_mapping.at(problem);
        }
        auto original_problem = Subproblem();
        for (const auto node_id: problem) {
            /* It is assumed that each singleton is already contained in the mapping */
            original_problem |= folded_mapping.at(Subproblem::Singleton(node_id));
        }
        folded_mapping[problem] = original_problem;
        return original_problem;
    };

    /* When you are in recursive mode, i.e., use_tvc is false, then you need to consider the relations represented by the graph,
     * instead of the actual relations */
    const auto problem = folding_problem.first;
    const auto original_problem = get_original_problem(problem);

    /* Check whether the folding problem has been solved before */
    if (folding_table.contains(original_problem)) return folding_table[original_problem];

    /* The same holds for the actual block of the problem */
    const auto block = folding_problem.second;
    const auto original_block = get_original_problem(block);

    /* We might need to update our mappings from folded problems to new ones */
    auto update_mapping = [&](const Subproblem folded_left, const Subproblem folded_right) {
        auto rec = [&](const Subproblem folded_left, const Subproblem folded_right, auto rec) {
            auto update_mapping = std::bind(rec, std::placeholders::_1, std::placeholders::_2, rec);
            /* Recursively update mappings */
            if (not folded_mapping.contains(folded_left)) MinCutAGaT{}.partition(adj_matrix, update_mapping, folded_left, true);
            if (not folded_mapping.contains(folded_right)) MinCutAGaT{}.partition(adj_matrix, update_mapping, folded_right, true);
            if (const auto combined_folded = folded_left | folded_right; not folded_mapping.contains(combined_folded)) {
                folded_mapping.emplace(combined_folded, folded_mapping[folded_left] | folded_mapping[folded_right]);
            }
        };
        rec(folded_left, folded_right, rec);
    };

    /* Define a callback function for each ccp pair to evaluate the best join order for each of them
     * Depending on whether we deal with a folded matrix, we might to consider the original problems here
     * and not the folded ones.
     */
    std::function<void(Subproblem left, Subproblem right)> join_order_callback;

    if (use_tvc) {
        join_order_callback = [&](const Subproblem left, const Subproblem right) -> void
        {
            /* Only update the plan table */
            PT_order.update(G, CE, C.cost_function(), left, right, cnf::CNF{});
        };
    } else {
        join_order_callback = [&](const Subproblem folded_left, const Subproblem folded_right) -> void
        {
            /* Also update the folded mapping */
            update_mapping(folded_left, folded_right);
            PT_order.update(G, CE, C.cost_function(), folded_mapping[folded_left], folded_mapping[folded_right], cnf::CNF{});
        };
    }

    /* Determine the best join order for the folding problem */
    if (not PT_order.has_plan(original_problem))
    {
        /* Use DP_CCP */
        adj_matrix.for_each_CSG_pair_undirected(original_block, join_order_callback);
    }

    /* Now we know that the best join order is known for each subproblem. Therefore, we only need to access the folding costs, as well as the Yannakakis heuristic
    For that, we will now traverse three different solution classes: 1. Join all relations in the block, 2. Join until two folds are left, 3. Use TVCs to solve the block */

    /* Perform some required precomputations for the Yannakakis Heuristic */
    std::unique_ptr<YannakakisHeuristic> heuristic = std::make_unique<WeakCardinalityHeuristic>(WeakCardinalityHeuristic(PT_order, folding_problem.first, G, adj_matrix, CE, folded_mapping));

    /* Initialize the table */
    folding_table[original_problem] = std::make_shared<std::pair<std::vector<Subproblem>, double>>(std::make_pair(std::vector<Subproblem>{}, std::numeric_limits<double>::infinity()));

    /* Solution Class 1: Join all relations in the block */
    double single_costs = 0;
    if (fold_costs.contains(original_problem)) {
        single_costs = fold_costs.at(original_problem);
    } else {
        single_costs = fold_costs[original_problem] = PT_order[original_problem].cost + YannakakisHeuristic::estimate_decompose_costs(G, original_problem, PT_order[original_problem], CE) + heuristic->estimate(G, adj_matrix, CE, PT_order, folded_mapping, problem, Subproblem());
    }
    folding_table[original_problem]->second = single_costs;
    folding_table[original_problem]->first = {original_problem};

    /* Solution Class 2: Join until all folds are left, which is only always possible if B(P) != P, signaled by the boolean flag in the problem P */

    /* Helper function to manage updates to best folds found so far, only used for two folds.
    * This will ALWAYS utilize original relations */
    auto update_two_fold = [&](const Subproblem left, const Subproblem right) {
        auto original_left = get_original_problem(left);
        auto original_right = get_original_problem(right);
        auto c_fold_double = [&](const Subproblem main, const Subproblem main_original, const Subproblem other) {
            if (fold_costs.contains(main_original)) {
                return fold_costs.at(main_original);
            }
            return fold_costs[main_original] = PT_order[main_original].cost + YannakakisHeuristic::estimate_decompose_costs(G, main_original, PT_order[main_original], CE) +  heuristic->estimate(G, adj_matrix, CE, PT_order, folded_mapping, main, other);
        };
        const double two_fold_costs = c_fold_double(left, original_left, right) + c_fold_double(right, original_right, left);
        if (two_fold_costs < folding_table[original_problem]->second)
        {
            folding_table[original_problem]->second = two_fold_costs;
            folding_table[original_problem]->first = {original_left, original_right};
        }
    };

    /* Again, we required different callback functions depending on whether we are in recursive mode or not */
    std::function<void(Subproblem, Subproblem)> folding_callback;

    if (use_tvc) {
        folding_callback = [&](const Subproblem left, const Subproblem right) -> void {
            update_two_fold(left, right);
        };
    } else {
        folding_callback = [&](const Subproblem folded_left, const Subproblem folded_right) -> void {
            update_mapping(folded_left, folded_right);
            update_two_fold(folded_left, folded_right);
        };
    }
    if (original_problem == original_block)
    {
        /* We only need top-level ccp's */
        MinCutAGaT{}.partition(adj_matrix, folding_callback, problem);
    }

    /* Solution Class 3: Use TVCs to generate smaller problems that can solve the underlying cycles *
     * Here, we offer two strategies: Greedily apply TVCs, to find smaller solutions, or a more exhaustive approach
     */

    /* Helper function for recursive evaluation of the best solution */
    auto evaluate_folded_graph = [&](AdjacencyMatrix& matrix, std::unordered_map<Subproblem, Subproblem, SubproblemHash>& rec_folded_mapping) {
        /* Find the best TVC solution */
        folding_table_entry_t solution = create_and_enumerate_problems(G, matrix, rec_folded_mapping, folding_table, folding_problem, fold_costs, PT_order, false);

        /* There might be greedily folded nodes which are not part of any block, which we now need to check against. */
        auto folded_nodes_in_solution = Subproblem(0);
        for (const auto fold: solution->first) {
            folded_nodes_in_solution |= fold;
        }

        /* Get unfolded nodes */
        for (const auto node_id: Subproblem::All(G.num_sources())) {
            if (const auto singleton = Subproblem::Singleton(node_id); rec_folded_mapping.contains(singleton)) {
                /* This node is folded, and might contain a relevant value */
                auto original_singleton = rec_folded_mapping[singleton];
                if (original_singleton != singleton and (original_singleton & folded_nodes_in_solution).empty()) {
                    auto fold_costs = PT_order[original_singleton].cost + YannakakisHeuristic::estimate_decompose_costs(G, original_singleton, PT_order[original_singleton], CE) + heuristic->estimate(G, adj_matrix, CE, PT_order, folded_mapping, original_singleton, Subproblem());
                    solution->first.emplace_back(original_singleton);
                    solution->second += fold_costs;
                }
            }
        }

        if (solution->second < folding_table[original_problem]->second)
        {
            folding_table[original_problem] = solution;
        }
    };

    /* Greedy approach */
    if (!Options::Get().ignore_tvcs)
    {
        AdjacencyMatrix folded_matrix(adj_matrix);

        /* Only evaluate when changes could be determined */
        if (std::unordered_map<Subproblem, Subproblem, SubproblemHash> rec_folded_mapping; get_greedy_folded_graph(adj_matrix, folded_matrix, folding_problem, rec_folded_mapping)) {
            evaluate_folded_graph(folded_matrix, rec_folded_mapping);
        }
        return folding_table[original_problem];
    }

    /* Just return the best solution found */
    return folding_table[original_problem];
}

bool Optimizer_ResultDB_utils::get_greedy_folded_graph(AdjacencyMatrix& current_matrix, AdjacencyMatrix& new_matrix, const folding_problem_t& folding_problem, std::unordered_map<Subproblem, Subproblem, SubproblemHash> &folded_mapping)
{
    std::vector<Subproblem> tvc_nodes;
    find_greedy_vertex_cuts(current_matrix, folding_problem, tvc_nodes);
    std::unordered_set<Subproblem, SubproblemHash> blocks_evaluated;
    create_folded_adjacency_matrix(tvc_nodes, current_matrix, new_matrix, folded_mapping);
    return !tvc_nodes.empty();
}


void Optimizer_ResultDB_utils::create_folded_adjacency_matrix(const std::vector<Subproblem>& folds, AdjacencyMatrix &old_matrix, AdjacencyMatrix &new_matrix, std::unordered_map<Subproblem, Subproblem, SubproblemHash> &folded_mapping)
{
    /* Assign each old node to a new node */
    std::vector<std::size_t> pairs(old_matrix.size(), 0);
    auto folded_nodes = Subproblem();
    std::unordered_map<Subproblem, Subproblem, SubproblemHash> old_folded_mapping;

    /* When we are in a recursive call, we need to use the existing mapping to create the new mapping */
    if (folded_mapping.empty())
    {
        for (const auto node_id: Subproblem::All(old_matrix.size()))
        {
            auto singleton = Subproblem::Singleton(node_id);
            old_folded_mapping.emplace(singleton, singleton);
        }
    } else {
        old_folded_mapping = folded_mapping;

        /* Reset mapping */
        folded_mapping = {};
    }
    auto deleted_nodes = Subproblem(0);

    /* Construct pairings for each fold */
    for (auto fold : folds)
    {
        std::vector<std::size_t> node_ids;

        /* Choose any node as reference node */
        const std::size_t reference_node = *fold.begin();
        for (const unsigned long node_id : fold)
        {
            pairs[node_id] = reference_node;
        }
        /* All nodes but the reference node are to be unused */
        deleted_nodes |= fold - Subproblem::Singleton(reference_node);

        if (not old_folded_mapping.contains(fold)) {
            auto original_problem = Subproblem();
            for (const auto node_id: fold) {
                /* It is assumed that each singleton is already contained in the mapping */
                original_problem |= old_folded_mapping[Subproblem::Singleton(node_id)];
            }
            old_folded_mapping[fold] = original_problem;
        }
        folded_mapping[Subproblem::Singleton(reference_node)] = old_folded_mapping[fold];
        folded_nodes |= fold;
    }

    /* Also add unaffected sources to the new adjacency matrix */
    for (const auto node_id : Subproblem::All(old_matrix.size()) - folded_nodes)
    {
        auto singleton = Subproblem::Singleton(node_id);
        folded_mapping[singleton] = singleton;
        pairs[node_id] = node_id;
    }

    /* Create matrix by adding new edges */
    for (const auto node_id : folded_nodes)
    {
        /* It was decided that this node was kept, do nothing */
        if (pairs[node_id] == node_id) {
            continue;
        }

        new_matrix[node_id] = Subproblem(0);
        const auto node_partner_problem = Subproblem::Singleton(pairs[node_id]);
        for (const auto neighbor_id : old_matrix[node_id])
        {
            /* Only update affected nodes */
            if (neighbor_id != pairs[neighbor_id]) {
                continue;
            }

            /* Reference node must not be included in itself */
            if (neighbor_id != pairs[node_id])
                new_matrix[neighbor_id] |= node_partner_problem;
            else
                new_matrix[neighbor_id] |= old_matrix[node_id];
        }
    }

    /* Remove invalid edges */
    for (const auto node_id: Subproblem::All(old_matrix.size())) {
        /* Remove reflexive edges */
        new_matrix[node_id] -= Subproblem::Singleton(node_id) | deleted_nodes;

    }


}

std::vector<std::vector<Subproblem>> Optimizer_ResultDB_utils::get_tvc_sets(const AdjacencyMatrix &M, const folding_problem_t &folding_problem)
{
    /* Result set */
    std::vector<std::vector<Subproblem>> tvc_sets;

    const auto problem = folding_problem.first;
    const auto block = folding_problem.second;

    /* First, identify all TVCs in the problem */
    const std::vector<Subproblem> tvc_nodes = M.find_two_vertex_cuts(block, problem);

    /* Start with 1 to avoid the empty set */
    const size_t max_set = 1 << tvc_nodes.size();
    for (size_t i = 1; i < max_set; i++)
    {
        /* Traverse the set and find out which TVC belongs to which fold */
        std::vector<Subproblem> preliminary_tvc_set; // New TVC fold, preliminary in case of merges!
        std::unordered_map<size_t, size_t> node_to_fold; // map from each node_id to their current position in the fold vector
        auto traversed = Subproblem();

        for (auto new_problem = Subproblem(i); const size_t tvc_id : new_problem)
        {
            auto tvc_problem = tvc_nodes[tvc_id];
            if (auto intersection = tvc_problem & traversed; intersection.empty()) {
                for (auto node_id: tvc_problem) node_to_fold.emplace(node_id, preliminary_tvc_set.size());
                preliminary_tvc_set.emplace_back(tvc_problem);
            } else {
                /* Get any intersecting node */
                auto first_intersecting_node = intersection.begin();
                const auto anchor_fold_id = node_to_fold[*first_intersecting_node];
                auto new_fold = tvc_problem ;
                for (auto node_id: intersection) {
                    new_fold |= preliminary_tvc_set[node_to_fold[node_id]];
                }
                for (auto node_id: tvc_problem) node_to_fold.emplace(node_id, anchor_fold_id);
                preliminary_tvc_set[anchor_fold_id] = new_fold;
                ++first_intersecting_node;
                if (first_intersecting_node != intersection.end()) preliminary_tvc_set[node_to_fold[*first_intersecting_node]] = Subproblem(0);
            }
            traversed |= tvc_problem;
        }
        /* Create final, new TVC set */
        std::vector<Subproblem> final_tvc_set;
        for (const auto tvc_problem: preliminary_tvc_set) {
            if (not tvc_problem.empty()) final_tvc_set.emplace_back(tvc_problem);
        }
        tvc_sets.emplace_back(final_tvc_set);
    }

    return tvc_sets;
}

void Optimizer_ResultDB_utils::find_greedy_vertex_cuts(const AdjacencyMatrix &M, const folding_problem_t &folding_problem, std::vector<Subproblem> &folds) {

    const auto problem = folding_problem.first;
    const auto block = folding_problem.second;

    M_insist(block.size() > 2, "Block must contain at least 3 nodes!");

    /* Find all TVCs in the block */
    const std::vector<Subproblem> vertex_cuts = M.find_two_vertex_cuts(block, problem);
    std::unordered_map<std::size_t, std::size_t> node_counts;

    /* Check for overlaps between different vertex cut pairs, and sort them according to the lowest overlap count */
    for (Subproblem pair : vertex_cuts) {
       for (size_t pair_node : pair) {
           if (node_counts.contains(pair_node)) {
               node_counts[pair_node] += 1;
           } else {
               node_counts.emplace(pair_node, 0);
           }
       }
    }

    std::unordered_map<Subproblem, std::size_t, SubproblemHash> cut_overlaps;
    for (Subproblem pair : vertex_cuts) {
        cut_overlaps.emplace(pair, 0);
        for (size_t pair_node : pair) {
            cut_overlaps[pair] += node_counts[pair_node];
        }
    }

    /* Use Counting Sort */
    std::vector<std::size_t> helper(vertex_cuts.size(), 0);
    std::vector<Subproblem> sorted_vertex_cuts(vertex_cuts.size());

    for (auto vertex_cut : vertex_cuts) {
        helper[cut_overlaps[vertex_cut]] += 1;
    }

    for (size_t i = 1; i < helper.size(); i++) {
        helper[i] += helper[i-1];
    }

    for (int i = vertex_cuts.size() - 1; i >= 0; i--) {
        sorted_vertex_cuts[helper[cut_overlaps[vertex_cuts[i]]] - 1] = vertex_cuts[i];
        helper[cut_overlaps[vertex_cuts[i]]] -= 1;
    }

    auto already_used = Subproblem(0);
    for (Subproblem pair : sorted_vertex_cuts) {
        /* One of the pairs might already be used earlier due to overlaps */
        if ((pair & already_used).empty()) {
            folds.emplace_back(pair);
            already_used |= pair;
        }
    }
}

template <typename PlanTable>
double Optimizer_ResultDB_utils::compute_costs_for_GHD_AGM(QueryGraph &G, std::vector<Subproblem>& join_attrs, GHNode& GHD, PlanTable &PT, const CardinalityEstimator &CE, bool use_table, std::unordered_map<Subproblem, double, SubproblemHash> &agm_costs) {

    auto compute_agm_bound_for_subproblem = [&](const Subproblem problem) {
        if (use_table and agm_costs.contains(problem)) {
            return agm_costs[problem];
        }

        if (problem.size() == 1) {
            agm_costs[problem] = std::log(CE.predict_cardinality(*PT[problem].model));
            return agm_costs[problem];
        }

        /* Collect relevant joins for this problem, i.e., the joins which only happen within this problem */
        std::vector<Subproblem> temp_join_problems(G.num_joins());
        auto all_join_problems = Subproblem();


        for (const auto node_id: problem) {
            for (const auto attr_id: join_attrs[node_id]) {
                temp_join_problems[attr_id] |= Subproblem::Singleton(node_id);
            }
        }

        std::vector<Subproblem> join_problems;
        for (auto temp_join: temp_join_problems) {
            if (!temp_join.empty()) {
                join_problems.emplace_back(temp_join);
            }
        }



        /*
        for (int i = 0; i < G.joins().size(); i++) {
            bool part_of_problem = false;
            auto data_sources_problem = Subproblem();
            const auto &join = G.joins[i];
            for (const auto &ds: join->sources()) {
                auto relation_problem = Subproblem::Singleton(ds.get().id());
                if (relation_problem.is_subset(problem)) {
                    part_of_problem = true;
                    data_sources_problem |= relation_problem;
                }
            }
            if (part_of_problem) {
                join_problems.emplace_back(data_sources_problem);
                all_join_problems |= data_sources_problem;
            }
        }


        /* Add artificial variable for unjoined relations
        for (const auto node_id: problem - all_join_problems) {
            join_problems.emplace_back(Subproblem::Singleton(node_id));
        }
        */

        /* Collect sizes of relations */
        std::vector<std::size_t> relation_sizes;
        std::unordered_map<std::size_t, std::size_t> rel_to_pos;
        for (const auto rel_id: problem) {
            relation_sizes.emplace_back(CE.predict_cardinality(*PT[Subproblem::Singleton(rel_id)].model));
            rel_to_pos[rel_id] = relation_sizes.size() - 1;
        }

        /* Collect log-based size of relations for linear programming */
        std::vector<double> relation_log_sizes;
        for (const auto &size : relation_sizes) {
            relation_log_sizes.emplace_back(std::log(size));
        }

        /* Setup linear programming model */
        glp_prob *lp = glp_create_prob();
        glp_set_obj_dir(lp, GLP_MIN);

        /* Setup first step for constrains */
        glp_add_rows(lp, join_problems.size());
        for (int i = 0; i < join_problems.size(); i++) {
            glp_set_row_bnds(lp, i + 1, GLP_LO, 1.0, 0.0);
        }

        /* Setup variables, one for each relation in the problem */
        glp_add_cols(lp, problem.size());
        for (int i = 0; i < problem.size(); i++) {
            /* Variable must be non-negative */
            glp_set_col_bnds(lp, i + 1, GLP_LO, 0.0, 0.0);
        }

        /* Setup coefficients */
        for (int i = 0; i < problem.size(); i++) {
            /* Variable must be non-negative */
            glp_set_obj_coef(lp, i + 1, relation_log_sizes[i]);
        }

        /* Setup matrix */
        int array_size = 0;
        for (const auto join_problem: join_problems) {
            array_size += join_problem.size();
        }

        /* Define arrays */
        int row[array_size + 1], col[array_size + 1];
        double coef[array_size + 1];

        int idx_inner = 1;
        int idx_outer = 1;
        for (const auto join_problem: join_problems) {
            for (const auto rel: join_problem) {
                /* Add coefficient for the variable */
                row[idx_inner] = idx_outer;
                col[idx_inner] = rel_to_pos[rel] + 1;
                coef[idx_inner] = 1.0;
                idx_inner++;
            }
            idx_outer++;
        }

        /* Load matrix */
        glp_load_matrix(lp, array_size, row, col, coef);

        /* Disable output prints (why is this even on by default??) */
        glp_term_out(GLP_OFF);

        /* Solve the linear program */
        glp_simplex(lp, nullptr);

        /* Compute AGM bound based on coefficients */
        double agm_bound = 0;
        for (auto rel: problem) {
            const int position = rel_to_pos[rel];
            agm_bound += relation_log_sizes[position] * glp_get_col_prim(lp, position + 1);
        }

        if (use_table) {
            agm_costs[problem] = agm_bound;
        }

        return agm_bound;
    };

    /* Compute the AGM bound for each subproblem in the GHD, take the maximum as costs for this GHD */
    double max_agm_bound = 0.0;
    for (auto subproblem : GHD) {
        const double agm_bound = compute_agm_bound_for_subproblem(subproblem);
        if (agm_bound > max_agm_bound) {
            max_agm_bound = agm_bound;
        }
    }

    return max_agm_bound;
}

template <typename PlanTable>
std::vector<Subproblem> Optimizer_ResultDB_utils::select_GHD_heuristically(QueryGraph &G, std::vector<std::vector<Subproblem>> &GHDs, const CardinalityEstimator &CE, PlanTable &PT) {
    /* First, we want to filter our GHDs based on the height of GHD tree */
    std::vector<std::vector<Subproblem>> filtered_GHDs;

    size_t min_height = std::numeric_limits<size_t>::max();
    std::unordered_map<size_t, std::vector<int>> ghd_heights;

    /* Find min height */
    for (int i = 0; i < GHDs.size(); i++) {
        auto &ghd = GHDs[i];
        /* Construct new, folded matrix, i.e., a new tree */
        AdjacencyMatrix folded_matrix(G.adjacency_matrix());
        std::unordered_map<Subproblem, Subproblem, SubproblemHash> new_folded_mapping{};
        create_folded_adjacency_matrix(ghd, G.adjacency_matrix(), folded_matrix, new_folded_mapping);

        /* The last subproblem is the root, so use that to compute the height */
        size_t curr_height = folded_matrix.get_height_with_root(*ghd.back().begin());
        if (ghd_heights.contains(curr_height)) {
            ghd_heights[curr_height].emplace_back(i);
        } else {
            ghd_heights[curr_height] = {i};
        }

        if (curr_height < min_height) {
            min_height = curr_height;
        }
    }

    std::unordered_map<size_t, std::vector<int>> ghd_outputs;
    size_t max_relations_per_root = 0;
    int chosen_idx = 0;

    /* Go through the GHDs with the minimal size, and return those with the maximum of output relations within the root */
    for (const auto idx: ghd_heights[min_height]) {
        auto &ghd = GHDs[idx];

        size_t relations_for_root = 0;
        if (PT.has_plan(ghd.back())) {
            relations_for_root = PT[ghd.back()].tuple_size;
        } else {
            for (const auto node_id: ghd.back()) {
                relations_for_root += PT[Subproblem::Singleton(node_id)].tuple_size;
            }
            PT[ghd.back()].tuple_size = relations_for_root;
        }

        if (relations_for_root > max_relations_per_root) {
            max_relations_per_root = relations_for_root;
            chosen_idx = idx;
        }
    }

    return std::move(GHDs[chosen_idx]);

}

template<typename PlanTable>
std::vector<Subproblem> Optimizer_ResultDB_utils::select_GHD_c_fold(QueryGraph &G, std::vector<std::vector<Subproblem> > &GHDs, const CardinalityEstimator &CE, PlanTable &PT) {
    const auto &C = Catalog::Get();

    /* Evaluate for each GHD */
    auto join_order_callback = [&](const Subproblem left, const Subproblem right) -> void
    {
        /* Only update the plan table */
        PT.update(G, CE, C.cost_function(), left, right, cnf::CNF{});
    };

    double best_costs = std::numeric_limits<double>::max();
    int best_idx = -1;
    std::unordered_map<Subproblem, Subproblem, SubproblemHash> folded_mapping;

    for (int i = 0; i < GHDs.size(); i++) {
        auto& ghd = GHDs[i];
        double curr_costs = 0;
        /* Determine optimal join order for each subproblem of the GHD */
        for (auto subproblem: ghd) {
            if (not PT.has_plan(subproblem))
            {
                /* Use DP_CCP */
                G.adjacency_matrix().for_each_CSG_pair_undirected(subproblem, join_order_callback);
            }
            /* Perform some required precomputations for the Yannakakis Heuristic */
            std::unique_ptr<YannakakisHeuristic> heuristic = std::make_unique<WeakCardinalityHeuristic>(WeakCardinalityHeuristic(PT, subproblem, G, G.adjacency_matrix(), CE, folded_mapping));

            // + YannakakisHeuristic::estimate_decompose_costs(G, subproblem, PT[subproblem], CE)
            curr_costs += YannakakisHeuristic::estimate_decompose_costs(G, subproblem, PT[subproblem], CE) + PT[subproblem].cost + heuristic->estimate(G, G.adjacency_matrix(), CE, PT, folded_mapping, subproblem, Subproblem());
        }

        // std::cerr << "C_Fold: " << curr_costs << ", idx: " << i << "\n";

        if (curr_costs < best_costs) {
            best_costs = curr_costs;
            best_idx = i;
        }
    }

    return std::move(GHDs[best_idx]);

}


template <typename PlanTable>
Optimizer_ResultDB_utils::folding_table_entry_t Optimizer_ResultDB_utils::get_best_GHD(QueryGraph &G, PlanTable &PT, const CardinalityEstimator &CE) {

    const auto joins_per_relation = G.get_joins_for_data_sources();

    auto compute_node_combinations = [&](std::vector<std::vector<std::shared_ptr<GHNode>>>& nodes_per_partition, int i, auto&& rec) -> std::vector<std::vector<std::shared_ptr<GHNode>>> {
        std::vector<std::vector<std::shared_ptr<GHNode>>> result;
        if (i == nodes_per_partition.size() - 1) {
            for (const auto &node: nodes_per_partition[i]) {
                std::vector comb = {node};
                result.emplace_back(comb);
            }
            return result;
        }
        auto intermediate_result = rec(nodes_per_partition, i + 1, rec);
        for (auto &node: nodes_per_partition[i]) {
            for (auto &children: intermediate_result) {
                result.push_back(children);
                result.back().emplace_back(node);
            }
        }
        return result;
    };

    auto can_be_extended = [&](const Subproblem C_attr, const Subproblem R) {
        for (const auto node_id: R) {
            if (joins_per_relation[node_id].is_subset(C_attr)) {
                return true;
            }
        }
        return false;
    };

    auto enumerate = [&](const Subproblem E, const Subproblem P, auto&& rec) -> std::vector<std::shared_ptr<GHNode>> {

        auto get_joins_for_subset = [&](const Subproblem C) -> Subproblem {
            auto joins = Subproblem(0);

            for (const auto node_id : C) {
                joins |= joins_per_relation[node_id];
            }

            return joins;
        };

        /* There is only one way to decompose a singleton */
        if (E.is_singleton()) return {std::make_shared<GHNode>(GHNode(E))};

        std::vector<std::shared_ptr<GHNode>> result;
        const auto P_attr = get_joins_for_subset(P);

        for (auto C(least_subset(E)); C != Subproblem(0); C = Subproblem(next_subset(C, E))) {
            const auto R = E - C;

            /* Ignore Cartesian Products */
            if (not G.adjacency_matrix().is_connected(C)) continue;

            /* Check whether the current subset would result in valid GHD, i.e., check whether the RIP is satisfied */
            const auto R_attr = get_joins_for_subset(R);
            const auto C_attr = get_joins_for_subset(C);

            /* Ignore the set if it could be extended */
            if (can_be_extended(C_attr, R)) continue;

            if (!(P_attr & R_attr).is_subset(C_attr)) continue;

            /* Compute the partition(s) resulting from this subset */
            auto partitions = G.adjacency_matrix().get_partitions_after_removal(E, C);

            /* No Partitions => E = C */
            if (partitions.empty()) {
                result.emplace_back(std::make_shared<GHNode>(GHNode(E)));
                continue;
            }

            std::vector<std::vector<std::shared_ptr<GHNode>>> partition_nodes;

            /* Recursively compute the GHDs of all partitions and combine them with the current subset */
            for (const auto &partition : partitions) {
                auto sub_ghds = rec(partition, C, rec);
                partition_nodes.emplace_back(sub_ghds);
            }

            /* Compute each possible combination of subtrees */
            auto subtree_combs = compute_node_combinations(partition_nodes, 0, compute_node_combinations);

            /* Construct for each possible combination the corresponding GHNode */
            for (auto &subtree_comb: subtree_combs) {
                result.emplace_back(std::make_shared<GHNode>(GHNode(C, subtree_comb)));
            }

        }

        return std::move(result);
    };

    /* Get all GHDs for the entire graph */
    auto GHDs = enumerate(Subproblem::All(G.num_sources()), Subproblem(0), enumerate);

    /* Evaluate GHDs based on AGM bound */
    double best_bound = std::numeric_limits<double>::max();
    std::vector<double> bounds_for_ghd;
    std::unordered_map<Subproblem, double, SubproblemHash> agm_costs;
    auto join_attrs = G.get_join_attributes_for_data_sources();

    for (auto &ghd: GHDs) {
        auto bound = compute_costs_for_GHD_AGM(G, join_attrs, *ghd, PT, CE, true, agm_costs);
        bounds_for_ghd.emplace_back(bound);
        if (bound < best_bound) {
            best_bound = bound;
        }
    }

    /* Further process all GHDs that within delta of the best bound */
    constexpr double delta = 0.01;
    std::vector<std::vector<Subproblem>> ghds_within_delta;

    for (int i = 0; i < GHDs.size(); i++) {
        if (std::abs(bounds_for_ghd[i] - best_bound) < delta) {
            ghds_within_delta.emplace_back();
            for (auto node: *GHDs[i]) {
                ghds_within_delta.back().emplace_back(node);
            }
        }
    }

    std::vector<Subproblem> best_ghd = {};
    if (Options::Get().result_db_optimizer == Options::GHD_Heuristic)
        best_ghd = select_GHD_heuristically(G, ghds_within_delta, CE, PT);
    else
        best_ghd = select_GHD_c_fold(G, ghds_within_delta, CE, PT);

    return std::make_shared<std::pair<std::vector<Subproblem>, double>>(best_ghd, -1);

}


template <typename PlanTable>
std::pair<std::unique_ptr<Producer>, bool> Optimizer_ResultDB_utils::dp_resultdb_with_plantable(QueryGraph &G) {
    PlanTable PT_order(G);

    auto &C = Catalog::Get();
    const auto &DB = C.get_database_in_use();
    auto &CE = DB.cardinality_estimator();

    /* Create source plans for base relations */
    auto current_source_plans = optimize_source_plans(G, PT_order);
    auto complete_problem = Subproblem::All(G.num_sources());

    auto join_order_callback = [&](const Subproblem left, const Subproblem right) -> void
    {
        /* Only update the plan table */
        PT_order.update(G, CE, C.cost_function(), left, right, cnf::CNF{});
    };

    /* Best ResultDB_Decompose Plan */
    if (not PT_order.has_plan(complete_problem) and Options::Get().result_db_optimizer == Options::DP_ResultDB)
    {
        /* Use DP_CCP */
        G.adjacency_matrix().for_each_CSG_pair_undirected(complete_problem, join_order_callback);
    }


    /* Enumerate all possible fold problems and get the best ones */
    std::unordered_map<Subproblem, Subproblem, SubproblemHash> folded_mapping{};
    std::unordered_map<Subproblem, folding_table_entry_t, SubproblemHash> folding_table{};
    std::unordered_map<Subproblem, double, SubproblemHash> fold_costs{};
    const folding_problem_t folding_problem = std::make_pair(complete_problem, complete_problem);
    auto solution = std::make_shared<std::pair<std::vector<Subproblem>, double>>(std::vector<Subproblem>{}, 0);
    if (G.is_cyclic()) {
        if (Options::Get().result_db_optimizer == Options::GHD_Heuristic or Options::Get().result_db_optimizer == Options::GHD_C_Fold) {
            solution = get_best_GHD(G, PT_order, CE);
        } else {
            solution = create_and_enumerate_problems(G, G.adjacency_matrix(), folded_mapping, folding_table, folding_problem, fold_costs, PT_order, true);
        }
    }

    /* Helper function to determine the best way to best semi-join order on the final folds chosen */
    auto compute_semi_join_reducer_costs = [&] {
        /* We do not want to consider semi-join heuristics in the final comparisons, so we just recompute the existing costs for each
         * problem we have computed */
        double folding_costs = 0;
        double join_costs = 0;
        double decompose_costs = 0;
        for (auto problem : solution->first)
        {
            join_costs += PT_order[problem].cost;
            decompose_costs += YannakakisHeuristic::estimate_decompose_costs(G, problem, PT_order[problem], CE);
            folding_costs += PT_order[problem].cost + YannakakisHeuristic::estimate_decompose_costs(G, problem, PT_order[problem], CE);
        }

        /* Construct new, folded matrix */
        AdjacencyMatrix folded_matrix(G.adjacency_matrix());
        std::unordered_map<Subproblem, Subproblem, SubproblemHash> new_folded_mapping{};
        create_folded_adjacency_matrix(solution->first, G.adjacency_matrix(), folded_matrix, new_folded_mapping);

        /* Create new base models for the TD_Root numeration */
        std::vector<std::unique_ptr<DataModel>> base_models;
        std::unordered_set<std::size_t> required_reductions;
        for (auto node_id : complete_problem)
        {
            /* Add anything for unused relations */
            if (folded_matrix[node_id].empty()) {
                base_models.emplace_back(CE.copy(*PT_order[Subproblem(1)].model));
                continue;
            }

            Subproblem related_problem = new_folded_mapping[Subproblem::Singleton(node_id)];
            base_models.emplace_back(CE.copy(*PT_order[related_problem].model));
            if (PT_order[related_problem].tuple_size != 0)
                required_reductions.emplace(node_id);
        }
        auto [reducer_order, reducer_costs] = enumerate_semi_join_reduction_order(G, required_reductions, folded_matrix, CE, base_models);
        // std::cerr << "Overall costs: " << reducer_costs + folding_costs << ", Decomposing Costs: " << decompose_costs << ", Join Costs: " << join_costs << ", Reducing Costs: " << reducer_costs << "\n";
        return std::make_tuple(reducer_order, reducer_costs + folding_costs);
    };

    /* Helper function to create the best decompose plan */
    auto decompose_plan = [&] -> std::pair<std::unique_ptr<Producer>, bool>
    {
        auto decompose_op = std::make_unique<DecomposeOperator>(std::cout, std::move(G.projections()),
                                                                std::move(G.sources()));
        auto single_table_plan = construct_join_order(G, PT_order, complete_problem, current_source_plans);
        decompose_op->add_child(single_table_plan);
        return {std::move(decompose_op), true};
    };

    /* Helper function to create the best semi-join reduction plan */
    auto semi_join_reducer_plan = [&]() -> std::pair<std::unique_ptr<Producer>, bool>
    {
        /* Create source plans for folds, add relations to the solution which are not part of any fold */
        auto folded_relations = Subproblem(0);
        for (auto fold: solution->first) {
            folded_relations |= fold;
        }
        for (const auto node_id: complete_problem - folded_relations) {
            solution->first.emplace_back(Subproblem::Singleton(node_id));
        }
        auto source_plans = std::make_unique<Producer *[]>(solution->first.size());
        std::vector<std::unique_ptr<DataModel>> base_models;
        const std::unordered_set<std::size_t> required_reductions;
        for (size_t i = 0; i < solution->first.size(); i++)
        {
            if (not PT_order.has_plan(solution->first[i])) {
                G.adjacency_matrix().for_each_CSG_pair_undirected(solution->first[i], join_order_callback);
            }
            base_models.emplace_back(CE.copy(*PT_order[solution->first[i]].model));
            base_models[i]->assign_to(Subproblem::Singleton(i));
            source_plans[i] = construct_join_order(G, PT_order, solution->first[i], current_source_plans);
        }
        if (solution->first.size() == 1) {
            return decompose_plan();
        }

        /* Fold the join graph, translate fold into fold_t */
        std::vector<fold_t> translated_folds;
        for (const auto& fold: solution->first) {
            fold_t translated_fold;
            for (const auto node_id: fold) {
                translated_fold.emplace(node_id);
            }
            translated_folds.emplace_back(translated_fold);
        }
        fold_query_graph(G, translated_folds);

        /* TODO: Avoid repeated computation of the same semi-join order, not a huge performance decrease though */
        auto [reducer_order, costs] = enumerate_semi_join_reduction_order(G, required_reductions, G.adjacency_matrix(), CE, base_models);

        // std::cerr << "Just Reduction: " << costs << ", Decompose: " << "\n";
        const auto num_sources = G.num_sources();

        // Create semi-join reducer plan
        auto semi_join_reduction_op = std::make_unique<SemiJoinReductionOperator>(std::move(G.projections()));
        semi_join_reduction_op->semi_join_reduction_order() = std::move(reducer_order);
        semi_join_reduction_op->sources() = std::move(G.sources());
        semi_join_reduction_op->joins() = std::move(G.joins());

        /* Add source plans as children. */
        for (std::size_t i = 0; i < num_sources; ++i)
            semi_join_reduction_op->add_child(source_plans[i]);
        return {std::move(semi_join_reduction_op), true};
    };
    if (Options::Get().result_db_optimizer == Options::TD_Root or Options::Get().result_db_optimizer == Options::GHD_Heuristic or Options::Get().result_db_optimizer == Options::GHD_C_Fold) {
        return semi_join_reducer_plan();
    }
    /* Best ResultDB_SemiJoin Plan */
    auto [reducer_order, reducer_costs] = compute_semi_join_reducer_costs();
    double decompose_costs = 1.9 * PT_order[complete_problem].cost + YannakakisHeuristic::estimate_decompose_costs(G, complete_problem, PT_order[complete_problem], CE);

    /* Decide whether to use ResultDB_SemiJoin or ResultDB_Decompose */
    // std::cerr << "Reducer: " << reducer_costs << ", Decompose: " << PT_order[complete_problem].cost << " + " << YannakakisHeuristic::estimate_decompose_costs(G, complete_problem, PT_order[complete_problem], CE) << "\n";
    if (reducer_costs < decompose_costs) return semi_join_reducer_plan();
    return decompose_plan();
}

double Optimizer_ResultDB_utils::optimize(QueryGraph &G, std::vector<Subproblem> &folding_problems, std::unique_ptr<Producer*[]> &source_plans, std::vector<std::unique_ptr<DataModel>> &base_models)
{
    switch (Options::Get().plan_table_type)
    {
        case Options::PT_auto: {
            /* Select most suitable type of plan table depending on the query graph structure.
             * Currently a simple heuristic based on the number of data sources.
             * TODO: Consider join edges too.  Eventually consider #CSGs. */
            if (G.num_sources() <= 15) {
                return optimize_with_plantable<PlanTableSmallOrDense>(G, folding_problems, source_plans, base_models);
            } else {
                return optimize_with_plantable<PlanTableLargeAndSparse>(G, folding_problems, source_plans, base_models);
            }
        }

        case Options::PT_SmallOrDense: {
            return optimize_with_plantable<PlanTableSmallOrDense>(G, folding_problems, source_plans, base_models);
        }

        case Options::PT_LargeAndSparse: {
            return optimize_with_plantable<PlanTableLargeAndSparse>(G, folding_problems, source_plans, base_models);
        }
    }
}

template<typename PlanTable>
double Optimizer_ResultDB_utils::optimize_with_plantable(QueryGraph &G, std::vector<Subproblem> &folding_problems, std::unique_ptr<Producer*[]> &source_plans, std::vector<std::unique_ptr<DataModel>> &base_models)
{
    PlanTable PT(G);
    auto &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

    /* Create source plans for base relations */
    auto current_source_plans = optimize_source_plans(G, PT);
    auto singletons = Subproblem::All(G.num_sources());

    std::size_t next_idx = 0;

    for (auto singleton_id : singletons) {
        source_plans[next_idx] = current_source_plans[singleton_id];
        PT[Subproblem::Singleton(singleton_id)].model->assign_to(Subproblem::Singleton(next_idx));
        base_models.emplace_back(std::move(PT[Subproblem::Singleton(singleton_id)].model));
        next_idx++;
    }
    return 0;
}

template<typename PlanTable>
void Optimizer_ResultDB_utils::optimize_join_order(const QueryGraph &G, PlanTable &PT, Subproblem folding_problem) {
    Catalog &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

#ifndef NDEBUG
    if (Options::Get().statistics) {
        std::size_t num_CSGs = 0, num_CCPs = 0;
        auto inc_CSGs = [&num_CSGs](Subproblem) { ++num_CSGs; };
        auto inc_CCPs = [&num_CCPs](Subproblem, Subproblem) { ++num_CCPs; };
        G.adjacency_matrix().for_each_CSG_undirected(folding_problem, inc_CSGs);
        G.adjacency_matrix().for_each_CSG_pair_undirected(folding_problem, inc_CCPs);
        std::cout << num_CSGs << " CSGs, " << num_CCPs << " CCPs" << std::endl;
    }
#endif

    auto callback = [&](Subproblem left, Subproblem right) {
        cnf::CNF condition; // TODO use join condition
        PT.update(G, CE, C.cost_function(), left, right, condition);
    };
    M_TIME_EXPR(G.adjacency_matrix().for_each_CSG_pair_undirected(folding_problem, callback), "Plan for RESULTDB enumeration", C.timer());

    PT[folding_problem].tuple_size = PT[PT[folding_problem].left].tuple_size + PT[PT[folding_problem].right].tuple_size;

    if (Options::Get().statistics) {
        std::cout << "Est. total cost: " << PT.get_final().cost
                  << "\nPlan cost: " << PT[PT.get_final().left].cost + PT[PT.get_final().right].cost
                  << std::endl;
    }
}



template <typename PlanTable>
Producer *Optimizer_ResultDB_utils::construct_join_order(const QueryGraph &G, const PlanTable &PT, Subproblem problem,
                                                         std::unique_ptr<Producer *[]> &source_plans)
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    std::vector<std::reference_wrapper<Join>> joins;
    for (auto &J : G.joins())
        joins.emplace_back(*J);

    /* Use nested lambdas to implement recursive lambda using CPS. */
    const auto construct_recursive = [&](Subproblem s) -> Producer *
    {
        auto construct_plan_impl = [&](Subproblem s, auto &construct_plan_rec) -> Producer *
        {
            auto subproblems = PT[s].get_subproblems();
            if (subproblems.empty())
            {
                M_insist(s.size() == 1);
                return source_plans[*s.begin()];
            }
            else
            {
                /* Compute plan for each sub problem.  Must happen *before* calculating the join predicate. */
                std::vector<Producer *> sub_plans;
                for (auto sub : subproblems)
                    sub_plans.push_back(construct_plan_rec(sub, construct_plan_rec));

                /* Calculate the join predicate. */
                cnf::CNF join_condition;
                for (auto it = joins.begin(); it != joins.end();)
                {
                    Subproblem join_sources;
                    /* Compute subproblem of sources to join. */
                    for (auto ds : it->get().sources())
                        join_sources(ds.get().id()) = true;

                    if (join_sources.is_subset(s))
                    { // possible join
                        join_condition = join_condition and it->get().condition();
                        it = joins.erase(it);
                    }
                    else
                    {
                        ++it;
                    }
                }

                /* Construct the join. */
                auto join = std::make_unique<JoinOperator>(join_condition);
                for (auto sub_plan : sub_plans)
                    join->add_child(sub_plan);
                auto join_info = std::make_unique<OperatorInformation>();
                join_info->subproblem = s;
                join_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
                join->info(std::move(join_info));
                return join.release();
            }
        };
        return construct_plan_impl(s, construct_plan_impl);
    };

    return construct_recursive(problem);
}

template <typename PlanTable>
std::unique_ptr<Producer *[]> Optimizer_ResultDB_utils::optimize_source_plans(const QueryGraph &G, PlanTable &PT)
{
    auto &C = Catalog::Get();
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    const auto num_sources = G.sources().size();
    auto source_plans = std::make_unique<Producer *[]>(num_sources);
    std::vector<size_t> tuple_sizes;
    G.get_projection_sizes_of_subproblems(tuple_sizes);
    for (auto &ds : G.sources())
    {
        Subproblem s = Subproblem::Singleton(ds->id());
        if (auto bt = cast<BaseTable>(ds.get()))
        {
            /* Produce a scan for base tables. */
            PT[s].cost = 0;
            PT[s].model = CE.estimate_scan(G, s);
            PT[s].tuple_size = tuple_sizes[ds->id()];
            auto &store = bt->table().store();
            auto source = new ScanOperator(store, bt->name().assert_not_none());
            source_plans[ds->id()] = source;

            /* Set operator information. */
            auto source_info = std::make_unique<OperatorInformation>();
            source_info->subproblem = s;
            source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
            source->info(std::move(source_info));
        }
        else
        {
            /* Recursively solve nested queries. */
            auto &Q = as<Query>(*ds);
            Optimizer Opt(C.plan_enumerator(), C.cost_function());
            auto [sub_plan, sub] = Opt.optimize(Q.query_graph());

            /* If an alias for the nested query is given and the nested query was not introduced as a fold, i.e. it does
             * not start with '$', prefix every attribute with the alias. */
            if (Q.alias().has_value() and *Q.alias()[0] != '$')
            {
                M_insist(is<ProjectionOperator>(sub_plan), "only projection may rename attributes");
                Schema S;
                for (auto &e : sub_plan->schema())
                    S.add({Q.alias(), e.id.name}, e.type, e.constraints);
                sub_plan->schema() = S;
            }

            /* Update the plan table with the `DataModel` and cost of the nested query and save the plan in the array of
             * source plans. */
            PT[s].cost = sub.cost;
            sub.model->assign_to(s); // adapt model s.t. it describes the result of the current subproblem
            PT[s].model = std::move(sub.model);
            PT[s].tuple_size = tuple_sizes[ds->id()];
            /* Save the plan in the array of source plans. */
            source_plans[ds->id()] = sub_plan.release();
        }

        /* Apply filter, if any. */
        if (ds->filter().size())
        {
            /* Update data model with filter. */
            auto new_model = CE.estimate_filter(G, *PT[s].model, ds->filter());
            PT[s].model = std::move(new_model);

            /* Optimize the filter by splitting into smaller filters and ordering them. */
            std::vector<cnf::CNF> filters = Optimizer::optimize_filter(ds->filter());
            Producer *filtered_ds = source_plans[ds->id()];

            /* Construct a plan as a sequence of filters. */
            for (auto &&filter : filters)
            {
                if (filter.size() == 1 and filter[0].size() > 1)
                { // disjunctive filter
                    auto tmp = std::make_unique<DisjunctiveFilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }
                else
                {
                    auto tmp = std::make_unique<FilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }
            }

            source_plans[ds->id()] = filtered_ds;
        }

        /* Set operator information. */
        auto source = source_plans[ds->id()];
        auto source_info = std::make_unique<OperatorInformation>();
        source_info->subproblem = s;
        source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model); // includes filters, if any
        source->info(std::move(source_info));
    }
    return source_plans;
}

std::unique_ptr<Producer *[]> Optimizer_ResultDB_utils::solve_cycles_without_enum(QueryGraph &G, std::vector<std::unique_ptr<DataModel>> &base_models)
{
    std::vector<fold_t> folds = compute_folds(G);
    fold_query_graph(G, folds);
    auto source_plans = std::make_unique<Producer *[]>(G.num_sources());
    std::vector<Subproblem> folding_problems;
    optimize(G, folding_problems, source_plans, base_models);
    return source_plans;
}

std::pair<std::unique_ptr<Producer>, bool> Optimizer_ResultDB_utils::dp_resultdb(QueryGraph &G)
{
    switch (Options::Get().plan_table_type)
    {
    case Options::PT_auto:
    {
        /* Select most suitable type of plan table depending on the query graph structure.
         * Currently a simple heuristic based on the number of data sources.
         * TODO: Consider join edges too.  Eventually consider #CSGs. */
        if (G.num_sources() <= 15)
        {
            return dp_resultdb_with_plantable<PlanTableSmallOrDense>(G);
        }
        else
        {
            return dp_resultdb_with_plantable<PlanTableLargeAndSparse>(G);
        }
    }

    case Options::PT_SmallOrDense:
    {
        return dp_resultdb_with_plantable<PlanTableSmallOrDense>(G);
    }

    case Options::PT_LargeAndSparse:
    {
        return dp_resultdb_with_plantable<PlanTableLargeAndSparse>(G);
    }
    }
}

std::pair<std::unique_ptr<Producer>, bool>
Optimizer_ResultDB::operator()(QueryGraph &G) const
{
    auto &C = Catalog::Get();
    auto &DB = C.get_database_in_use();
    auto &CE = DB.cardinality_estimator();

    /*----- Perform pre-optimizations on the QueryGraph. -----*/
    for (auto &pre_opt : C.pre_optimizations())
        (*pre_opt.second).operator()(G);

    if (G.sources().size() == 0)
        return {std::make_unique<ProjectionOperator>(G.projections()), false};

    /*----- Check that query graph is compatible. If not, report warning and fallback to standard `Optimizer`. -----*/
    if (G.sources().size() < 2 or
        not G.group_by().empty() or
        not G.aggregates().empty() or
        not G.order_by().empty() or
        G.limit().limit or
        G.limit().offset or
        std::any_of(G.joins().begin(), G.joins().end(), [](auto &join)
                    { return not join->condition().is_equi(); }) or
        std::any_of(G.projections().begin(), G.projections().end(), [](auto &p)
                    {
                        return not is<const ast::Designator>(p.first) or p.second.has_value(); // only designators without alias supported
                    }))
    {
        std::cerr << "WARNING: No compatible query for ResultDB `Optimizer`. Fallback to standard `Optimizer`."
                  << std::endl;

        std::unique_ptr<Producer> producer;
        Optimizer Opt(C.plan_enumerator(), C.cost_function());
        producer = Opt(G);
        return {std::move(producer), false};
    }

    /*----- Fold the query graph and compute semi-join reduction order. -----*/
    Optimizer_ResultDB_utils::combine_joins(G); // in case there are multiple joins between two specific data sources

    std::unique_ptr<Producer *[]> source_plans;
    std::vector<std::unique_ptr<DataModel>> base_models;

    if (Options::Get().optimize_result_db)
    {
        return Optimizer_ResultDB_utils::dp_resultdb(G);
    }

    if (G.is_cyclic())
    {
        source_plans = Optimizer_ResultDB_utils::solve_cycles_without_enum(G, base_models);
    }
    else
    {
        std::vector<Subproblem> folding_problems;
        source_plans = std::make_unique<Producer *[]>(G.num_sources());
        Optimizer_ResultDB_utils::optimize(G, folding_problems, source_plans, base_models);
    }

    /*----- Compute plans for data sources. -----*/
    const auto num_sources = G.sources().size();

    std::vector<semi_join_order_t> semi_join_reduction_order;
    auto semi_join_reduction_op = std::make_unique<SemiJoinReductionOperator>(std::move(G.projections()));
    /* Add source plans as children. */
    for (std::size_t i = 0; i < num_sources; ++i)
        semi_join_reduction_op->add_child(source_plans[i]);
    semi_join_reduction_order = Optimizer_ResultDB_utils::compute_semi_join_reduction_order(G, *semi_join_reduction_op);

    /* Construct a semi join reduction operator with all necessary information requried by the code generation. */
    semi_join_reduction_op->semi_join_reduction_order() = std::move(semi_join_reduction_order);
    semi_join_reduction_op->sources() = std::move(G.sources());
    semi_join_reduction_op->joins() = std::move(G.joins());

    return {std::move(semi_join_reduction_op), true};
}

/*======================================================================================================================
 * Optimizer
 *====================================================================================================================*/

std::pair<std::unique_ptr<Producer>, PlanTableEntry> Optimizer::optimize(QueryGraph &G) const
{
    switch (Options::Get().plan_table_type)
    {
    case Options::PT_auto:
    {
        /* Select most suitable type of plan table depending on the query graph structure.
         * Currently a simple heuristic based on the number of data sources.
         * TODO: Consider join edges too.  Eventually consider #CSGs. */
        if (G.num_sources() <= 15)
        {
            auto [plan, PT] = optimize_with_plantable<PlanTableSmallOrDense>(G);
            return {std::move(plan), std::move(PT.get_final())};
        }
        else
        {
            auto [plan, PT] = optimize_with_plantable<PlanTableLargeAndSparse>(G);
            return {std::move(plan), std::move(PT.get_final())};
        }
    }

    case Options::PT_SmallOrDense:
    {
        auto [plan, PT] = optimize_with_plantable<PlanTableSmallOrDense>(G);
        return {std::move(plan), std::move(PT.get_final())};
    }

    case Options::PT_LargeAndSparse:
    {
        auto [plan, PT] = optimize_with_plantable<PlanTableLargeAndSparse>(G);
        return {std::move(plan), std::move(PT.get_final())};
    }
    }
}

template <typename PlanTable>
std::pair<std::unique_ptr<Producer>, PlanTable> Optimizer::optimize_with_plantable(QueryGraph &G) const
{
    PlanTable PT(G);
    const auto num_sources = G.sources().size();
    auto &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

    if (num_sources == 0)
    {
        PT.get_final().cost = 0;                 // no sources → no cost
        PT.get_final().model = CE.empty_model(); // XXX: should rather be 1 (single tuple) than empty
        return {std::make_unique<ProjectionOperator>(G.projections()), std::move(PT)};
    }

    /*----- Initialize plan table and compute plans for data sources. -----*/
    auto source_plans = optimize_source_plans(G, PT);

    /*----- Compute join order and construct plan containing all joins. -----*/
    optimize_join_order(G, PT);
    std::unique_ptr<Producer> plan = construct_join_order(G, PT, source_plans);
    auto &entry = PT.get_final();

    /*----- Construct plan for remaining operations. -----*/
    if (Options::Get().decompose)
    {
        /* Add `DecomposeOperator` on top of plan. */
        if (not G.group_by().empty() or
            not G.aggregates().empty() or
            not G.order_by().empty() or
            G.limit().limit or
            G.limit().offset or
            std::any_of(G.joins().begin(), G.joins().end(), [](auto &join)
                        { return not join->condition().is_equi(); }) or
            std::any_of(G.projections().begin(), G.projections().end(), [](auto &p)
                        {
                            return not is<const ast::Designator>(p.first) or p.second.has_value(); // only designators without alias supported
                        }))
        {
            std::cerr << "WARNING: No compatible query to decompose. Fallback to standard `Optimizer`."
                      << std::endl;

            std::unique_ptr<Producer> producer;
            Optimizer Opt(C.plan_enumerator(), C.cost_function());
            producer = M_TIME_EXPR(Opt(G), "Compute the logical query plan", C.timer());
            return {std::move(producer), std::move(PT)};
        }
        auto decompose_op = std::make_unique<DecomposeOperator>(std::cout, std::move(G.projections()),
                                                                std::move(G.sources()));
        decompose_op->add_child(plan.release());
        plan = std::move(decompose_op);
    }
    else
    {
        plan = optimize_plan(G, std::move(plan), entry);
    }

    return {std::move(plan), std::move(PT)};
}

template <typename PlanTable>
std::unique_ptr<Producer *[]> Optimizer::optimize_source_plans(const QueryGraph &G, PlanTable &PT) const
{
    const auto num_sources = G.sources().size();
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    auto source_plans = std::make_unique<Producer *[]>(num_sources);
    std::vector<size_t> tuple_sizes;
    G.get_projection_sizes_of_subproblems(tuple_sizes);
    for (auto &ds : G.sources())
    {
        Subproblem s = Subproblem::Singleton(ds->id());
        if (auto bt = cast<BaseTable>(ds.get()))
        {
            /* Produce a scan for base tables. */
            PT[s].cost = 0;
            PT[s].model = CE.estimate_scan(G, s);
            PT[s].tuple_size = tuple_sizes[ds->id()];
            auto &store = bt->table().store();
            auto source = std::make_unique<ScanOperator>(store, bt->name().assert_not_none());

            /* Set operator information. */
            auto source_info = std::make_unique<OperatorInformation>();
            source_info->subproblem = s;
            source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
            source->info(std::move(source_info));

            source_plans[ds->id()] = source.release();
        }
        else
        {
            /* Recursively solve nested queries. */
            auto &Q = as<Query>(*ds);
            const bool old = std::exchange(needs_projection_, Q.alias().has_value()); // aliased nested queries need projection
            auto [sub_plan, sub] = optimize(Q.query_graph());
            needs_projection_ = old;

            /* If an alias for the nested query is given, prefix every attribute with the alias. */
            if (Q.alias().has_value())
            {
                M_insist(is<ProjectionOperator>(sub_plan), "only projection may rename attributes");
                Schema S;
                for (auto &e : sub_plan->schema())
                    S.add({Q.alias(), e.id.name}, e.type, e.constraints);
                sub_plan->schema() = S;
            }

            /* Update the plan table with the `DataModel` and cost of the nested query and save the plan in the array of
             * source plans. */
            PT[s].cost = sub.cost;
            sub.model->assign_to(s); // adapt model s.t. it describes the result of the current subproblem
            PT[s].model = std::move(sub.model);
            PT[s].tuple_size = tuple_sizes[ds->id()];
            source_plans[ds->id()] = sub_plan.release();
        }

        /* Apply filter, if any. */
        if (ds->filter().size())
        {
            /* Optimize the filter by splitting into smaller filters and ordering them. */
            std::vector<cnf::CNF> filters = Optimizer::optimize_filter(ds->filter());
            Producer *filtered_ds = source_plans[ds->id()];

            /* Construct a plan as a sequence of filters. */
            for (auto &&filter : filters)
            {
                /* Update data model with filter. */
                auto new_model = CE.estimate_filter(G, *PT[s].model, filter);
                PT[s].model = std::move(new_model);

                if (filter.size() == 1 and filter[0].size() > 1)
                { // disjunctive filter
                    auto tmp = std::make_unique<DisjunctiveFilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }
                else
                {
                    auto tmp = std::make_unique<FilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }

                /* Set operator information. */
                auto source_info = std::make_unique<OperatorInformation>();
                source_info->subproblem = s;
                source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model); // includes filters, if any
                filtered_ds->info(std::move(source_info));
            }

            source_plans[ds->id()] = filtered_ds;
        }
    }
    return source_plans;
}

template <typename PlanTable>
void Optimizer::optimize_join_order(const QueryGraph &G, PlanTable &PT) const
{
    Catalog &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

#ifndef NDEBUG
    if (Options::Get().statistics)
    {
        std::size_t num_CSGs = 0, num_CCPs = 0;
        const Subproblem All = Subproblem::All(G.num_sources());
        auto inc_CSGs = [&num_CSGs](Subproblem)
        { ++num_CSGs; };
        auto inc_CCPs = [&num_CCPs](Subproblem, Subproblem)
        { ++num_CCPs; };
        G.adjacency_matrix().for_each_CSG_undirected(All, inc_CSGs);
        G.adjacency_matrix().for_each_CSG_pair_undirected(All, inc_CCPs);
        std::cout << num_CSGs << " CSGs, " << num_CCPs << " CCPs" << std::endl;
    }
#endif

    M_TIME_EXPR(plan_enumerator()(G, cost_function(), PT), "Plan enumeration", C.timer());

    if (Options::Get().statistics)
    {
        std::cout << "Est. total cost: " << PT.get_final().cost
                  << "\nEst. result set size: " << CE.predict_cardinality(*PT.get_final().model)
                  << "\nPlan cost: " << PT[PT.get_final().left].cost + PT[PT.get_final().right].cost
                  << std::endl;
    }
}

template <typename PlanTable>
std::unique_ptr<Producer> Optimizer::construct_join_order(const QueryGraph &G, const PlanTable &PT,
                                                          const std::unique_ptr<Producer *[]> &source_plans) const
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    std::vector<std::reference_wrapper<Join>> joins;
    for (auto &J : G.joins())
        joins.emplace_back(*J);

    /* Use nested lambdas to implement recursive lambda using CPS. */
    const auto construct_recursive = [&](Subproblem s) -> Producer *
    {
        auto construct_plan_impl = [&](Subproblem s, auto &construct_plan_rec) -> Producer *
        {
            auto subproblems = PT[s].get_subproblems();
            if (subproblems.empty())
            {
                M_insist(s.size() == 1);
                return source_plans[*s.begin()];
            }
            else
            {
                /* Compute plan for each sub problem.  Must happen *before* calculating the join predicate. */
                std::vector<Producer *> sub_plans;
                for (auto sub : subproblems)
                    sub_plans.push_back(construct_plan_rec(sub, construct_plan_rec));

                /* Calculate the join predicate. */
                cnf::CNF join_condition;
                for (auto it = joins.begin(); it != joins.end();)
                {
                    Subproblem join_sources;
                    /* Compute subproblem of sources to join. */
                    for (auto ds : it->get().sources())
                        join_sources(ds.get().id()) = true;

                    if (join_sources.is_subset(s))
                    { // possible join
                        join_condition = join_condition and it->get().condition();
                        it = joins.erase(it);
                    }
                    else
                    {
                        ++it;
                    }
                }

                /* Construct the join. */
                auto join = std::make_unique<JoinOperator>(join_condition);
                for (auto sub_plan : sub_plans)
                    join->add_child(sub_plan);
                auto join_info = std::make_unique<OperatorInformation>();
                join_info->subproblem = s;
                join_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
                join->info(std::move(join_info));
                return join.release();
            }
        };
        return construct_plan_impl(s, construct_plan_impl);
    };

    return std::unique_ptr<Producer>(construct_recursive(Subproblem::All(G.num_sources())));
}

std::unique_ptr<Producer> Optimizer::optimize_plan(QueryGraph &G, std::unique_ptr<Producer> plan, PlanTableEntry &entry)
    const
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    /* Perform grouping. */
    if (not G.group_by().empty())
    {
        /* Compute `DataModel` after grouping. */
        auto new_model = CE.estimate_grouping(G, *entry.model, G.group_by()); // TODO provide aggregates
        entry.model = std::move(new_model);
        // TODO pick "best" algorithm
        auto group_by = std::make_unique<GroupingOperator>(G.group_by(), G.aggregates());
        group_by->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        group_by->info(std::move(info));
        plan = std::move(group_by);
    }
    else if (not G.aggregates().empty())
    {
        /* Compute `DataModel` after grouping. */
        auto new_model = CE.estimate_grouping(G, *entry.model, std::vector<GroupingOperator::group_type>());
        entry.model = std::move(new_model);
        auto agg = std::make_unique<AggregationOperator>(G.aggregates());
        agg->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        agg->info(std::move(info));
        plan = std::move(agg);
    }

    auto additional_projections = Optimizer::compute_projections_required_for_order_by(G.projections(), G.order_by());
    const bool requires_post_projection = not additional_projections.empty();

    /* Perform projection. */
    if (not additional_projections.empty() or not G.projections().empty())
    {
        /* Merge original projections with additional projections. */
        additional_projections.insert(additional_projections.end(), G.projections().begin(), G.projections().end());
        auto projection = std::make_unique<ProjectionOperator>(std::move(additional_projections));
        projection->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = projection->child(0)->info().estimated_cardinality;

        projection->info(std::move(info));
        plan = std::move(projection);
    }

    /* Perform ordering. */
    if (not G.order_by().empty())
    {
        // TODO estimate data model
        auto order_by = std::make_unique<SortingOperator>(G.order_by());
        order_by->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = order_by->child(0)->info().estimated_cardinality;

        order_by->info(std::move(info));
        plan = std::move(order_by);
    }

    /* Limit. */
    if (G.limit().limit or G.limit().offset)
    {
        /* Compute `DataModel` after limit. */
        auto new_model = CE.estimate_limit(G, *entry.model, G.limit().limit, G.limit().offset);
        entry.model = std::move(new_model);
        // TODO estimate data model
        auto limit = std::make_unique<LimitOperator>(G.limit().limit, G.limit().offset);
        limit->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        limit->info(std::move(info));
        plan = std::move(limit);
    }

    /* Perform post-ordering projection. */
    if (requires_post_projection or (not is<ProjectionOperator>(plan) and needs_projection_))
    {
        // TODO estimate data model
        /* Change aliased projections in designators with the alias as name since original projection is
         * performed beforehand. */
        std::vector<projection_type> adapted_projections;
        for (auto [expr, alias] : G.projections())
        {
            if (alias.has_value())
            {
                Token name(expr.get().tok.pos, alias.assert_not_none(), TK_IDENTIFIER);
                auto d = std::make_unique<const Designator>(Token::CreateArtificial(), Token::CreateArtificial(),
                                                            std::move(name), expr.get().type(), &expr.get());
                adapted_projections.emplace_back(*d, ThreadSafePooledOptionalString{});
                created_exprs_.emplace_back(std::move(d));
            }
            else
            {
                adapted_projections.emplace_back(expr, ThreadSafePooledOptionalString{});
            }
        }
        auto projection = std::make_unique<ProjectionOperator>(std::move(adapted_projections));
        projection->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = projection->child(0)->info().estimated_cardinality;

        projection->info(std::move(info));
        plan = std::move(projection);
    }
    return plan;
}

#define DEFINE(PLANTABLE) \
template \
std::pair<std::unique_ptr<Producer>, PLANTABLE> \
Optimizer::optimize_with_plantable(QueryGraph&) const; \
template \
std::unique_ptr<Producer*[]> \
Optimizer::optimize_source_plans(const QueryGraph&, PLANTABLE&) const; \
template \
void \
Optimizer::optimize_join_order(const QueryGraph&, PLANTABLE&) const;   \
template \
std::unique_ptr<Producer> \
Optimizer::construct_join_order(const QueryGraph&, const PLANTABLE&, const std::unique_ptr<Producer*[]>&) const; \
template \
std::unique_ptr<Producer*[]> Optimizer_ResultDB_utils::optimize_source_plans(const QueryGraph&, PLANTABLE&); \
template \
void \
Optimizer_ResultDB_utils::optimize_join_order(const QueryGraph&, PLANTABLE&, Subproblem);   \
template \
Producer* \
Optimizer_ResultDB_utils::construct_join_order(const QueryGraph&, const PLANTABLE&, Subproblem, std::unique_ptr<Producer*[]>&)
DEFINE(PlanTableSmallOrDense);
DEFINE(PlanTableLargeAndSparse);
#undef DEFINE

