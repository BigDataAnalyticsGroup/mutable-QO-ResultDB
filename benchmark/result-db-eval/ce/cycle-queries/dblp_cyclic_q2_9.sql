select * from dblp17 dblp17_0, dblp17 dblp17_1, dblp9 dblp9_2, dblp9 dblp9_3 where dblp17_0.s = dblp17_1.s and dblp17_0.d = dblp9_2.s and dblp17_1.d = dblp9_3.s and dblp9_2.d = dblp9_3.d;
