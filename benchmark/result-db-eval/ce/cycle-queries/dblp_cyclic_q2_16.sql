select * from dblp25, dblp1, dblp22 dblp22_2, dblp22 dblp22_3 where dblp25.s = dblp1.s and dblp25.d = dblp22_2.s and dblp1.d = dblp22_3.s and dblp22_2.d = dblp22_3.d;
