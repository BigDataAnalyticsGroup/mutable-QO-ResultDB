select * from dblp26, dblp2, dblp8, dblp18, dblp21, dblp1 where dblp26.s = dblp1.d and dblp26.d = dblp2.s and dblp2.d = dblp8.s and dblp8.d = dblp18.s and dblp18.d = dblp21.s and dblp21.d = dblp1.s;
