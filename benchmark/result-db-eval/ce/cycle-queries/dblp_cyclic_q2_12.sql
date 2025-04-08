select * from dblp18 dblp18_0, dblp18 dblp18_1, dblp22 dblp22_2, dblp22 dblp22_3 where dblp18_0.s = dblp18_1.s and dblp18_0.d = dblp22_2.s and dblp18_1.d = dblp22_3.s and dblp22_2.d = dblp22_3.d;
