select * from dblp25 dblp25_0, dblp25 dblp25_1, dblp21, dblp26 where dblp25_0.s = dblp25_1.s and dblp25_0.d = dblp21.s and dblp25_1.d = dblp26.s and dblp21.d = dblp26.d;
