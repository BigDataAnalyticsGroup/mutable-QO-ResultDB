#include <mutable/catalog/YannakakisHeuristic.hpp>
#include <mutable/IR/PlanTable.hpp>
#include <mutable/catalog/CardinalityEstimator.hpp>
#include <mutable/util/ADT.hpp>


using namespace m;


double YannakakisHeuristic::estimate_decompose_costs(const QueryGraph &G, const Subproblem complete_problem, const PlanTableEntry& entry, const CardinalityEstimator &CE)
{
    // Single Problems do not have to be decomposed
    if (complete_problem.size() == 1) return 0;
    const auto model = CE.estimate_full_reduction(G, *entry.model);
    return 40 * static_cast<double>(CE.predict_cardinality(*model)) * static_cast<double>(entry.tuple_size);
}

/*======================================================================================================================
 * WeakCardinalityHeuristic
 *====================================================================================================================*/

template<typename PlanTable>
WeakCardinalityHeuristic::WeakCardinalityHeuristic(const PlanTable &PT, const Subproblem problem, const QueryGraph &G, const AdjacencyMatrix &M, const CardinalityEstimator &CE, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping) {
    const auto all = Subproblem::Singleton(G.num_sources());
    auto found = Subproblem(0);
    for (auto neighbor: M.neighbors(problem)) {

        /* Get problems reachable from neighbors */
        auto original_reachable = Subproblem(0);
        auto neighbor_problem = Subproblem::Singleton(neighbor);

        /* Do not check neighbors belonging to the same block multiple times */
        if (!(found & neighbor_problem).empty()) continue;
        for (const auto node_id: M.reachable(neighbor_problem, all, problem) - neighbor_problem) {
            const auto original_singleton = get_folded_problem(Subproblem::Singleton(node_id), folded_mapping);
            original_reachable |= original_singleton;
        }
        found |= original_reachable;

        /* Get model and add its reduction to list of neighbors */
        auto neighbor_model = CE.copy(*PT[neighbor_problem].model);
        auto reduced_neighbor_model = CE.estimate_reduction(G, *neighbor_model, original_reachable);
        auto original_problem = get_folded_problem(problem, folded_mapping);
        card_order.emplace_back(neighbor, CE.predict_cardinality(*CE.estimate_semi_join(G, *PT[original_problem].model, *reduced_neighbor_model, {}
        )));
        models.emplace(neighbor, std::move(reduced_neighbor_model));
    }
    auto cmp = [](const std::pair<std::size_t, std::size_t> &a, const std::pair<std::size_t, std::size_t> &b){
        return a.second < b.second;
    };
    std::sort(card_order.begin(), card_order.end(), cmp);
}

template<typename PlanTable>
double
WeakCardinalityHeuristic::operator()(estimate_tag, const PlanTable &PT, const Subproblem left, const Subproblem right, const QueryGraph &G, const AdjacencyMatrix&M, const CardinalityEstimator &CE, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping) const
{
    auto main_problem = get_folded_problem(left, folded_mapping);
    if (right.empty()) {
        const auto main_neighbors = M.neighbors(left);

        /* With no neighbors, there is nothing to do! */
        if (main_neighbors.empty()) {
            return 0;
        }
        auto main_model = CE.copy(*PT[main_problem].model);
        double reduction_costs = 0;

        /* Traverse all neighbors */
        for (const auto& [neighbor, _] : card_order) {
            if (not (Subproblem::Singleton(neighbor) & main_neighbors)) continue;
            reduction_costs += CE.predict_cardinality(*main_model);
            main_model = CE.estimate_semi_join(G, *main_model, *models.find(neighbor)->second, {});
        }

        /* Final hash function */
        return reduction_costs;
    }
    const auto main_neighbors = M.neighbors(left) - right;

    /* If no neighbors are present, you can simply use the reduction from the neighbor */
    auto main_model = CE.copy(*PT[main_problem].model);
    if (main_neighbors.empty()) {
        return static_cast<double>(CE.predict_cardinality(*main_model));
    }

    /* Model of other fold, must be reduced for more accurate results */
    auto other_problem = get_folded_problem(right, folded_mapping);
    auto other_model = CE.copy(*PT[other_problem].model);
    for (auto other_neighbor: M.neighbors(right) - left) {
        other_model = CE.estimate_semi_join(G, *other_model, *models.find(other_neighbor)->second, {});
    }

    auto other_card = CE.predict_cardinality(*CE.estimate_semi_join(G, *main_model, *other_model, {}));
    double costs = 0;
    for (auto [neighbor, card] : card_order) {
        if (not (Subproblem::Singleton(neighbor) & main_neighbors)) continue;
        costs += CE.predict_cardinality(*main_model);
        if (other_card < card) {
            main_model = CE.estimate_semi_join(G, *main_model, *other_model, {});
            other_card = std::numeric_limits<std::size_t>::max();
        } else {
            main_model = CE.estimate_semi_join(G, *main_model, *models.find(neighbor)->second, {});
        }
    }
    return costs;
}

template
double
WeakCardinalityHeuristic::operator()(estimate_tag, const PlanTableSmallOrDense&, Subproblem, Subproblem, const QueryGraph&,  const AdjacencyMatrix&, const CardinalityEstimator&, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>&) const;
template
double
WeakCardinalityHeuristic::operator()(estimate_tag, const PlanTableLargeAndSparse&, Subproblem, Subproblem, const QueryGraph&,  const AdjacencyMatrix&, const CardinalityEstimator&, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>&) const;

template
WeakCardinalityHeuristic::WeakCardinalityHeuristic(const PlanTableSmallOrDense&, Subproblem, const QueryGraph&, const AdjacencyMatrix&, const CardinalityEstimator&, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>&);

template
WeakCardinalityHeuristic::WeakCardinalityHeuristic(const PlanTableLargeAndSparse&, Subproblem, const QueryGraph&, const AdjacencyMatrix&, const CardinalityEstimator&, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>&);
