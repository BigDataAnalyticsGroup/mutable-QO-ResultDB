select * from dblp2 dblp2_0, dblp2 dblp2_1, dblp5 dblp5_2, dblp5 dblp5_3 where dblp2_0.s = dblp2_1.s and dblp2_0.d = dblp5_2.s and dblp2_1.d = dblp5_3.s and dblp5_2.d = dblp5_3.d;
