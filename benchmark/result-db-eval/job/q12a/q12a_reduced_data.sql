\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code = '[us]') TO 'benchmark/result-db-eval/job/q12a/data/12a_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM company_type AS ct  WHERE ct.kind = 'production companies') TO 'benchmark/result-db-eval/job/q12a/data/12a_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it1  WHERE it1.info = 'genres') TO 'benchmark/result-db-eval/job/q12a/data/12a_it1.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it2  WHERE it2.info = 'rating') TO 'benchmark/result-db-eval/job/q12a/data/12a_it2.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc ) TO 'benchmark/result-db-eval/job/q12a/data/12a_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Drama' OR mi.info = 'Horror')) TO 'benchmark/result-db-eval/job/q12a/data/12a_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx  WHERE mi_idx.info > '8.0') TO 'benchmark/result-db-eval/job/q12a/data/12a_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year >= 2005 AND t.production_year <= 2008) TO 'benchmark/result-db-eval/job/q12a/data/12a_t.csv' CSV;
