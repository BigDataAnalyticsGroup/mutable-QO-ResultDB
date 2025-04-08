select * from dblp14 dblp14_0, dblp14 dblp14_1, dblp21 dblp21_2, dblp21 dblp21_3 where dblp14_0.s = dblp14_1.s and dblp14_0.d = dblp21_2.s and dblp14_1.d = dblp21_3.s and dblp21_2.d = dblp21_3.d;
