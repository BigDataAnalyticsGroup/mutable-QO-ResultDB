\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code !='[pl]' AND (cn.name LIKE '20th Century Fox%' OR cn.name LIKE 'Twentieth Century Fox%')) TO 'benchmark/result-db-eval/job/q11c/data/11c_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM company_type AS ct  WHERE ct.kind != 'production companies' AND ct.kind IS NOT NULL) TO 'benchmark/result-db-eval/job/q11c/data/11c_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE (k.keyword = 'sequel' OR k.keyword = 'revenge' OR k.keyword = 'based-on-novel')) TO 'benchmark/result-db-eval/job/q11c/data/11c_k.csv' CSV;
\copy (SELECT DISTINCT * FROM link_type AS lt ) TO 'benchmark/result-db-eval/job/q11c/data/11c_lt.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc  WHERE mc.note IS NOT NULL) TO 'benchmark/result-db-eval/job/q11c/data/11c_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q11c/data/11c_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_link AS ml ) TO 'benchmark/result-db-eval/job/q11c/data/11c_ml.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 1950) TO 'benchmark/result-db-eval/job/q11c/data/11c_t.csv' CSV;
