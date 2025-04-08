\copy (SELECT DISTINCT * FROM info_type AS it  WHERE it.info ='rating') TO 'benchmark/result-db-eval/job/q4a/data/4a_it.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE k.keyword LIKE '%sequel%') TO 'benchmark/result-db-eval/job/q4a/data/4a_k.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx  WHERE mi_idx.info > '5.0') TO 'benchmark/result-db-eval/job/q4a/data/4a_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q4a/data/4a_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 2005) TO 'benchmark/result-db-eval/job/q4a/data/4a_t.csv' CSV;
