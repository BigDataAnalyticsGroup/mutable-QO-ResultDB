select * from yago1, yago25, yago50, yago3, yago36, yago8 where yago1.s = yago25.s and yago1.d = yago3.d and yago25.d = yago8.d and yago50.s = yago3.s and yago50.d = yago36.d and yago36.s = yago8.s;
