select * from dblp2 dblp2_0, dblp2 dblp2_1, dblp21, dblp5 where dblp2_0.s = dblp2_1.s and dblp2_0.d = dblp21.s and dblp2_1.d = dblp5.s and dblp21.d = dblp5.d;
