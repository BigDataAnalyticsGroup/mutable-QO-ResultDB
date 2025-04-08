select * from dblp26 dblp26_0, dblp26 dblp26_1, dblp1, dblp25 where dblp26_0.s = dblp26_1.s and dblp26_0.d = dblp1.s and dblp26_1.d = dblp25.s and dblp1.d = dblp25.d;
