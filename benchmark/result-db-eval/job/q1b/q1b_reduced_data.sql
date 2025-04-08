\copy (SELECT DISTINCT * FROM company_type AS ct  WHERE ct.kind = 'production companies') TO 'benchmark/result-db-eval/job/q1b/data/1b_ct.csv' CSV;
\copy (SELECT DISTINCT * FROM info_type AS it  WHERE it.info = 'bottom 10 rank') TO 'benchmark/result-db-eval/job/q1b/data/1b_it.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_companies AS mc  WHERE NOT mc.note LIKE '%(as Metro-Goldwyn-Mayer Pictures)%') TO 'benchmark/result-db-eval/job/q1b/data/1b_mc.csv' CSV;
\copy (SELECT DISTINCT * FROM movie_info_idx AS mi_idx ) TO 'benchmark/result-db-eval/job/q1b/data/1b_mi_idx.csv' CSV;
\copy (SELECT DISTINCT * FROM title AS t  WHERE t.production_year >= 2005 AND t.production_year <= 2010) TO 'benchmark/result-db-eval/job/q1b/data/1b_t.csv' CSV;
