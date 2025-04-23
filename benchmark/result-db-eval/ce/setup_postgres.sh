#!/usr/bin/env bash

if [ $# -eq 0 ]
then
    echo "Supply PostgreSQL username."
    exit 1
fi

USER=$1
DB_NAME="ce"

# Drop and create database
psql -U ${USER} -d postgres -c "DROP DATABASE IF EXISTS "${DB_NAME}
psql -U ${USER} -d postgres -c "CREATE DATABASE "${DB_NAME}

# Create tables
psql -U ${USER} -d ${DB_NAME} -f "$(pwd)/benchmark/result-db-eval/ce/schema_postgres.sql"

psql -U ${USER} -d ${DB_NAME} -c "\copy dblp1 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp1.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp2 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp2.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp3 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp3.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp4 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp4.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp5 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp5.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp6 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp6.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp7 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp7.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp8 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp8.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp9 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp9.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp10 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp10.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp11 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp11.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp12 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp12.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp13 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp13.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp14 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp14.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp15 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp15.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp16 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp16.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp17 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp17.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp18 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp18.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp19 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp19.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp20 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp20.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp21 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp21.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp22 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp22.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp23 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp23.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp24 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp24.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp25 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp25.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp26 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp26.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";
psql -U ${USER} -d ${DB_NAME} -c "\copy dblp27 FROM '$(pwd)/benchmark/result-db-eval/ce/data/dblp27.csv' WITH (FORMAT csv, DELIMITER ',', QUOTE '\"', ESCAPE '\\')";