select * from dblp9, dblp5, dblp17, dblp2, dblp25, dblp21 where dblp9.s = dblp21.d and dblp9.d = dblp5.s and dblp5.d = dblp17.s and dblp17.d = dblp2.s and dblp2.d = dblp25.s and dblp25.d = dblp21.s;
