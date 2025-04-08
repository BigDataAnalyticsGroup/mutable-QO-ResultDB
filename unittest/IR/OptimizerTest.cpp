#include "catch2/catch.hpp"
#include "mutable/Options.hpp"
#include <iostream>
#include <mutable/IR/Optimizer.hpp>
#include <mutable/catalog/Catalog.hpp>
#include <mutable/catalog/Type.hpp>
#include <mutable/IR/PlanTable.hpp>
#include <mutable/mutable.hpp>
#include <mutable/storage/Store.hpp>
#include <mutable/util/ADT.hpp>
#include <parse/Parser.hpp>
#include <parse/Sema.hpp>


using namespace m;

template<typename PlanTable>
void init_PT_base_case(const QueryGraph &G, PlanTable &PT)
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();
    using Subproblem = SmallBitset;
    for (auto &ds : G.sources()) {
        Subproblem s = Subproblem::Singleton(ds->id());
        auto bt = as<const BaseTable>(*ds);
        PT[s].cost = 0;
        PT[s].tuple_size = 10;
        PT[s].model = CE.estimate_scan(G, s);
    }
}

/*======================================================================================================================
 * Test Cost Function.
 *====================================================================================================================*/
TEST_CASE("Optimizer/ResultDB/Generic", "[IR]") {
    /* Get Catalog and create new database to use for unit testing. */
    Catalog::Clear();
    Catalog &Cat = Catalog::Get();
    auto &db = Cat.add_database(Cat.pool("db"));
    Cat.set_database_in_use(db);

    Diagnostic diag(false, std::cout, std::cerr);

    /* Create pooled strings. */
    ThreadSafePooledString str_A = Cat.pool("A");
    ThreadSafePooledString str_B = Cat.pool("B");
    ThreadSafePooledString str_C = Cat.pool("C");
    ThreadSafePooledString str_D = Cat.pool("D");
    ThreadSafePooledString str_E = Cat.pool("E");
    ThreadSafePooledString str_F = Cat.pool("F");
    ThreadSafePooledString str_G = Cat.pool("G");

    ThreadSafePooledString col_id = Cat.pool("id");
    ThreadSafePooledString col_aid = Cat.pool("aid");
    ThreadSafePooledString col_bid = Cat.pool("bid");
    ThreadSafePooledString col_cid = Cat.pool("cid");
    ThreadSafePooledString col_did = Cat.pool("did");
    ThreadSafePooledString col_eid = Cat.pool("eid");
    ThreadSafePooledString col_fid = Cat.pool("fid");
    ThreadSafePooledString col_gid = Cat.pool("gid");

    /* Create tables. */
    Table &tbl_A = db.add_table(str_A);
    Table &tbl_B = db.add_table(str_B);
    Table &tbl_C = db.add_table(str_C);
    Table &tbl_D = db.add_table(str_D);
    Table &tbl_E = db.add_table(str_E);
    Table &tbl_F = db.add_table(str_F);
    Table &tbl_G = db.add_table(str_G);

    /* Add columns to tables. */
    tbl_A.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_A.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_A.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));

    /* Add data to tables. */
    tbl_A.store(Cat.create_store(tbl_A));
    tbl_B.store(Cat.create_store(tbl_B));
    tbl_C.store(Cat.create_store(tbl_C));
    tbl_D.store(Cat.create_store(tbl_D));
    tbl_E.store(Cat.create_store(tbl_E));
    tbl_F.store(Cat.create_store(tbl_F));
    tbl_G.store(Cat.create_store(tbl_G));
    tbl_A.layout(Cat.data_layout());
    tbl_B.layout(Cat.data_layout());
    tbl_C.layout(Cat.data_layout());
    tbl_D.layout(Cat.data_layout());
    tbl_E.layout(Cat.data_layout());
    tbl_F.layout(Cat.data_layout());
    tbl_G.layout(Cat.data_layout());

    const Subproblem A(1);
    const Subproblem B(2);
    const Subproblem C(4);
    const Subproblem D(8);
    const Subproblem E(16);
    const Subproblem F(32);
    const Subproblem G(64);

    SECTION("acylic tree")
    {
        /* Define query:
         *
         *       A
         *      / \
         *     B   E
         *    / \ / \
         *    C D F G
         */
        const std::string query = "\
SELECT * \
FROM A, B, C, D, E, F, G \
WHERE A.bid = B.aid AND A.eid = E.aid AND B.cid = C.bid AND B.did = D.bid AND E.fid = F.eid AND E.gid = G.eid;";

        /* Setup semi-join cardinalities */
        for (std::size_t i = 0; i < 100; ++i) { tbl_A.store().append(); }
        for (std::size_t i = 0; i < 200; ++i) { tbl_B.store().append(); }
        for (std::size_t i = 0; i < 1000; ++i) { tbl_C.store().append(); }
        for (std::size_t i = 0; i < 300; ++i) { tbl_D.store().append(); }
        for (std::size_t i = 0; i < 10000; ++i) { tbl_E.store().append(); }
        for (std::size_t i = 0; i < 1500; ++i) { tbl_F.store().append(); }
        for (std::size_t i = 0; i < 500; ++i) { tbl_G.store().append(); }

        std::istringstream json_input;
        json_input.str("{ \"db\": [ \
                                {\"relations\": [\"A\"], \"size\":100, \"reductions\": [{ \"right_relations\": [\"B\", \"C\", \"D\"],  \"size\":50}, \
                                                                                    { \"right_relations\": [\"E\", \"F\", \"G\"],  \"size\":30}, \
                                                                                    { \"right_relations\": [\"B\", \"E\", \"C\", \"D\", \"F\", \"G\"],  \"size\":20}]}, \
                                {\"relations\": [\"B\"], \"size\":200, \"reductions\": [{ \"right_relations\": [\"A\", \"E\", \"F\", \"G\"],  \"size\":80}, \
                                                                                    { \"right_relations\": [\"C\"],  \"size\":120}, \
                                                                                    { \"right_relations\": [\"D\"],  \"size\":50}, \
                                                                                    { \"right_relations\": [\"A\", \"E\", \"F\", \"G\", \"C\"],  \"size\":75},\
                                                                                    { \"right_relations\": [\"A\", \"E\", \"F\", \"G\", \"D\"],  \"size\":45},\
                                                                                    { \"right_relations\": [\"C\", \"D\"],  \"size\":50},\
                                                                                    { \"right_relations\": [\"C\", \"D\", \"A\", \"E\", \"F\", \"G\"],  \"size\":30}]}, \
                                {\"relations\": [\"C\"], \"size\":1000, \"reductions\": [{ \"right_relations\": [\"B\", \"D\", \"A\", \"E\", \"F\", \"G\"],  \"size\":500}]}, \
                                {\"relations\": [\"D\"], \"size\":300, \"reductions\": [{ \"right_relations\": [\"B\", \"C\", \"A\", \"E\", \"F\", \"G\"],  \"size\":100}]}, \
                                {\"relations\": [\"E\"], \"size\":10000, \"reductions\": [{ \"right_relations\": [\"F\"],  \"size\":1000}, \
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\"],  \"size\":2500}, \
                                                                                    { \"right_relations\": [\"G\"],  \"size\":5000}, \
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"F\"],  \"size\":950},\
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"G\"],  \"size\":2000},\
                                                                                    { \"right_relations\": [\"F\", \"G\"],  \"size\":800},\
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"F\", \"G\"],  \"size\":750}]}, \
                                {\"relations\": [\"F\"], \"size\":1500, \"reductions\": [{ \"right_relations\": [\"B\", \"C\", \"D\", \"A\", \"E\", \"G\"],  \"size\":1200}]}, \
                                {\"relations\": [\"G\"], \"size\":500, \"reductions\": [{ \"right_relations\": [\"B\", \"C\", \"D\", \"A\", \"E\", \"F\"],  \"size\":500}]} \
                                ]}");

        auto stmt = m::statement_from_string(diag, query);
        REQUIRE(not diag.num_errors());
        auto query_graph = QueryGraph::Build(*stmt);
        auto &QG = *query_graph;

        std::unique_ptr<CardinalityEstimator> est = std::make_unique<InjectionCardinalityEstimator>(diag, Cat.pool("db"), json_input);

        auto A_model = est->estimate_scan(QG, A);
        auto B_model = est->estimate_scan(QG, B);
        auto C_model = est->estimate_scan(QG, C);
        auto D_model = est->estimate_scan(QG, D);
        auto E_model = est->estimate_scan(QG, E);
        auto F_model = est->estimate_scan(QG, F);
        auto G_model = est->estimate_scan(QG, G);

        db.cardinality_estimator(std::move(est));



        auto &ICE = db.cardinality_estimator();
        Cat.default_plan_enumerator(Cat.pool("DPccp"));

        SECTION("Cardinality orders")
        {

            std::vector<std::unique_ptr<DataModel>> base_models;

            base_models.emplace_back(std::move(A_model));
            base_models.emplace_back(std::move(B_model));
            base_models.emplace_back(std::move(C_model));
            base_models.emplace_back(std::move(D_model));
            base_models.emplace_back(std::move(E_model));
            base_models.emplace_back(std::move(F_model));
            base_models.emplace_back(std::move(G_model));

            /* Check correctness of cardinality orders */
            std::vector<std::size_t> card_orders[QG.num_sources()];

            std::vector<std::size_t> cardinality_order_A = {4, 1};
            std::vector<std::size_t> cardinality_order_B = {3, 0, 2};
            std::vector<std::size_t> cardinality_order_C = {1};
            std::vector<std::size_t> cardinality_order_D = {1};
            std::vector<std::size_t> cardinality_order_E = {5, 0, 6};
            std::vector<std::size_t> cardinality_order_F = {5};
            std::vector<std::size_t> cardinality_order_G = {5};


            auto tree_enumerator = TreeEnumerator(QG.num_sources());
            tree_enumerator.determine_reduced_models(QG, QG.adjacency_matrix(), ICE, card_orders, base_models);

            REQUIRE(std::equal(card_orders[0].begin(), card_orders[0].begin() + 1, cardinality_order_A.begin()));
            REQUIRE(std::equal(card_orders[1].begin(), card_orders[1].begin() + 2, cardinality_order_B.begin()));
            REQUIRE(std::equal(card_orders[2].begin(), card_orders[2].begin(), cardinality_order_C.begin()));
            REQUIRE(std::equal(card_orders[3].begin(), card_orders[3].begin(), cardinality_order_D.begin()));
            REQUIRE(std::equal(card_orders[4].begin(), card_orders[4].begin() + 2, cardinality_order_E.begin()));
            REQUIRE(std::equal(card_orders[5].begin(), card_orders[5].begin(), cardinality_order_F.begin()));
            REQUIRE(std::equal(card_orders[6].begin(), card_orders[6].begin(), cardinality_order_G.begin()));
        }

        SECTION("Check enumeration")
        {
            auto tree_enumerator_correct = TreeEnumerator(QG.num_sources());
            auto SJ = SemiJoinCostFunction();

            /* Initial models */
            auto A_red_model = ICE.estimate_full_reduction(QG, *A_model);
            auto B_red_model = ICE.estimate_full_reduction(QG, *B_model);
            auto C_red_model = ICE.estimate_full_reduction(QG, *C_model);
            auto D_red_model = ICE.estimate_full_reduction(QG, *D_model);
            auto E_red_model = ICE.estimate_full_reduction(QG, *E_model);
            auto F_red_model = ICE.estimate_full_reduction(QG, *F_model);
            auto G_red_model = ICE.estimate_full_reduction(QG, *G_model);

            /* Reduced models */
            auto BC_model = ICE.estimate_semi_join(QG, *B_model, *C_model, {});
            auto BD_model = ICE.estimate_semi_join(QG, *B_model, *D_model, {});
            auto BCD_model = ICE.estimate_semi_join(QG, *BC_model, *D_model, {});
            auto EF_model = ICE.estimate_semi_join(QG, *E_model, *F_model, {});
            auto EG_model = ICE.estimate_semi_join(QG, *E_model, *G_model, {});
            auto EFG_model = ICE.estimate_semi_join(QG, *EF_model, *G_model, {});
            auto AB_model = ICE.estimate_semi_join(QG, *A_model, *BCD_model, {});
            auto EA_model = ICE.estimate_semi_join(QG, *E_model, *AB_model, {});
            auto AE_model = ICE.estimate_semi_join(QG, *A_model, *EFG_model, {});
            auto ABE_model = ICE.estimate_semi_join(QG, *AB_model, *EFG_model, {});
            auto BCDA_model = ICE.estimate_semi_join(QG, *BCD_model, *AE_model, {});
            auto EFGA_model = ICE.estimate_semi_join(QG, *EFG_model, *AB_model, {});
            auto EFA_model = ICE.estimate_semi_join(QG, *EF_model, *AB_model, {});
            auto EGA_model = ICE.estimate_semi_join(QG, *EG_model, *AB_model, {});
            auto GE_model = ICE.estimate_semi_join(QG, *G_model, *EFA_model, {});
            auto FE_model = ICE.estimate_semi_join(QG, *F_model, *EGA_model, {});
            auto BDA_model = ICE.estimate_semi_join(QG, *BD_model, *AE_model, {});
            auto CB_model = ICE.estimate_semi_join(QG, *C_model, *BDA_model, {});
            auto BCA_model = ICE.estimate_semi_join(QG, *BC_model, *AE_model, {});
            auto DB_model = ICE.estimate_semi_join(QG, *D_model, *BCA_model, {});
            auto BA_model = ICE.estimate_semi_join(QG, *B_model, *AE_model, {});

            /* Basic costs */
            auto C_costs = 0;
            auto D_costs = 0;
            auto G_costs = 0;
            auto F_costs = 0;

            /* Recursive costs */
            auto BD_costs = SJ.estimate_semi_join_costs(ICE, *B_model, *D_model)
                                    + SJ.estimate_semi_join_costs(ICE, *D_model, *B_red_model);
            auto BCD_costs = BD_costs + SJ.estimate_semi_join_costs(ICE, *BD_model, *C_model)
                                    + SJ.estimate_semi_join_costs(ICE, *C_model, *B_red_model);
            auto EF_costs = SJ.estimate_semi_join_costs(ICE, *E_model, *F_model)
                                    + SJ.estimate_semi_join_costs(ICE, *F_model, *E_red_model);
            auto EFG_costs = EF_costs + SJ.estimate_semi_join_costs(ICE, *EF_model, *G_model)
                                    + SJ.estimate_semi_join_costs(ICE, *G_model, *E_red_model);
            auto AB_costs = BCD_costs + SJ.estimate_semi_join_costs(ICE, *A_model, *BCD_model)
                                    + SJ.estimate_semi_join_costs(ICE, *BCD_model, *A_red_model);
            auto AE_costs = EFG_costs + SJ.estimate_semi_join_costs(ICE, *A_model, *EFG_model)
                                    + SJ.estimate_semi_join_costs(ICE, *EFG_model, *A_red_model);
            auto ABE_costs = AE_costs + BCD_costs + SJ.estimate_semi_join_costs(ICE, *AE_model, *BCD_model)
                                    + SJ.estimate_semi_join_costs(ICE, *BCD_model, *A_red_model);
            auto BDA_costs = BD_costs + AE_costs + SJ.estimate_semi_join_costs(ICE, *BD_model, *AE_model)
                                    + SJ.estimate_semi_join_costs(ICE, *AE_model, *B_red_model);
            auto BCDA_costs = BDA_costs + SJ.estimate_semi_join_costs(ICE, *BDA_model, *C_model)
                                    + SJ.estimate_semi_join_costs(ICE, *C_model, *B_red_model);
            auto EFA_costs = EF_costs + AB_costs + SJ.estimate_semi_join_costs(ICE, *EF_model, *AB_model)
                                    + SJ.estimate_semi_join_costs(ICE, *AB_model, *E_red_model);
            auto EFGA_costs = EFA_costs + SJ.estimate_semi_join_costs(ICE, *EFA_model, *G_model)
                                    + SJ.estimate_semi_join_costs(ICE, *G_model, *E_red_model);
            auto GE_costs = EFA_costs + SJ.estimate_semi_join_costs(ICE, *G_model, *EFA_model)
                                    + SJ.estimate_semi_join_costs(ICE, *EFA_model, *G_red_model);
            auto EA_costs = AB_costs + SJ.estimate_semi_join_costs(ICE, *E_model, *AB_model)
                                    + SJ.estimate_semi_join_costs(ICE, *AB_model, *E_red_model);
            auto EAG_costs =  EA_costs + SJ.estimate_semi_join_costs(ICE, *EA_model, *G_model)
                                    + SJ.estimate_semi_join_costs(ICE, *G_model, *E_red_model);
            auto FE_costs = EAG_costs + SJ.estimate_semi_join_costs(ICE, *F_model, *EGA_model)
                                    + SJ.estimate_semi_join_costs(ICE, *EGA_model, *F_red_model);
            auto CB_costs = BDA_costs + SJ.estimate_semi_join_costs(ICE, *C_model, *BDA_model)
                                    + SJ.estimate_semi_join_costs(ICE, *BDA_model, *C_red_model);
            auto BA_Costs = AE_costs + SJ.estimate_semi_join_costs(ICE, *B_model, *AE_model)
                                    + SJ.estimate_semi_join_costs(ICE, *AE_model, *B_red_model);
            auto BAC_costs = BA_Costs + SJ.estimate_semi_join_costs(ICE, *BA_model, *C_model)
                                    + SJ.estimate_semi_join_costs(ICE, *C_model, *B_red_model);
            auto DB_costs = BAC_costs + SJ.estimate_semi_join_costs(ICE, *D_model, *BCA_model)
                            + SJ.estimate_semi_join_costs(ICE, *BCA_model, *D_red_model);


            std::vector<std::unique_ptr<DataModel>> base_models;

            base_models.emplace_back(std::move(A_model));
            base_models.emplace_back(std::move(B_model));
            base_models.emplace_back(std::move(C_model));
            base_models.emplace_back(std::move(D_model));
            base_models.emplace_back(std::move(E_model));
            base_models.emplace_back(std::move(F_model));
            base_models.emplace_back(std::move(G_model));

            /* Check correctness of cardinality orders */
            std::vector<std::size_t> card_orders[QG.num_sources()];


            auto tree_enumerator = TreeEnumerator(QG.num_sources());
            // auto best_root = tree_enumerator.find_best_root(QG, QG.adjacency_matrix(), ICE, SJ, card_orders, base_models);

            /*
            REQUIRE(tree_enumerator.parent_node_costs(1,3)->second == D_costs);
            REQUIRE(tree_enumerator.parent_node_costs(4,5)->second == F_costs);
            REQUIRE(tree_enumerator.parent_node_costs(4,6)->second == G_costs);
            REQUIRE(tree_enumerator.parent_node_costs(0,1)->second == BCD_costs);
            REQUIRE(tree_enumerator.parent_node_costs(0,4)->second == EFG_costs);
            REQUIRE(tree_enumerator.parent_node_costs(0,0)->second == ABE_costs);
            REQUIRE(tree_enumerator.parent_node_costs(4,0)->second == AB_costs);
            REQUIRE(tree_enumerator.parent_node_costs(5, 4)->second == EFA_costs);
            REQUIRE(tree_enumerator.parent_node_costs(6,6)->second == GE_costs);
            REQUIRE(tree_enumerator.parent_node_costs(5, 5)->second == FE_costs);
            REQUIRE(tree_enumerator.parent_node_costs(6, 4)->second == EAG_costs);
            REQUIRE(tree_enumerator.parent_node_costs(2, 2)->second == CB_costs);
            REQUIRE(tree_enumerator.parent_node_costs(3, 1)->second == BAC_costs);
            REQUIRE(tree_enumerator.parent_node_costs(3, 3)->second == DB_costs);
            REQUIRE(tree_enumerator.parent_node_costs(2, 1)->second == BDA_costs);
            REQUIRE(tree_enumerator.parent_node_costs(1, 1)->second == BCDA_costs);
            REQUIRE(tree_enumerator.parent_node_costs(4, 4)->second == EFGA_costs);
             */

            std::size_t correct_best_root = 0;
            auto costs = tree_enumerator.parent_node_costs(0,0)->second;
            for (std::size_t i = 1; i < QG.num_sources(); i++) {
                if (tree_enumerator.parent_node_costs(i,i)->second < costs) {
                    costs = tree_enumerator.parent_node_costs(i,i)->second;
                    correct_best_root = i;
                }
            }

            // REQUIRE(correct_best_root == best_root);
        }

        SECTION("Check final semi-join order")
        {

            std::vector<Optimizer_ResultDB::semi_join_order_t> semi_join_reduction_order_correct;

            semi_join_reduction_order_correct.emplace_back(QG[2], QG[4]);
            semi_join_reduction_order_correct.emplace_back(QG[4], QG[5]);
            semi_join_reduction_order_correct.emplace_back(QG[4], QG[6]);
            semi_join_reduction_order_correct.emplace_back(QG[0], QG[4]);
            semi_join_reduction_order_correct.emplace_back(QG[2], QG[0]);
            semi_join_reduction_order_correct.emplace_back(QG[2], QG[3]);

            std::vector<std::unique_ptr<DataModel>> base_models;

            base_models.emplace_back(std::move(A_model));
            base_models.emplace_back(std::move(B_model));
            base_models.emplace_back(std::move(C_model));
            base_models.emplace_back(std::move(D_model));
            base_models.emplace_back(std::move(E_model));
            base_models.emplace_back(std::move(F_model));
            base_models.emplace_back(std::move(G_model));

            /*            std::vector<Optimizer_ResultDB::semi_join_order_t> semi_join_reduction_order_actual =
                                Optimizer_ResultDB_utils::enumerate_semi_join_reduction_order(QG, ICE, base_models);

                        auto it_correct = semi_join_reduction_order_correct.begin();
                        auto it_actual = semi_join_reduction_order_actual.begin();

                        while(it_correct != semi_join_reduction_order_correct.end() && it_actual != semi_join_reduction_order_actual.end())
                        {
                            REQUIRE(it_correct->lhs == it_correct->lhs);
                            REQUIRE(it_correct->rhs == it_correct->rhs);
                            if(it_correct != semi_join_reduction_order_correct.end())
                            {
                                ++it_correct;
                            }
                            if(it_actual != semi_join_reduction_order_correct.end())
                            {
                                ++it_actual;
                            }
                        }*/


        }
        SECTION("Complete Run Acyclic")
        {
            Optimizer_ResultDB opt;
            auto ret_op = opt.operator()(QG);
            REQUIRE(ret_op.first != nullptr);
            REQUIRE(ret_op.second);
        }
        SECTION("cyclic")
    {
        /* Define query:
         *
         * A -- B \ / F
         * |  / |  E  |
         * C -- D / \ G
         */
        const std::string query = "\
        SELECT * \
        FROM A, B, C, D, E, F, G \
        WHERE A.bid = B.aid AND A.cid = C.aid AND B.did = D.bid AND C.did = D.cid AND B.eid = E.bid AND D.eid = E.did \
                                  AND E.fid = F.eid AND E.gid = G.eid AND G.fid = F.gid AND B.cid = C.bid;";

        /* Setup semi-join cardinalities */
        for (std::size_t i = 0; i < 100; ++i) { tbl_A.store().append(); }
        for (std::size_t i = 0; i < 200; ++i) { tbl_B.store().append(); }
        for (std::size_t i = 0; i < 1000; ++i) { tbl_C.store().append(); }
        for (std::size_t i = 0; i < 300; ++i) { tbl_D.store().append(); }
        for (std::size_t i = 0; i < 10000; ++i) { tbl_E.store().append(); }
        for (std::size_t i = 0; i < 1500; ++i) { tbl_F.store().append(); }
        for (std::size_t i = 0; i < 500; ++i) { tbl_G.store().append(); }

        std::istringstream json_input;
        json_input.str("{ \"db\": [ \
                                {\"relations\": [\"A\"], \"size\":100, \"reductions\": [{ \"right_relations\": [\"B\", \"C\", \"D\", \"E\", \"F\", \"G\"],  \"size\":20}]}, \
                                {\"relations\": [\"B\"], \"size\":200}, \
                                {\"relations\": [\"C\"], \"size\":1000}, \
                                {\"relations\": [\"D\"], \"size\":300}, \
                                {\"relations\": [\"E\"], \"size\":10000, \"reductions\": [{ \"right_relations\": [\"F\", \"G\"],  \"size\":500},\
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\"],  \"size\":800}, \
                                                                                    { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"F\", \"G\"],  \"size\":400}]}, \
                                {\"relations\": [\"F\"], \"size\":1500, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"E\", \"G\"],  \"size\":800}]}, \
                                {\"relations\": [\"G\"], \"size\":500, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"E\", \"F\"],  \"size\":250}]}, \
                                {\"relations\": [\"B\", \"D\"], \"size\":400}, \
                                {\"relations\": [\"B\", \"C\"], \"size\":2000}, \
                                {\"relations\": [\"C\", \"D\"], \"size\":3000}, \
                                {\"relations\": [\"F\", \"E\"], \"size\":6000, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\"],  \"size\":3000},\
                                                                                        { \"right_relations\": [\"G\"],  \"size\":2500},\
                                                                                        { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"G\"],  \"size\":2000}]}, \
                                {\"relations\": [\"F\", \"G\"], \"size\":5000, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"E\"],  \"size\":4000}]}, \
                                {\"relations\": [\"G\", \"E\"], \"size\":100, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\"],  \"size\":50},\
                                                                                        { \"right_relations\": [\"F\"],  \"size\":30},\
                                                                                        { \"right_relations\": [\"A\", \"B\", \"C\", \"D\", \"F\"],  \"size\":25}]}, \
                                {\"relations\": [\"B\", \"D\", \"C\"], \"size\":5000, \"reductions\": [{ \"right_relations\": [\"A\"],  \"size\":3000},\
                                                                                                { \"right_relations\": [\"E\", \"F\", \"G\"],  \"size\":4500},  \
                                                                                                { \"right_relations\": [\"A\", \"E\", \"F\", \"G\"],  \"size\":2700}]}, \
                                {\"relations\": [\"E\", \"F\", \"G\"], \"size\":10000, \"reductions\": [{ \"right_relations\": [\"A\", \"B\", \"C\", \"D\"],  \"size\":5000}]} \
                                ]}");
        auto stmt = m::statement_from_string(diag, query);
        REQUIRE(not diag.num_errors());
        auto query_graph = QueryGraph::Build(*stmt);
        auto &QG = *query_graph;

        std::unique_ptr<CardinalityEstimator> est = std::make_unique<InjectionCardinalityEstimator>(diag, Cat.pool("db"), json_input);

        db.cardinality_estimator(std::move(est));

        auto &ICE = db.cardinality_estimator();
        Cat.default_plan_enumerator(Cat.pool("DPccp"));

        SECTION("Complete Run Cyclic")
        {
            Optimizer_ResultDB opt;
            auto [fst, snd] = opt.operator()(QG);
            REQUIRE(fst != nullptr);
            REQUIRE(snd);
        }
    }



    }
}
TEST_CASE("Optimizer/ResultDB/Problems/1", "[IR]") {
    Catalog::Clear();
    Catalog &Cat = Catalog::Get();
    auto &db = Cat.add_database(Cat.pool("db"));
    Cat.set_database_in_use(db);
    Diagnostic diag(false, std::cout, std::cerr);

    /* Create pooled strings. */
    ThreadSafePooledString str_A = Cat.pool("A");
    ThreadSafePooledString str_B = Cat.pool("B");
    ThreadSafePooledString str_C = Cat.pool("C");
    ThreadSafePooledString str_D = Cat.pool("D");
    ThreadSafePooledString str_E = Cat.pool("E");
    ThreadSafePooledString str_F = Cat.pool("F");
    ThreadSafePooledString str_G = Cat.pool("G");
    ThreadSafePooledString str_H = Cat.pool("H");

    ThreadSafePooledString col_id = Cat.pool("id");
    ThreadSafePooledString col_aid = Cat.pool("aid");
    ThreadSafePooledString col_bid = Cat.pool("bid");
    ThreadSafePooledString col_cid = Cat.pool("cid");
    ThreadSafePooledString col_did = Cat.pool("did");
    ThreadSafePooledString col_eid = Cat.pool("eid");
    ThreadSafePooledString col_fid = Cat.pool("fid");
    ThreadSafePooledString col_gid = Cat.pool("gid");
    ThreadSafePooledString col_hid = Cat.pool("hid");

    /* Create tables. */
    Table &tbl_A = db.add_table(str_A);
    Table &tbl_B = db.add_table(str_B);
    Table &tbl_C = db.add_table(str_C);
    Table &tbl_D = db.add_table(str_D);
    Table &tbl_E = db.add_table(str_E);
    Table &tbl_F = db.add_table(str_F);
    Table &tbl_G = db.add_table(str_G);
    Table &tbl_H = db.add_table(str_H);

    /* Add columns to tables. */
    tbl_A.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_A.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_hid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_hid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_H.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_H.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));

    /* Add data to tables. */
    tbl_A.store(Cat.create_store(tbl_A));
    tbl_B.store(Cat.create_store(tbl_B));
    tbl_C.store(Cat.create_store(tbl_C));
    tbl_D.store(Cat.create_store(tbl_D));
    tbl_E.store(Cat.create_store(tbl_E));
    tbl_F.store(Cat.create_store(tbl_F));
    tbl_G.store(Cat.create_store(tbl_G));
    tbl_H.store(Cat.create_store(tbl_H));
    tbl_A.layout(Cat.data_layout());
    tbl_B.layout(Cat.data_layout());
    tbl_C.layout(Cat.data_layout());
    tbl_D.layout(Cat.data_layout());
    tbl_E.layout(Cat.data_layout());
    tbl_F.layout(Cat.data_layout());
    tbl_G.layout(Cat.data_layout());
    tbl_H.layout(Cat.data_layout());

    constexpr std::size_t num_rows_A = 10000000; // Avoid all joins with A at all costs!
    constexpr std::size_t num_rows_B = 100;
    constexpr std::size_t num_rows_C = 80;
    constexpr std::size_t num_rows_D = 120;
    constexpr std::size_t num_rows_E = 120;
    constexpr std::size_t num_rows_F = 240;
    constexpr std::size_t num_rows_G = 150;
    constexpr std::size_t num_rows_H = 360;
    for (std::size_t i = 0; i < num_rows_A; ++i) { tbl_A.store().append(); }
    for (std::size_t i = 0; i < num_rows_B; ++i) { tbl_B.store().append(); }
    for (std::size_t i = 0; i < num_rows_C; ++i) { tbl_C.store().append(); }
    for (std::size_t i = 0; i < num_rows_D; ++i) { tbl_D.store().append(); }
    for (std::size_t i = 0; i < num_rows_E; ++i) { tbl_E.store().append(); }
    for (std::size_t i = 0; i < num_rows_F; ++i) { tbl_F.store().append(); }
    for (std::size_t i = 0; i < num_rows_G; ++i) { tbl_G.store().append(); }
    for (std::size_t i = 0; i < num_rows_H; ++i) { tbl_H.store().append(); }


    SECTION("cycle") {
        /* Define query:
     *
     * A -- B -- C -- D
     * |    | \  |    |
     * E -- F -- G -- H
     */
        const std::string query = "\
    SELECT * \
    FROM A, B, C, D, E, F, G, H \
    WHERE A.bid = B.aid AND B.cid = C.bid AND C.did = D.cid AND D.hid = H.did AND A.eid = E.aid AND F.eid = G.fid \
                              AND B.fid = F.bid AND G.cid = C.gid AND H.gid = G.hid AND E.fid = F.eid AND B.gid=G.bid;";

    auto stmt = statement_from_string(diag, query);
    REQUIRE(not diag.num_errors());
    auto query_graph = QueryGraph::Build(*stmt);
    auto &QG = *query_graph;

    /* We first want to check whether blocks work correctly */
    std::vector<Subproblem> blocks;
    Subproblem cut_vertices;
    QG.adjacency_matrix().compute_blocks_and_cut_vertices(blocks, cut_vertices, Subproblem::All(QG.num_sources()), 3);

    Subproblem all = Subproblem::All(QG.num_sources());
    REQUIRE(blocks.size() == 1);
    REQUIRE(blocks[0] == all);
    REQUIRE(cut_vertices.empty());

    Optimizer_ResultDB_utils::bc_forest_t bc_forest = Optimizer_ResultDB_utils::build_bc_forest(blocks, cut_vertices);
    REQUIRE(bc_forest[all].empty());

    std::vector<Optimizer_ResultDB_utils::tree_problem_t> tree_problems = Optimizer_ResultDB_utils::create_tree_sets(bc_forest, blocks, Subproblem(0));
    REQUIRE(tree_problems.size() == 1);
    REQUIRE(tree_problems[0][0][0].first == all);
    REQUIRE(tree_problems[0][0][0].second == all);

    using PlanTable = PlanTableSmallOrDense;
    PlanTable plan_table(QG);
    init_PT_base_case(QG, plan_table);

    /* First, check whether TVCs can be determined greedily and exhaustive */
    std::unordered_map<Subproblem, Subproblem, SubproblemHash> folded_mapping;
    std::unordered_map<Subproblem, Optimizer_ResultDB_utils::folding_table_entry_t, SubproblemHash> folded_map;
        std::unordered_map<Subproblem, double, SubproblemHash> fold_costs;

    /* Exhaustive */
    std::vector<std::vector<Subproblem>> tvc_sets_exhaustive = Optimizer_ResultDB_utils::get_tvc_sets(QG.adjacency_matrix(), tree_problems[0][0][0]);
    REQUIRE(tvc_sets_exhaustive.size() == 7);
    REQUIRE(tvc_sets_exhaustive[0][0] == Subproblem(34));
    REQUIRE(tvc_sets_exhaustive[1][0] == Subproblem(66));
    REQUIRE(tvc_sets_exhaustive[2][0] == Subproblem(98));
    REQUIRE(tvc_sets_exhaustive[3][0] == Subproblem(68));
    REQUIRE(tvc_sets_exhaustive[4][0] == Subproblem(34));
    REQUIRE(tvc_sets_exhaustive[4][1] == Subproblem(68));
    REQUIRE(tvc_sets_exhaustive[5][0] == Subproblem(70));
    REQUIRE(tvc_sets_exhaustive[6][0] == Subproblem(102));

    /* Greedy */
    std::vector<Subproblem> greedy_folds;
    Optimizer_ResultDB_utils::find_greedy_vertex_cuts(QG.adjacency_matrix(), tree_problems[0][0][0], greedy_folds);
    REQUIRE(greedy_folds.size() == 2);
    REQUIRE(greedy_folds[0] == Subproblem(34));
    REQUIRE(greedy_folds[1] == Subproblem(68));

    /* Try folding some example graphs, and test whether this works well. Also utilize recursive models. */
    AdjacencyMatrix new_matrix(QG.adjacency_matrix());
    Optimizer_ResultDB_utils::create_folded_adjacency_matrix(greedy_folds, QG.adjacency_matrix(), new_matrix, folded_mapping);

    auto check_greedy_folding = [&](AdjacencyMatrix& matrix) {
        /* The smallest node from each fold is always chosen as the anchor node */
        REQUIRE(matrix[0] == Subproblem(18));
        REQUIRE(matrix[1] == Subproblem(21));
        REQUIRE(matrix[2] == Subproblem(138));
        REQUIRE(matrix[3] == Subproblem(132));
        REQUIRE(matrix[4] == Subproblem(3));
        REQUIRE(matrix[5] == Subproblem(0));
        REQUIRE(matrix[6] == Subproblem(0));
        REQUIRE(matrix[7] == Subproblem(12));

        /* Check whether the folded mapping is correct */
        REQUIRE(folded_mapping[Subproblem(1)] == Subproblem(1));
        REQUIRE(folded_mapping[Subproblem(2)] == Subproblem(34));
        REQUIRE(folded_mapping[Subproblem(4)] == Subproblem(68));
        REQUIRE(folded_mapping[Subproblem(8)] == Subproblem(8));
        REQUIRE(folded_mapping[Subproblem(16)] == Subproblem(16));
        REQUIRE(folded_mapping[Subproblem(128)] == Subproblem(128));
    };
    check_greedy_folding(new_matrix);

    /* Check whether the same result will happen when using the complete greedy approach */
    AdjacencyMatrix greedy_new_matrix(QG.adjacency_matrix());
    folded_mapping = {};

    Optimizer_ResultDB_utils::get_greedy_folded_graph(QG.adjacency_matrix(), greedy_new_matrix, tree_problems[0][0][0], folded_mapping);
    check_greedy_folding(greedy_new_matrix);

    folded_mapping = {};
    Optimizer_ResultDB_utils::folding_table_entry_t result = Optimizer_ResultDB_utils::enumerate_block_problem(QG, QG.adjacency_matrix(), folded_mapping, folded_map, tree_problems[0][0][0], fold_costs, plan_table, true);
    REQUIRE(result->first.size() == 4);
    REQUIRE(result->first[0] == Subproblem(1));
    REQUIRE(result->first[1] == Subproblem(50));
    REQUIRE(result->first[2] == Subproblem(68));
    REQUIRE(result->first[3] == Subproblem(136));

    /* Now perform a full check to verify the correctness of the entire stack, greedy */
    Optimizer_ResultDB_utils::dp_resultdb_with_plantable<PlanTableSmallOrDense>(QG);
    Options::Get().result_db_optimizer = Options::DP_ResultDB_Exhaustive;
        stmt = statement_from_string(diag, query);
        REQUIRE(not diag.num_errors());
        query_graph = QueryGraph::Build(*stmt);
        auto &QG2 = *query_graph;
        /* Now perform a full check to verify the correctness of the entire stack, greedy */
        Optimizer_ResultDB_utils::dp_resultdb_with_plantable<PlanTableSmallOrDense>(QG2);
    }
    SECTION("chain") {
        /* Define query:
*
* A -- B -- C -- D
* |
* E -- F -- G -- H
*/
        const std::string query = "\
    SELECT * \
    FROM A, B, C, D, E, F, G, H \
    WHERE A.bid = B.aid AND B.cid = C.bid AND C.did = D.cid AND A.eid = E.aid AND F.eid = G.fid \
                                AND H.gid = G.hid AND E.fid=F.eid;";

        auto stmt = statement_from_string(diag, query);
        REQUIRE(not diag.num_errors());
        auto query_graph = QueryGraph::Build(*stmt);
        auto &QG = *query_graph;

        /* Full Stack evaluation */
        Optimizer_ResultDB_utils::dp_resultdb_with_plantable<PlanTableSmallOrDense>(QG);
    }

}

TEST_CASE("Optimizer/ResultDB/Problems/2", "[IR]") {
    Catalog::Clear();
    Catalog &Cat = Catalog::Get();
    auto &db = Cat.add_database(Cat.pool("db"));
    Cat.set_database_in_use(db);
    Diagnostic diag(false, std::cout, std::cerr);

    /* Create pooled strings. */
    ThreadSafePooledString str_A = Cat.pool("A");
    ThreadSafePooledString str_B = Cat.pool("B");
    ThreadSafePooledString str_C = Cat.pool("C");
    ThreadSafePooledString str_D = Cat.pool("D");
    ThreadSafePooledString str_E = Cat.pool("E");
    ThreadSafePooledString str_F = Cat.pool("F");
    ThreadSafePooledString str_G = Cat.pool("G");
    ThreadSafePooledString str_H = Cat.pool("H");
    ThreadSafePooledString str_I = Cat.pool("I");
    ThreadSafePooledString str_J = Cat.pool("J");

    ThreadSafePooledString col_id = Cat.pool("id");
    ThreadSafePooledString col_aid = Cat.pool("aid");
    ThreadSafePooledString col_bid = Cat.pool("bid");
    ThreadSafePooledString col_cid = Cat.pool("cid");
    ThreadSafePooledString col_did = Cat.pool("did");
    ThreadSafePooledString col_eid = Cat.pool("eid");
    ThreadSafePooledString col_fid = Cat.pool("fid");
    ThreadSafePooledString col_gid = Cat.pool("gid");
    ThreadSafePooledString col_hid = Cat.pool("hid");
    ThreadSafePooledString col_iid = Cat.pool("iid");
    ThreadSafePooledString col_jid = Cat.pool("jid");

    /* Create tables. */
    Table &tbl_A = db.add_table(str_A);
    Table &tbl_B = db.add_table(str_B);
    Table &tbl_C = db.add_table(str_C);
    Table &tbl_D = db.add_table(str_D);
    Table &tbl_E = db.add_table(str_E);
    Table &tbl_F = db.add_table(str_F);
    Table &tbl_G = db.add_table(str_G);
    Table &tbl_H = db.add_table(str_H);
    Table &tbl_I = db.add_table(str_I);
    Table &tbl_J = db.add_table(str_J);

    /* Add columns to tables. */
    tbl_A.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_A.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_B.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_hid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_C.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_iid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_D.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_E.push_back(col_jid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_aid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_F.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_fid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_bid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_G.push_back(col_hid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_H.push_back(col_gid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_H.push_back(col_cid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_H.push_back(col_iid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_I.push_back(col_hid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_I.push_back(col_did, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_I.push_back(col_jid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_J.push_back(col_eid, Type::Get_Integer(Type::TY_Vector, 4));
    tbl_J.push_back(col_iid, Type::Get_Integer(Type::TY_Vector, 4));

    /* Add data to tables. */
    tbl_A.store(Cat.create_store(tbl_A));
    tbl_B.store(Cat.create_store(tbl_B));
    tbl_C.store(Cat.create_store(tbl_C));
    tbl_D.store(Cat.create_store(tbl_D));
    tbl_E.store(Cat.create_store(tbl_E));
    tbl_F.store(Cat.create_store(tbl_F));
    tbl_G.store(Cat.create_store(tbl_G));
    tbl_H.store(Cat.create_store(tbl_H));
    tbl_I.store(Cat.create_store(tbl_I));
    tbl_J.store(Cat.create_store(tbl_J));
    tbl_A.layout(Cat.data_layout());
    tbl_B.layout(Cat.data_layout());
    tbl_C.layout(Cat.data_layout());
    tbl_D.layout(Cat.data_layout());
    tbl_E.layout(Cat.data_layout());
    tbl_F.layout(Cat.data_layout());
    tbl_G.layout(Cat.data_layout());
    tbl_H.layout(Cat.data_layout());
    tbl_I.layout(Cat.data_layout());
    tbl_J.layout(Cat.data_layout());

    constexpr std::size_t num_rows_A = 100000; // Avoid all joins with A at all costs!
    constexpr std::size_t num_rows_B = 100;
    constexpr std::size_t num_rows_C = 80;
    constexpr std::size_t num_rows_D = 120;
    constexpr std::size_t num_rows_E = 120;
    constexpr std::size_t num_rows_F = 240;
    constexpr std::size_t num_rows_G = 150;
    constexpr std::size_t num_rows_H = 360;
    constexpr std::size_t num_rows_I = 120;
    constexpr std::size_t num_rows_J = 20;
    for (std::size_t i = 0; i < num_rows_A; ++i) { tbl_A.store().append(); }
    for (std::size_t i = 0; i < num_rows_B; ++i) { tbl_B.store().append(); }
    for (std::size_t i = 0; i < num_rows_C; ++i) { tbl_C.store().append(); }
    for (std::size_t i = 0; i < num_rows_D; ++i) { tbl_D.store().append(); }
    for (std::size_t i = 0; i < num_rows_E; ++i) { tbl_E.store().append(); }
    for (std::size_t i = 0; i < num_rows_F; ++i) { tbl_F.store().append(); }
    for (std::size_t i = 0; i < num_rows_G; ++i) { tbl_G.store().append(); }
    for (std::size_t i = 0; i < num_rows_H; ++i) { tbl_H.store().append(); }
    for (std::size_t i = 0; i < num_rows_I; ++i) { tbl_I.store().append(); }
    for (std::size_t i = 0; i < num_rows_J; ++i) { tbl_J.store().append(); }
    SECTION("Check normal") {
        /* Define query:
*
* A -- B -- C -- D -- E
* |    |    |    |    |
* F -- G -- H -- I -- J
*/
        const std::string query = "\
    SELECT * \
    FROM A, B, C, D, E, F, G, H, I, J \
    WHERE A.bid = B.aid AND B.cid = C.bid AND C.did = D.cid AND D.eid = E.did AND A.fid = F.aid AND F.gid = G.fid AND G.hid = H.gid \
                              AND H.iid = I.hid AND I.jid = J.iid AND B.gid = G.bid AND C.hid = H.cid AND D.iid=I.did AND E.jid = J.eid;";

        auto stmt = statement_from_string(diag, query);
        REQUIRE(not diag.num_errors());
        auto query_graph = QueryGraph::Build(*stmt);
        auto &QG = *query_graph;

        /* Now perform a full check to verify the correctness of the entire stack, greedy */
        Optimizer_ResultDB_utils::dp_resultdb_with_plantable<PlanTableSmallOrDense>(QG);
    }
}
