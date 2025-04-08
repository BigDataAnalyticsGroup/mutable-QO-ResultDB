\copy (SELECT DISTINCT * FROM info_type AS it1  WHERE it1.info = 'countries') TO 'benchmark/result-db-eval/job/q14a/data/14a_it1.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it2  WHERE it2.info = 'rating') TO 'benchmark/result-db-eval/job/q14a/data/14a_it2.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE (k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')) TO 'benchmark/result-db-eval/job/q14a/data/14a_k.csv' CSV;
\copy (SELECT DISTINCT * FROM kind_type AS kt  WHERE kt.kind = 'movie') TO 'benchmark/result-db-eval/job/q14a/data/14a_kt.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')) TO 'benchmark/result-db-eval/job/q14a/data/14a_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx  WHERE mi_idx.info < '8.5') TO 'benchmark/result-db-eval/job/q14a/data/14a_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q14a/data/14a_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 2010) TO 'benchmark/result-db-eval/job/q14a/data/14a_t.csv' CSV;
