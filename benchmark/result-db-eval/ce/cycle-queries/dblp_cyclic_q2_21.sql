select * from dblp2 dblp2_0, dblp2 dblp2_1, dblp23 dblp23_2, dblp23 dblp23_3 where dblp2_0.s = dblp2_1.s and dblp2_0.d = dblp23_2.s and dblp2_1.d = dblp23_3.s and dblp23_2.d = dblp23_3.d;
