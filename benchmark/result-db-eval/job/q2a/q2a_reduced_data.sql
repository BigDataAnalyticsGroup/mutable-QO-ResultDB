\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code ='[de]') TO 'benchmark/result-db-eval/job/q2a/data/2a_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE k.keyword ='character-name-in-title') TO 'benchmark/result-db-eval/job/q2a/data/2a_k.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc ) TO 'benchmark/result-db-eval/job/q2a/data/2a_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q2a/data/2a_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t ) TO 'benchmark/result-db-eval/job/q2a/data/2a_t.csv' CSV;
