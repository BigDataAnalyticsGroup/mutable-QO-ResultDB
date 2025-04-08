select * from dblp26, dblp5, dblp9, dblp8, dblp17, dblp25 where dblp26.s = dblp25.d and dblp26.d = dblp5.s and dblp5.d = dblp9.s and dblp9.d = dblp8.s and dblp8.d = dblp17.s and dblp17.d = dblp25.s;
