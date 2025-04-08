select * from dblp26, dblp8, dblp5, dblp2, dblp17, dblp1 where dblp26.s = dblp1.d and dblp26.d = dblp8.s and dblp8.d = dblp5.s and dblp5.d = dblp2.s and dblp2.d = dblp17.s and dblp17.d = dblp1.s;
