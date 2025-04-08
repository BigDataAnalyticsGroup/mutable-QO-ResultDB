\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code !='[pl]' AND (cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')) TO 'benchmark/result-db-eval/job/q21a/data/21a_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM company_type AS ct  WHERE ct.kind ='production companies') TO 'benchmark/result-db-eval/job/q21a/data/21a_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE k.keyword ='sequel') TO 'benchmark/result-db-eval/job/q21a/data/21a_k.csv' CSV;
\copy (SELECT DISTINCT * FROM link_type AS lt  WHERE lt.link LIKE '%follow%') TO 'benchmark/result-db-eval/job/q21a/data/21a_lt.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc  WHERE mc.note IS NULL) TO 'benchmark/result-db-eval/job/q21a/data/21a_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German')) TO 'benchmark/result-db-eval/job/q21a/data/21a_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q21a/data/21a_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_link AS ml ) TO 'benchmark/result-db-eval/job/q21a/data/21a_ml.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year >= 1950 AND t.production_year <= 2000) TO 'benchmark/result-db-eval/job/q21a/data/21a_t.csv' CSV;
