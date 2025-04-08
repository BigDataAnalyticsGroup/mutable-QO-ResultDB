select * from dblp16 dblp16_0, dblp16 dblp16_1, dblp23 dblp23_2, dblp23 dblp23_3 where dblp16_0.s = dblp16_1.s and dblp16_0.d = dblp23_2.s and dblp16_1.d = dblp23_3.s and dblp23_2.d = dblp23_3.d;
