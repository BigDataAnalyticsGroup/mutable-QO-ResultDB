import re


if __name__ == "__main__":
    with open("./benchmark/result-db-eval/ce/schema_postgres.sql", "r") as exist:
        with open("./benchmark/result-db-eval/ce/schema_mutable_t.sql", "w") as mutable_file:
            with open("./benchmark/result-db-eval/ce/setup_postgres.sh", "w") as postgres_init:
                mutable_file.write("CREATE DATABASE result_db;\nUSE result_db;\n\n\n")
                content = exist.read()
                pattern = r"create\s+table\s+(\w+)"
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    mutable_file.write(f"CREATE TABLE {match} (s INT(4) NOT NULL, d INT(4) NOT NULL);\n")
                    postgres_init.write(f"psql -U ${{USER}} -d ${{DB_NAME}} -c \"\copy {match} FROM '$(pwd)/benchmark/result-db-eval/ce/data/{match}_original.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\\\"', ESCAPE '\\\\')\";\n")



