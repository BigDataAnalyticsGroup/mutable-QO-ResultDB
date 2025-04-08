import os
import random
import subprocess

if __name__ == "__main__":
    for root, dirs, files in os.walk("./benchmark/result-db-eval/ce/data/"):
        for file in files:
            if "original" not in file:
                continue
            path = os.path.join(root, file)
            with open(path, "r") as f_in:
                with open(path.replace("_original", ""), "w") as f_out:
                    counter = 0
                    for line in f_in:
                        if counter < 100000:
                            f_out.write(line)
                        else:
                            coinflip = random.randint(1, 2)
                            if coinflip <= 1:
                                f_out.write(line)
                        counter += 1
