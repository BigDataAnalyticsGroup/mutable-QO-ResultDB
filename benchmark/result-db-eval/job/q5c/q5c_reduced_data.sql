\copy (SELECT DISTINCT * FROM company_type AS ct  WHERE ct.kind = 'production companies') TO 'benchmark/result-db-eval/job/q5c/data/5c_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it ) TO 'benchmark/result-db-eval/job/q5c/data/5c_it.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc  WHERE NOT mc.note LIKE '%(TV)%' AND mc.note LIKE '%(USA)%') TO 'benchmark/result-db-eval/job/q5c/data/5c_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')) TO 'benchmark/result-db-eval/job/q5c/data/5c_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 1990) TO 'benchmark/result-db-eval/job/q5c/data/5c_t.csv' CSV;
