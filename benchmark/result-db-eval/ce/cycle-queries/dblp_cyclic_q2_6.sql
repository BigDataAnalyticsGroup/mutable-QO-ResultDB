select * from dblp25 dblp25_0, dblp25 dblp25_1, dblp24 dblp24_2, dblp24 dblp24_3 where dblp25_0.s = dblp25_1.s and dblp25_0.d = dblp24_2.s and dblp25_1.d = dblp24_3.s and dblp24_2.d = dblp24_3.d;
