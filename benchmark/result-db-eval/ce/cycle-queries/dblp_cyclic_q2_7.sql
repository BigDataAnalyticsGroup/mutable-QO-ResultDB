select * from dblp9 dblp9_0, dblp9 dblp9_1, dblp12, dblp1 where dblp9_0.s = dblp9_1.s and dblp9_0.d = dblp12.s and dblp9_1.d = dblp1.s and dblp12.d = dblp1.d;
