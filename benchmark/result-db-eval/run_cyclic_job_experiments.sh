#!/usr/bin/env bash

job_benchmarks=(
    "q1b"
    "q2a"
    "q3c"
    "q4a"
    "q5c"
    "q7a"
    "q8a"
    "q9c"
    "q10c"
    "q11c"
    "q12a"
    "q14a"
    "q15d"
    "q18c"
    "q19a"
    "q21a"
    "q22c"
    "q23a"
    "q24a"
    "q25b"
    "q26a"
    "q27a"
    "q28c"
    "q30c"
    "q31a"
    "q33c"
)

for query in "${job_benchmarks[@]}"; do
    python ./benchmark/Benchmark.py --output ./benchmark/result-db-eval/job/recreated_results/cyclic_results.csv ./benchmark/result-db-eval/job/${query}/${query}_cyclic_benchmark.yml
done
