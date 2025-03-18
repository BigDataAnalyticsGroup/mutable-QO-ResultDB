#pragma once

#include <cstdint>
#include <mutable/IR/QueryGraph.hpp>
#include <mutable/mutable-config.hpp>
#include <mutable/util/crtp.hpp>
#include <mutable/util/macro.hpp>
#include <mutable/util/MinCutAGaT.hpp>
#include <unordered_map>
#include <mutable/IR/PlanTable.hpp>


namespace m {

struct estimate_tag : const_virtual_crtp_helper<estimate_tag>::
                       returns<double>::
                       crtp_args<const PlanTableSmallOrDense&, const PlanTableLargeAndSparse&>::
                       args<SmallBitset, SmallBitset, const QueryGraph&, const AdjacencyMatrix&, const CardinalityEstimator&, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>&>  { };


struct PlanTableLargeAndSparse;
struct PlanTableEntry;
struct PlanTableSmallOrDense;
struct CardinalityEstimator;

/** An interface for all yannakakis heuristics. */
struct M_EXPORT YannakakisHeuristic : estimate_tag::base_type
{
    using Subproblem = SmallBitset;
    using estimate_tag::base_type::operator();


    YannakakisHeuristic() = default;

    virtual ~YannakakisHeuristic() = default;

    /** Estimate the costs of a pair of subproblems yielded for semi-join reductions. */
    template<typename PlanTable>
    double estimate(const QueryGraph &G,  const AdjacencyMatrix&M, const CardinalityEstimator &CE, const PlanTable &PT, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping, Subproblem left, Subproblem right) const {
        return operator()(estimate_tag{}, PT, left, right, G, M, CE, folded_mapping);
    }

    public:
    static double estimate_decompose_costs(const QueryGraph &G, Subproblem complete_problem, const PlanTableEntry& entry, const CardinalityEstimator &CE);
};

namespace {
    template<typename Actual>
    struct M_EXPORT YannakakisHeuristicCRTP
            : YannakakisHeuristic, estimate_tag::derived_type<Actual> {
    };
}


/**
* DummyEstimator that always returns the size of the cartesian product of the given subproblems
*/
struct M_EXPORT WeakCardinalityHeuristic : YannakakisHeuristicCRTP<WeakCardinalityHeuristic>
{
    template<typename PlanTable>
    WeakCardinalityHeuristic(const PlanTable &PT, Subproblem problem, const QueryGraph &G, const AdjacencyMatrix &M, const CardinalityEstimator &CE, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping);

    template<typename PlanTable>
    double operator()(estimate_tag, const PlanTable &PT, Subproblem left, Subproblem right, const QueryGraph &G, const AdjacencyMatrix&M, const CardinalityEstimator &CE, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping) const;

private:
    std::unordered_map<std::size_t, std::unique_ptr<DataModel>> models;
    std::vector<std::pair<std::size_t, std::size_t>> card_order;

    [[nodiscard]] static Subproblem get_folded_problem(const Subproblem problem, const std::unordered_map<Subproblem, Subproblem, SubproblemHash>& folded_mapping) {
        if (folded_mapping.empty()) return problem;
        return folded_mapping.at(problem);
    }

};



}


