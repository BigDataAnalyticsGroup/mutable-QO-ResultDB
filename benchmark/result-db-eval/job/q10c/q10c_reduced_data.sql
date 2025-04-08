\copy (SELECT DISTINCT * FROM char_name AS chn ) TO 'benchmark/result-db-eval/job/q10c/data/10c_chn.csv' CSV;
\copy (SELECT DISTINCT * FROM cast_info AS ci  WHERE ci.note LIKE '%(producer)%') TO 'benchmark/result-db-eval/job/q10c/data/10c_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code = '[us]') TO 'benchmark/result-db-eval/job/q10c/data/10c_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM company_type AS ct ) TO 'benchmark/result-db-eval/job/q10c/data/10c_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc ) TO 'benchmark/result-db-eval/job/q10c/data/10c_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM role_type AS rt ) TO 'benchmark/result-db-eval/job/q10c/data/10c_rt.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 1990) TO 'benchmark/result-db-eval/job/q10c/data/10c_t.csv' CSV;
