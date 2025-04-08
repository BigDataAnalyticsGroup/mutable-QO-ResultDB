\copy (SELECT DISTINCT * FROM cast_info AS ci  WHERE (ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')) TO 'benchmark/result-db-eval/job/q25b/data/25b_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it1  WHERE it1.info = 'genres') TO 'benchmark/result-db-eval/job/q25b/data/25b_it1.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it2  WHERE it2.info = 'votes') TO 'benchmark/result-db-eval/job/q25b/data/25b_it2.csv' CSV;
\copy (SELECT DISTINCT * FROM keyword AS k  WHERE (k.keyword = 'murder' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity')) TO 'benchmark/result-db-eval/job/q25b/data/25b_k.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE mi.info = 'Horror') TO 'benchmark/result-db-eval/job/q25b/data/25b_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx ) TO 'benchmark/result-db-eval/job/q25b/data/25b_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_keyword AS mk ) TO 'benchmark/result-db-eval/job/q25b/data/25b_mk.csv' CSV;
\copy (SELECT DISTINCT * FROM name AS n  WHERE n.gender = 'm') TO 'benchmark/result-db-eval/job/q25b/data/25b_n.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year > 2010 AND t.title LIKE 'Vampire%') TO 'benchmark/result-db-eval/job/q25b/data/25b_t.csv' CSV;
