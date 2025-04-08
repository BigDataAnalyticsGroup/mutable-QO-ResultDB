\copy (SELECT DISTINCT * FROM aka_name AS an1 ) TO 'benchmark/result-db-eval/job/q8a/data/8a_an1.csv' CSV;
\copy (SELECT DISTINCT * FROM cast_info AS ci  WHERE ci.note ='(voice: English version)') TO 'benchmark/result-db-eval/job/q8a/data/8a_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM company_name AS cn  WHERE cn.country_code ='[jp]') TO 'benchmark/result-db-eval/job/q8a/data/8a_cn.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc  WHERE mc.note LIKE '%(Japan)%' AND NOT mc.note LIKE '%(USA)%') TO 'benchmark/result-db-eval/job/q8a/data/8a_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM name AS n1  WHERE n1.name LIKE '%Yo%' AND NOT n1.name LIKE '%Yu%') TO 'benchmark/result-db-eval/job/q8a/data/8a_n1.csv' CSV;
\copy (SELECT DISTINCT * FROM role_type AS rt  WHERE rt.role ='actress') TO 'benchmark/result-db-eval/job/q8a/data/8a_rt.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t ) TO 'benchmark/result-db-eval/job/q8a/data/8a_t.csv' CSV;
