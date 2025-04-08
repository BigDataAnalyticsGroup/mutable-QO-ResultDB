\copy (SELECT DISTINCT * FROM aka_name AS an ) TO 'benchmark/result-db-eval/job/q9c/data/9c_an.csv' CSV;
\copy (SELECT DISTINCT * FROM char_name AS chn ) TO 'benchmark/result-db-eval/job/q9c/data/9c_chn.csv' CSV;
\copy (SELECT DISTINCT * FROM cast_info AS ci  WHERE (ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')) TO 'benchmark/result-db-eval/job/q9c/data/9c_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code ='[us]') TO 'benchmark/result-db-eval/job/q9c/data/9c_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc ) TO 'benchmark/result-db-eval/job/q9c/data/9c_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM name AS n  WHERE n.gender ='f' AND n.name LIKE '%An%') TO 'benchmark/result-db-eval/job/q9c/data/9c_n.csv' CSV;
\copy (SELECT DISTINCT * FROM role_type AS rt  WHERE rt.role ='actress') TO 'benchmark/result-db-eval/job/q9c/data/9c_rt.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t ) TO 'benchmark/result-db-eval/job/q9c/data/9c_t.csv' CSV;
