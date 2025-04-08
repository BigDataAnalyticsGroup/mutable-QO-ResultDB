\copy (SELECT DISTINCT * FROM aka_name AS an  WHERE an.name LIKE '%a%') TO 'benchmark/result-db-eval/job/q7a/data/7a_an.csv' CSV;
\copy (SELECT DISTINCT * FROM cast_info AS ci ) TO 'benchmark/result-db-eval/job/q7a/data/7a_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it  WHERE it.info = 'mini biography') TO 'benchmark/result-db-eval/job/q7a/data/7a_it.csv' CSV;
\copy (SELECT DISTINCT * FROM link_type AS lt  WHERE lt.link = 'features') TO 'benchmark/result-db-eval/job/q7a/data/7a_lt.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_link AS ml ) TO 'benchmark/result-db-eval/job/q7a/data/7a_ml.csv' CSV;
\copy (SELECT DISTINCT * FROM name AS n  WHERE n.name_pcode_cf >= 'A' AND n.name_pcode_cf <= 'F' AND (n.gender='m' OR (n.gender = 'f' AND n.name LIKE 'B%'))) TO 'benchmark/result-db-eval/job/q7a/data/7a_n.csv' CSV;
\copy (SELECT DISTINCT * FROM person_info AS pi  WHERE pi.note = 'Volker Boehm') TO 'benchmark/result-db-eval/job/q7a/data/7a_pi.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year >= 1980 AND t.production_year <= 1995) TO 'benchmark/result-db-eval/job/q7a/data/7a_t.csv' CSV;
