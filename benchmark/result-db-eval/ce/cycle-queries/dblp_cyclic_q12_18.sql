select * from dblp16, dblp9, dblp8, dblp18, dblp5, dblp2 where dblp16.s = dblp2.d and dblp16.d = dblp9.s and dblp9.d = dblp8.s and dblp8.d = dblp18.s and dblp18.d = dblp5.s and dblp5.d = dblp2.s;
