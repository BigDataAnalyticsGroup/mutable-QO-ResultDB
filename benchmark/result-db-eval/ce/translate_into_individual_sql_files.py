import os


if __name__ == "__main__":
    for root, dirs, files in os.walk("./benchmark/result-db-eval/ce/queries/"):
        for file in files:
            file_path = os.path.join(root, file)
            # Ignore acyclic queries
            if "acyclic" in file_path:
                continue
            with open(file_path, "r") as query_file:
                curr = 0
                for line in query_file:
                    if "select count(*)" in line:
                        curr += 1
                        with open(f"./benchmark/result-db-eval/ce/cycle-queries/{file.replace('.sql', '')}_{curr}.sql", "w") as new_file:
                           new_file.write(line.replace("count(*)", "*"))


