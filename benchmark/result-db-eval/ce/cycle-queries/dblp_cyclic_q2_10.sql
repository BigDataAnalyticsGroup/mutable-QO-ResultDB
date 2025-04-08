select * from dblp14 dblp14_0, dblp14 dblp14_1, dblp21, dblp5 where dblp14_0.s = dblp14_1.s and dblp14_0.d = dblp21.s and dblp14_1.d = dblp5.s and dblp21.d = dblp5.d;
