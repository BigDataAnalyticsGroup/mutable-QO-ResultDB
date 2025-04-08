\copy (SELECT DISTINCT * FROM keyword AS k  WHERE k.keyword LIKE '%sequel%') TO 'benchmark/result-db-eval/job/q3c/data/3c_k.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')) TO 'benchmark/result-db-eval/job/q3c/data/3c_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q3c/data/3c_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 1990) TO 'benchmark/result-db-eval/job/q3c/data/3c_t.csv' CSV;
