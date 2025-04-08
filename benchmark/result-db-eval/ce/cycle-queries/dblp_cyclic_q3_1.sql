select * from dblp23 dblp23_0, dblp23 dblp23_1, dblp10 dblp10_2, dblp10 dblp10_3 where dblp23_0.s = dblp23_1.s and dblp23_0.d = dblp10_2.s and dblp23_1.d = dblp10_3.d and dblp10_2.d = dblp10_3.s;
