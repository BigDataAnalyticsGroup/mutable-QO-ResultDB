select * from dblp8 dblp8_0, dblp8 dblp8_1, dblp23 dblp23_2, dblp23 dblp23_3 where dblp8_0.s = dblp8_1.s and dblp8_0.d = dblp23_2.s and dblp8_1.d = dblp23_3.s and dblp23_2.d = dblp23_3.d;
