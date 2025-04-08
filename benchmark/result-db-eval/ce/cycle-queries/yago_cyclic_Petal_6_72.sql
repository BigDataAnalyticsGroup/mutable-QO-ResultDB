select * from yago8, yago0, yago31, yago11, yago36, yago3 where yago8.s = yago0.s and yago8.d = yago11.d and yago0.d = yago3.d and yago31.s = yago11.s and yago31.d = yago36.d and yago36.s = yago3.s;
