select * from dblp9 dblp9_0, dblp9 dblp9_1, dblp21, dblp5 where dblp9_0.s = dblp9_1.s and dblp9_0.d = dblp21.s and dblp9_1.d = dblp5.s and dblp21.d = dblp5.d;
