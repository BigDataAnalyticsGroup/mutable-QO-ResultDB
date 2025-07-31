import argparse
import re
import os
import shutil
import csv


from query_utility import JoinGraph
import job_acyclic_mutable_query_definitions as q_def
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

def create_reduced_data(query_name: str, config: dict[str, str]) -> None:
    import job_acyclic_postgres_query_definitions as q_def
    join_graph = getattr(q_def, f"create_q{query_name}")()
    file_content = ""
    filename = f"benchmark/result-db-eval/job/q{query_name}/q{query_name}_reduced_data.sql"
    output_dir = f"benchmark/result-db-eval/job/q{query_name}/data"
    for relation in join_graph.relations:
        query = relation.get_query_for_reduced_relation()
        reduced_relation_filename = f'{query_name}_{relation.alias}.csv'
        file_content += f"\copy ({query}) TO '{output_dir}/{reduced_relation_filename}' CSV;\n"
    with open(filename, 'w') as file:
        file.write(file_content)
    command = f"psql -U {config['user']} -d imdb -f {filename}"
    print(subprocess.run(command, capture_output=True, text=True, shell=True))
    for relation in join_graph.relations:
        with open(f"{output_dir}/{query_name}_{relation.alias}.csv", "r", encoding="utf-8") as f:
            content = f.read().replace('""', r'\"')

        with open(f"{output_dir}/{query_name}_{relation.alias}.csv", "w", encoding="utf-8") as f:
            f.write(content)




def create_benchmark_file(query: str, schema: dict[str, dict[str, str]], config) -> None:
    join_graph: JoinGraph = getattr(q_def, f"create_q{query}")() # execute the function `create_<query>` of module `q_def`
    create_reduced_data(query, config)
    return
    data = '\n'
    for rel in join_graph.relations:
        data += f"\t'{rel.alias}':\n"
        data += f"\t\tfile: 'benchmark/result-db-eval/job/q{query}/data/{query}_{rel.alias}.csv'\n"
        data += f"\t\tformat: 'csv'\n"
        data += f"\t\tdelimiter: ','\n"
        data += f"\t\theader: 0\n"
        data += f"\t\tattributes:\n"
        for attr, datatype in schema[rel.name].items():
            data += f"\t\t\t'{attr}': '{datatype}'\n"
        data = data.replace('\t', '    ')

    with open(f"./benchmark/job/mutable-cyclic/{query}.sql", 'r') as mutable_file:
        mutable_query = mutable_file.read().split("\n\n")[1] # split at "\n\n" to remove import statements
        mutable_query = " ".join(mutable_query.splitlines()).strip() # convert to single line to ensure correct formatting
        mutable_query = mutable_query.replace('\t', "")
    for rel in join_graph.relations:
        mutable_query = mutable_query.replace(f" {rel.name} AS",f" {rel.alias} AS")
        for fil in rel.filters:
            assert fil in mutable_query, f"{fil} not in \n{mutable_query} for \n{query}"
            mutable_query = mutable_query.replace(f'{fil} AND ', "")
    benchmark = f"""description: Join-Order Benchmark q{query}.
suite: job
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
          --use-cardinality-file benchmark/result-db-eval/job/q{query}/q{query}_cyclic_injected_cardinalities.json
          --plan-enumerator DPccp
        configurations:                                   # Different experiment configurations.
          'ResultDB_SemiJoin':
            args: >-
              --result-db
            pattern:
              Execution Time: '^Execute machine code:.*'
          'TD_Fold':
            args: >-
              --result-db
              --optimize-result-db
              --td_root
            pattern:
              Execution Time: '^Execute machine code:.*'
          'TD_Fold_NoTVC':
            args: >-
              --result-db
              --optimize-result-db
              --td_root
              --ignore_tvcs
            pattern:
              Execution Time: '^Execute machine code:.*'
          'TD_ResultDB':
            args: >-
              --result-db
              --optimize-result-db
            pattern:
              Execution Time: '^Execute machine code:.*'
          'ResultDB_Decompose':
            args: >-
              --decompose
            pattern:
              Execution Time: '^Execute machine code:.*'
          'GHD_Heuristic':
            args: >-
              --result-db
              --optimize-result-db
              --ghd_heuristic
            pattern:
              Execution Time: '^Execute machine code:.*'
          'GHD_C_Fold':
            args: >-
              --result-db
              --optimize-result-db
              --ghd_c_fold
            pattern:
              Execution Time: '^Execute machine code:.*'
        cases:
            0: \'{mutable_query}\'
"""
    with open(f"./benchmark/result-db-eval/job/q{query}/q{query}_cyclic_benchmark.yml", 'w') as benchmark_file:
        benchmark_file.write(benchmark)

if __name__ == "__main__":
    # Command Line Arguments
    parser = argparse.ArgumentParser(
        prog="Create mutable benchmark files for JOB queries",
        description="""Script to create mutable benchmark files.""",
    )

    parser.add_argument("-q", "--queries", default=["imdb"], nargs="+", type=str)
    parser.add_argument("-u", "--user", required=True)

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
    for query in job_queries:
        query_folder_path = f"./benchmark/result-db-eval/job/q{query}/data"
        if not os.path.exists(query_folder_path):
            os.makedirs(query_folder_path)

    if "imdb" in config["queries"]:  # use all JOB queries
        assert len(config["queries"]) == 1, "list of queries may only contain 'imdb' or actual queries"
        config["queries"] = job_queries
    else:
        assert set(config["queries"]).issubset(job_queries), print(config["queries"])
    mutable_schema = parse_schema( "./benchmark/result-db-eval/job/schema_mutable_reduced.sql" )
    for query in job_queries:
        create_reduced_data(query, config)
        # create_benchmark_file(query, mutable_schema, config)
    #create_benchmark_file("1b", mutable_schema, config)
