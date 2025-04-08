\copy (SELECT DISTINCT * FROM aka_title AS at ) TO 'benchmark/result-db-eval/job/q15d/data/15d_at.csv' CSV;
\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code = '[us]') TO 'benchmark/result-db-eval/job/q15d/data/15d_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM company_type AS ct ) TO 'benchmark/result-db-eval/job/q15d/data/15d_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it1  WHERE it1.info = 'release dates') TO 'benchmark/result-db-eval/job/q15d/data/15d_it1.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k ) TO 'benchmark/result-db-eval/job/q15d/data/15d_k.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc ) TO 'benchmark/result-db-eval/job/q15d/data/15d_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE mi.note LIKE '%internet%') TO 'benchmark/result-db-eval/job/q15d/data/15d_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q15d/data/15d_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 1990) TO 'benchmark/result-db-eval/job/q15d/data/15d_t.csv' CSV;
