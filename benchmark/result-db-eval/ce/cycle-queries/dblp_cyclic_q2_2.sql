select * from dblp26, dblp21, dblp25, dblp1 where dblp26.s = dblp21.s and dblp26.d = dblp25.s and dblp21.d = dblp1.s and dblp25.d = dblp1.d;
