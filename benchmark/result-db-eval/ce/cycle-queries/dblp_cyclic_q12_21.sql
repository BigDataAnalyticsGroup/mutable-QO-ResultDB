select * from dblp19, dblp8, dblp17, dblp9, dblp21, dblp2 where dblp19.s = dblp2.d and dblp19.d = dblp8.s and dblp8.d = dblp17.s and dblp17.d = dblp9.s and dblp9.d = dblp21.s and dblp21.d = dblp2.s;
