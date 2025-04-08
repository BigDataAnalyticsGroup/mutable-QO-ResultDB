import argparse
import re
import os
import shutil
import csv
import networkx as nx
import matplotlib.pyplot as plt


from query_utility import JoinGraph
import query_definitions as q_def
import subprocess

def parse_schema(file: str) -> dict[str, dict[str, str]]:
    with open(file, "r") as schema_file:
        mutable_schema: dict[str, dict[str, str]] = dict()  # maps relation to dict (mapping column_name to datatype)
        schema = schema_file.read()
        matches = re.finditer(r"CREATE TABLE (\w+) \((.*?)\);", schema, re.DOTALL)
        for match in matches:
            table_name = match.group(1)
            attributes = match.group(2)
            attr_dict: dict[str, str] = dict()  # maps column_name to datatype
            for attr in attributes.split(","):
                attr = attr.strip()
                if not attr:
                    continue
                attr_name, attr_type = attr.split(maxsplit=1)
                attr_type = re.sub(r"INT\(\d+\)", "INT", attr_type)
                attr_type = re.sub(r"CHAR\((\d+)\)", r"CHAR \1", attr_type)
                attr_dict[attr_name] = attr_type
            mutable_schema[table_name] = attr_dict
        return mutable_schema
def create_benchmark_file(query: str, schema: dict[str, dict[str, str]], config) -> None:
    join_graph: JoinGraph = getattr(q_def, f"create_q{query}")() # execute the function `create_<query>` of module `q_def`
    # edges = []
    # for join in join_graph.joins:
    #     edges.append((join.left_relation.alias, join.right_relation.alias))
    # G = nx.Graph()
    # G.add_edges_from(edges)
    # assert len(G.nodes) == len(join_graph.relations), "RIP"
    #
    # # Draw the graph
    # plt.figure(figsize=(10, 10))
    # nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    # plt.show()
    # return
    data = '\n'
    used_rels = set()
    for rel in join_graph.relations:
        if rel.name in used_rels:
            continue
        data += f"\t'{rel.name}':\n"
        data += f"\t\tfile: 'benchmark/result-db-eval/ce/data/{rel.name}.csv'\n"
        data += f"\t\tformat: 'csv'\n"
        data += f"\t\tdelimiter: ','\n"
        data += f"\t\theader: 0\n"
        data += f"\t\tattributes:\n"
        for attr, datatype in schema[rel.name].items():
            data += f"\t\t\t'{attr}': '{datatype}'\n"
        data = data.replace('\t', '    ')
        used_rels.add(rel.name)

    with open(f"./benchmark/result-db-eval/ce/cycle-queries/dblp_cyclic_q{query}.sql", 'r') as mutable_file:
        mutable_query = mutable_file.read()
        mutable_query = mutable_query.replace('\t', "").replace("select", "SELECT").replace("from", "FROM").replace("where", "WHERE").replace("and", "AND")
    for rel in join_graph.relations:
        mutable_query = mutable_query.replace(f" {rel.name} {rel.alias}",f" {rel.name} AS {rel.alias}")
    benchmark = f"""description: CE q{query}.
suite: ce
benchmark: ce
name: q{query}
readonly: true
chart:
    x:
        scale: linear
        type: O
        label: JOB Queries
    y:
        scale: linear
        type: Q
        label: 'Execution time [ms]'
    # Defaults: scale is "linear", type is "Q", label is "X" or "Y"
data:{data}

systems:
    mutable:
        args: >-
          --backend WasmV8
          --no-simd
          --cardinality-estimator Injected
          --use-cardinality-file benchmark/result-db-eval/ce/q{query}_injected_cardinalities.json
          --plan-enumerator DPccp
        configurations:                                   # Different experiment configurations.
            'WasmV8, ResultDB_SemiJoin':
                args: --result-db
                pattern: '^Process the query:.*'
            'WasmV8, ResultDB_Decompose':
                args: --decompose
                pattern: '^Process the query:.*'
            'WasmV8, TD_Fold':
                args: --result-db --optimize-result-db --td_root
                pattern: '^Process the query:.*'
            'WasmV8, TD_Fold_NoTVC':
                args: --result-db --optimize-result-db --td_root --ignore_tvcs
                pattern: '^Process the query:.*'
            'WasmV8, TD_RESULTDB':
                args: --result-db --optimize-result-db --td_resultdb
                pattern: '^Process the query:.*'
        cases:
            0: \'{mutable_query}\'
"""
    with open(f"./benchmark/result-db-eval/ce/q{query}_benchmark.yml", 'w') as benchmark_file:
        benchmark_file.write(benchmark)

if __name__ == "__main__":
    # Command Line Arguments
    parser = argparse.ArgumentParser(
        prog="Create mutable benchmark files for JOB queries",
        description="""Script to create mutable benchmark files.""",
    )

    parser.add_argument("-q", "--queries", default=["ce"], nargs="+", type=str)
    parser.add_argument("-u", "--user", required=True)

    args = parser.parse_args()
    config = vars(args)

    queries = [
        "8_1",
        "8_2", "8_3",
        "8_4", "8_5", "8_6", "8_7", "8_8", "8_9", "8_10", "8_11", "8_12"
    ]
    mutable_schema = parse_schema( "./benchmark/result-db-eval/ce/schema_mutable_t.sql" )
    for query in queries:
        create_benchmark_file(query, mutable_schema, config)
