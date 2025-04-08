select * from dblp25 dblp25_0, dblp25 dblp25_1, dblp22 dblp22_2, dblp22 dblp22_3 where dblp25_0.s = dblp25_1.s and dblp25_0.d = dblp22_2.s and dblp25_1.d = dblp22_3.s and dblp22_2.d = dblp22_3.d;
