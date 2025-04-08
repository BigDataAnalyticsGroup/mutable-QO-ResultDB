select * from dblp2 dblp2_0, dblp2 dblp2_1, dblp7 dblp7_2, dblp7 dblp7_3 where dblp2_0.s = dblp2_1.s and dblp2_0.d = dblp7_2.s and dblp2_1.d = dblp7_3.s and dblp7_2.d = dblp7_3.d;
