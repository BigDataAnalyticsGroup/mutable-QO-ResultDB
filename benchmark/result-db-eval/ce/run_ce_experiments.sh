#!/usr/bin/env bash

ce_benchmarks=(
    "8_1"
    "8_2"
    "8_3"
    "8_4"
    "8_5"
    "8_6"
    "8_7"
    "8_8"
    "8_9"
    "8_10"
    "8_11"
)

for query in "${ce_benchmarks[@]}"; do
    python ./benchmark/Benchmark.py --output ./benchmark/result-db-eval/ce/recreated_results.csv ./benchmark/result-db-eval/ce/q${query}_benchmark.yml
done
