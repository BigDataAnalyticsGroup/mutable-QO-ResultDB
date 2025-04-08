select * from dblp18 dblp18_0, dblp18 dblp18_1, dblp21, dblp5 where dblp18_0.s = dblp18_1.s and dblp18_0.d = dblp21.s and dblp18_1.d = dblp5.s and dblp21.d = dblp5.d;
