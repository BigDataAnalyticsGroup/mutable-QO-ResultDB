#!/bin/bash

# Define path to DuckDB CLI
DUCKDB=duckdb_cli

{ ${DUCKDB} | grep 'Run Time' | cut -d ' ' -f 4 | awk '{print $1 * 1000;}'; } << EOF
CREATE TABLE Attributes_multi_i32 ( id INT, a0 INT, a1 INT, a2 INT, a3 INT );
COPY Attributes_multi_i32 FROM 'benchmark/operators/data/Attributes_multi_i32.csv' ( HEADER );
.timer on
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 < -2147483647 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 < -1932735283 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 < -1717986918 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 < -1288490188 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  -858993459 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  -429496729 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <           0 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <   429496729 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <   858993459 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  1288490188 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  1717986918 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  1932735283 AND a1 < -2104533975;
SELECT COUNT(*) FROM Attributes_multi_i32 WHERE a0 <  2104533975 AND a1 < -2104533975;
EOF
