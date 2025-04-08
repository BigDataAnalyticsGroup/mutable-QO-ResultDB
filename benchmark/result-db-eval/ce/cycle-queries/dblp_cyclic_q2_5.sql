select * from dblp17 dblp17_0, dblp17 dblp17_1, dblp7 dblp7_2, dblp7 dblp7_3 where dblp17_0.s = dblp17_1.s and dblp17_0.d = dblp7_2.s and dblp17_1.d = dblp7_3.s and dblp7_2.d = dblp7_3.d;
