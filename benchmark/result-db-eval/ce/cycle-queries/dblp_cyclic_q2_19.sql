select * from dblp8 dblp8_0, dblp8 dblp8_1, dblp24 dblp24_2, dblp24 dblp24_3 where dblp8_0.s = dblp8_1.s and dblp8_0.d = dblp24_2.s and dblp8_1.d = dblp24_3.s and dblp24_2.d = dblp24_3.d;
