import argparse
import re


from query_utility import JoinGraph
import job_mutable_query_definitions as q_def

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

def create_benchmark_file(query: str, schema: dict[str, dict[str, str]]) -> None:
    join_graph: JoinGraph = getattr(q_def, f"create_q{query}")() # execute the function `create_<query>` of module `q_def`
    # edges = []
    # for join in join_graph.joins:
    #     edges.append((join.left_relation.alias, join.right_relation.alias))
    # G = nx.Graph()
    # G.add_edges_from(edges)
    # assert len(G.nodes) == len(join_graph.relations), "RIP"

    # Draw the graph
    # plt.figure(figsize=(10, 10))
    # nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    # plt.show()
    relation_names = [r.name for r in join_graph.relations]
    data = '\n'
    for r in relation_names:
        data += f"\t'{r}':\n"
        data += f"\t\tfile: 'benchmark/job/data/{r}.csv'\n"
        data += f"\t\tformat: 'csv'\n"
        data += f"\t\tdelimiter: ','\n"
        data += f"\t\theader: 0\n"
        data += f"\t\tattributes:\n"
        for attr, datatype in schema[r].items():
            data += f"\t\t\t'{attr}': '{datatype}'\n"
        data = data.replace('\t', '    ')

    with open(f"./benchmark/job/mutable/{query}.sql", 'r') as mutable_file:
        mutable_query = mutable_file.read().split("\n\n")[1] # split at "\n\n" to remove import statements
        mutable_query = " ".join(mutable_query.splitlines()).strip() # convert to single line to ensure correct formatting
        mutable_query = mutable_query.replace('\t', "")
    benchmark = f"""description: Join-Order Benchmark q{query}.
suite: result-db
benchmark: job
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
          --use-cardinality-file benchmark/result-db-eval/job/q{query}_cardinalities.json
          --plan-enumerator DPccp
        configurations:                                   # Different experiment configurations.
            'WasmV8, ResultDB_SemiJoin':
                args: --result-db
                pattern: '^Execute machine code:.*'
            'WasmV8, ResultDB_Decompose':
                args: --decompose
                pattern: '^Execute machine code:.*'
            'WasmV8, TD_RESULTDB':
                args: '--result-db --optimize-result-db --dp_resultdb'
                pattern: '^Execute machine code:.*'
        cases:
            0: \'{mutable_query}\'
"""
    with open(f"./benchmark/result-db-eval/job/q{query}_benchmark.yml", 'w') as benchmark_file:
        benchmark_file.write(benchmark)

if __name__ == "__main__":
    # Command Line Arguments
    parser = argparse.ArgumentParser(
        prog="Create mutable benchmark files for JOB queries",
        description="""Script to create mutable benchmark files.""",
    )

    parser.add_argument("-q", "--queries", default=["imdb"], nargs="+", type=str)

    args = parser.parse_args()
    config = vars(args)

    job_queries = [
        "1b",
        "2a",
        "3c",
        "4a",
        "5c",
        "7a",
        "8a",
        "9c",
        "10c",
        "11c",
        "12a",
        "14a",
        "15d",
        "18c",
        "19a",
        "21a",
        "22c",
        "23a",
        "24a",
        "25b",
        "26a",
        "27a",
        "28c",
        "30c",
        "31a",
        "33c",
    ]

    if "imdb" in config["queries"]:  # use all JOB queries
        assert len(config["queries"]) == 1, "list of queries may only contain 'imdb' or actual queries"
        config["queries"] = job_queries
    else:
        assert set(config["queries"]).issubset(job_queries), print(config["queries"])
    mutable_schema = parse_schema( "./benchmark/result-db-eval/job/schema_mutable_reduced.sql" )
    for query in job_queries:
        create_benchmark_file(query, mutable_schema)
