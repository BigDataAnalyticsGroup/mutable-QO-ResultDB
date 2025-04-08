\copy (SELECT DISTINCT * FROM cast_info AS ci  WHERE (ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')) TO 'benchmark/result-db-eval/job/q18c/data/18c_ci.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it1  WHERE it1.info = 'genres') TO 'benchmark/result-db-eval/job/q18c/data/18c_it1.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it2  WHERE it2.info = 'votes') TO 'benchmark/result-db-eval/job/q18c/data/18c_it2.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info AS mi  WHERE (mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')) TO 'benchmark/result-db-eval/job/q18c/data/18c_mi.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx ) TO 'benchmark/result-db-eval/job/q18c/data/18c_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM name AS n  WHERE n.gender = 'm') TO 'benchmark/result-db-eval/job/q18c/data/18c_n.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t ) TO 'benchmark/result-db-eval/job/q18c/data/18c_t.csv' CSV;
