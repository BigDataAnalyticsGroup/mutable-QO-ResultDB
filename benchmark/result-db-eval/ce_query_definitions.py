from query_utility import Relation, Join, JoinGraph


def create_qdblp_cyclic_q8_1():
	dblp23 = Relation(name = "dblp23", alias = "dblp23", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp23, dblp21, dblp5, dblp9, dblp20_4, dblp20_5]

	j0 = Join(dblp23, dblp21, ["s"], ["s"])
	j1 = Join(dblp23, dblp5, ["d"], ["s"])
	j2 = Join(dblp21, dblp5, ["d"], ["d"])
	j3 = Join(dblp5, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_2():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_5 = Relation(name = "dblp8", alias = "dblp8_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp8_4, dblp8_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp8_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp8_5, ["d"], ["s"])
	j6 = Join(dblp8_4, dblp8_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_3():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_7():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_6():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_4():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_5():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_8():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp8_1, dblp8_2, dblp9_3, dblp18_4, dblp18_5]

	j0 = Join(dblp9_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9_3, ["d"], ["s"])
	j4 = Join(dblp9_3, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9_3, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_9():
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_14():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp9, dblp18_4, dblp18_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_11():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp2, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp2, ["d"], ["s"])
	j4 = Join(dblp2, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_10():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp8_1, dblp8_2, dblp17_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17_3, ["d"], ["s"])
	j4 = Join(dblp17_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_12():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp5, dblp20_4, dblp20_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp5, ["d"], ["s"])
	j4 = Join(dblp5, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp5, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qdblp_cyclic_q8_13():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_1():
	dblp23 = Relation(name = "dblp23", alias = "dblp23", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp23, dblp21, dblp5, dblp9, dblp20_4, dblp20_5]

	j0 = Join(dblp23, dblp21, ["s"], ["s"])
	j1 = Join(dblp23, dblp5, ["d"], ["s"])
	j2 = Join(dblp21, dblp5, ["d"], ["d"])
	j3 = Join(dblp5, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_2():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_5 = Relation(name = "dblp8", alias = "dblp8_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp8_4, dblp8_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp8_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp8_5, ["d"], ["s"])
	j6 = Join(dblp8_4, dblp8_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_3():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_7():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_6():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_4():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_5():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_8():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp8_1, dblp8_2, dblp9_3, dblp18_4, dblp18_5]

	j0 = Join(dblp9_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9_3, ["d"], ["s"])
	j4 = Join(dblp9_3, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9_3, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_9():
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_14():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp9, dblp18_4, dblp18_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_11():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp2, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp2, ["d"], ["s"])
	j4 = Join(dblp2, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_10():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp8_1, dblp8_2, dblp17_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17_3, ["d"], ["s"])
	j4 = Join(dblp17_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_12():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp5, dblp20_4, dblp20_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp5, ["d"], ["s"])
	j4 = Join(dblp5, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp5, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_qq8_13():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_1():
	dblp23 = Relation(name = "dblp23", alias = "dblp23", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp23, dblp21, dblp5, dblp9, dblp20_4, dblp20_5]

	j0 = Join(dblp23, dblp21, ["s"], ["s"])
	j1 = Join(dblp23, dblp5, ["d"], ["s"])
	j2 = Join(dblp21, dblp5, ["d"], ["d"])
	j3 = Join(dblp5, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_2():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_5 = Relation(name = "dblp8", alias = "dblp8_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp8_4, dblp8_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp8_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp8_5, ["d"], ["s"])
	j6 = Join(dblp8_4, dblp8_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_3():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_7():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_6():
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp2, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp2, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_4():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_5():
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp9, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_8():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp8_1, dblp8_2, dblp9_3, dblp18_4, dblp18_5]

	j0 = Join(dblp9_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9_3, ["d"], ["s"])
	j4 = Join(dblp9_3, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9_3, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_9():
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17, dblp8_1, dblp8_2, dblp8_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["s"])
	j4 = Join(dblp8_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp8_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_14():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_4 = Relation(name = "dblp18", alias = "dblp18_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp9, dblp18_4, dblp18_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp9, ["d"], ["s"])
	j4 = Join(dblp9, dblp18_4, ["s"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["d"], ["s"])
	j6 = Join(dblp18_4, dblp18_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_11():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp2, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp2, ["d"], ["s"])
	j4 = Join(dblp2, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_10():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp8_1, dblp8_2, dblp17_3, dblp20_4, dblp20_5]

	j0 = Join(dblp17_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17_3, ["d"], ["s"])
	j4 = Join(dblp17_3, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17_3, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_12():
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp19, dblp8_1, dblp8_2, dblp5, dblp20_4, dblp20_5]

	j0 = Join(dblp19, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp19, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp5, ["d"], ["s"])
	j4 = Join(dblp5, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp5, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q8_13():
	dblp16 = Relation(name = "dblp16", alias = "dblp16", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_4 = Relation(name = "dblp20", alias = "dblp20_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp16, dblp8_1, dblp8_2, dblp17, dblp20_4, dblp20_5]

	j0 = Join(dblp16, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp16, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_2, ["d"], ["d"])
	j3 = Join(dblp8_2, dblp17, ["d"], ["s"])
	j4 = Join(dblp17, dblp20_4, ["s"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["d"], ["s"])
	j6 = Join(dblp20_4, dblp20_5, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 1000', 'dblp2_0.s < 1000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 1000', 'dblp2_1.s < 1000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = ['dblp7_2.d < 1000', 'dblp7_2.s < 1000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = ['dblp7_3.d < 1000', 'dblp7_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 1000', 'dblp2_0.s < 1000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 1000', 'dblp2_1.s < 1000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 1000', 'dblp23_2.s < 1000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 1000', 'dblp23_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = ['dblp18_0.d < 1000', 'dblp18_0.s < 1000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = ['dblp18_1.d < 1000', 'dblp18_1.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 1000', 'dblp5.s < 1000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = ['dblp8_0.d < 1000', 'dblp8_0.s < 1000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = ['dblp8_1.d < 1000', 'dblp8_1.s < 1000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = ['dblp24_2.d < 1000', 'dblp24_2.s < 1000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = ['dblp24_3.d < 1000', 'dblp24_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 1000', 'dblp2_0.s < 1000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 1000', 'dblp2_1.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 1000', 'dblp5.s < 1000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = ['dblp17_0.d < 1000', 'dblp17_0.s < 1000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = ['dblp17_1.d < 1000', 'dblp17_1.s < 1000'], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['s', 'd'], filters = ['dblp9_2.d < 1000', 'dblp9_2.s < 1000'], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['s', 'd'], filters = ['dblp9_3.d < 1000', 'dblp9_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['s', 'd'], filters = ['dblp26_0.d < 1000', 'dblp26_0.s < 1000'], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['s', 'd'], filters = ['dblp26_1.d < 1000', 'dblp26_1.s < 1000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 1000', 'dblp1.s < 1000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 1000', 'dblp25.s < 1000'], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = ['dblp9_0.d < 1000', 'dblp9_0.s < 1000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = ['dblp9_1.d < 1000', 'dblp9_1.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 1000', 'dblp5.s < 1000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = ['dblp26.d < 1000', 'dblp26.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 1000', 'dblp25.s < 1000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 1000', 'dblp1.s < 1000'], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['s', 'd'], filters = ['dblp20_0.d < 1000', 'dblp20_0.s < 1000'], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['s', 'd'], filters = ['dblp20_1.d < 1000', 'dblp20_1.s < 1000'], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['s', 'd'], filters = ['dblp20_2.d < 1000', 'dblp20_2.s < 1000'], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['s', 'd'], filters = ['dblp20_3.d < 1000', 'dblp20_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = ['dblp17_0.d < 1000', 'dblp17_0.s < 1000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = ['dblp17_1.d < 1000', 'dblp17_1.s < 1000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = ['dblp7_2.d < 1000', 'dblp7_2.s < 1000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = ['dblp7_3.d < 1000', 'dblp7_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 1000', 'dblp25_0.s < 1000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 1000', 'dblp25_1.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = ['dblp26.d < 1000', 'dblp26.s < 1000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 1000', 'dblp25_0.s < 1000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 1000', 'dblp25_1.s < 1000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = ['dblp24_2.d < 1000', 'dblp24_2.s < 1000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = ['dblp24_3.d < 1000', 'dblp24_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = ['dblp9_0.d < 1000', 'dblp9_0.s < 1000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = ['dblp9_1.d < 1000', 'dblp9_1.s < 1000'], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['s', 'd'], filters = ['dblp12.d < 1000', 'dblp12.s < 1000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 1000', 'dblp1.s < 1000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 1000', 'dblp25_0.s < 1000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 1000', 'dblp25_1.s < 1000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 1000', 'dblp22_2.s < 1000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 1000', 'dblp22_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = ['dblp8_0.d < 1000', 'dblp8_0.s < 1000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = ['dblp8_1.d < 1000', 'dblp8_1.s < 1000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 1000', 'dblp23_2.s < 1000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 1000', 'dblp23_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 1000', 'dblp25.s < 1000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 1000', 'dblp1.s < 1000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 1000', 'dblp22_2.s < 1000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 1000', 'dblp22_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 1000', 'dblp2_0.s < 1000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 1000', 'dblp2_1.s < 1000'], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['s', 'd'], filters = ['dblp5_2.d < 1000', 'dblp5_2.s < 1000'], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['s', 'd'], filters = ['dblp5_3.d < 1000', 'dblp5_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['s', 'd'], filters = ['dblp16_0.d < 1000', 'dblp16_0.s < 1000'], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['s', 'd'], filters = ['dblp16_1.d < 1000', 'dblp16_1.s < 1000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 1000', 'dblp23_2.s < 1000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 1000', 'dblp23_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = ['dblp18_0.d < 1000', 'dblp18_0.s < 1000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = ['dblp18_1.d < 1000', 'dblp18_1.s < 1000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 1000', 'dblp22_2.s < 1000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 1000', 'dblp22_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = ['dblp14_0.d < 1000', 'dblp14_0.s < 1000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = ['dblp14_1.d < 1000', 'dblp14_1.s < 1000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 1000', 'dblp21.s < 1000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 1000', 'dblp5.s < 1000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = ['dblp14_0.d < 1000', 'dblp14_0.s < 1000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = ['dblp14_1.d < 1000', 'dblp14_1.s < 1000'], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['s', 'd'], filters = ['dblp21_2.d < 1000', 'dblp21_2.s < 1000'], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['s', 'd'], filters = ['dblp21_3.d < 1000', 'dblp21_3.s < 1000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 10000', 'dblp2_0.s < 10000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 10000', 'dblp2_1.s < 10000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = ['dblp7_2.d < 10000', 'dblp7_2.s < 10000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = ['dblp7_3.d < 10000', 'dblp7_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 10000', 'dblp2_0.s < 10000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 10000', 'dblp2_1.s < 10000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 10000', 'dblp23_2.s < 10000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 10000', 'dblp23_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = ['dblp18_0.d < 10000', 'dblp18_0.s < 10000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = ['dblp18_1.d < 10000', 'dblp18_1.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 10000', 'dblp5.s < 10000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = ['dblp8_0.d < 10000', 'dblp8_0.s < 10000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = ['dblp8_1.d < 10000', 'dblp8_1.s < 10000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = ['dblp24_2.d < 10000', 'dblp24_2.s < 10000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = ['dblp24_3.d < 10000', 'dblp24_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 10000', 'dblp2_0.s < 10000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 10000', 'dblp2_1.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 10000', 'dblp5.s < 10000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = ['dblp17_0.d < 10000', 'dblp17_0.s < 10000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = ['dblp17_1.d < 10000', 'dblp17_1.s < 10000'], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['s', 'd'], filters = ['dblp9_2.d < 10000', 'dblp9_2.s < 10000'], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['s', 'd'], filters = ['dblp9_3.d < 10000', 'dblp9_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['s', 'd'], filters = ['dblp26_0.d < 10000', 'dblp26_0.s < 10000'], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['s', 'd'], filters = ['dblp26_1.d < 10000', 'dblp26_1.s < 10000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 10000', 'dblp1.s < 10000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 10000', 'dblp25.s < 10000'], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = ['dblp9_0.d < 10000', 'dblp9_0.s < 10000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = ['dblp9_1.d < 10000', 'dblp9_1.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 10000', 'dblp5.s < 10000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = ['dblp26.d < 10000', 'dblp26.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 10000', 'dblp25.s < 10000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 10000', 'dblp1.s < 10000'], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['s', 'd'], filters = ['dblp20_0.d < 10000', 'dblp20_0.s < 10000'], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['s', 'd'], filters = ['dblp20_1.d < 10000', 'dblp20_1.s < 10000'], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['s', 'd'], filters = ['dblp20_2.d < 10000', 'dblp20_2.s < 10000'], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['s', 'd'], filters = ['dblp20_3.d < 10000', 'dblp20_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = ['dblp17_0.d < 10000', 'dblp17_0.s < 10000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = ['dblp17_1.d < 10000', 'dblp17_1.s < 10000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['s', 'd'], filters = ['dblp7_2.d < 10000', 'dblp7_2.s < 10000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['s', 'd'], filters = ['dblp7_3.d < 10000', 'dblp7_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 10000', 'dblp25_0.s < 10000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 10000', 'dblp25_1.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = ['dblp26.d < 10000', 'dblp26.s < 10000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 10000', 'dblp25_0.s < 10000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 10000', 'dblp25_1.s < 10000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['s', 'd'], filters = ['dblp24_2.d < 10000', 'dblp24_2.s < 10000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['s', 'd'], filters = ['dblp24_3.d < 10000', 'dblp24_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = ['dblp9_0.d < 10000', 'dblp9_0.s < 10000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['s', 'd'], filters = ['dblp9_1.d < 10000', 'dblp9_1.s < 10000'], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['s', 'd'], filters = ['dblp12.d < 10000', 'dblp12.s < 10000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 10000', 'dblp1.s < 10000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = ['dblp25_0.d < 10000', 'dblp25_0.s < 10000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['s', 'd'], filters = ['dblp25_1.d < 10000', 'dblp25_1.s < 10000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 10000', 'dblp22_2.s < 10000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 10000', 'dblp22_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['s', 'd'], filters = ['dblp8_0.d < 10000', 'dblp8_0.s < 10000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['s', 'd'], filters = ['dblp8_1.d < 10000', 'dblp8_1.s < 10000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 10000', 'dblp23_2.s < 10000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 10000', 'dblp23_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = ['dblp25.d < 10000', 'dblp25.s < 10000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = ['dblp1.d < 10000', 'dblp1.s < 10000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 10000', 'dblp22_2.s < 10000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 10000', 'dblp22_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = ['dblp2_0.d < 10000', 'dblp2_0.s < 10000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = ['dblp2_1.d < 10000', 'dblp2_1.s < 10000'], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['s', 'd'], filters = ['dblp5_2.d < 10000', 'dblp5_2.s < 10000'], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['s', 'd'], filters = ['dblp5_3.d < 10000', 'dblp5_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['s', 'd'], filters = ['dblp16_0.d < 10000', 'dblp16_0.s < 10000'], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['s', 'd'], filters = ['dblp16_1.d < 10000', 'dblp16_1.s < 10000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['s', 'd'], filters = ['dblp23_2.d < 10000', 'dblp23_2.s < 10000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['s', 'd'], filters = ['dblp23_3.d < 10000', 'dblp23_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['s', 'd'], filters = ['dblp18_0.d < 10000', 'dblp18_0.s < 10000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = ['dblp18_1.d < 10000', 'dblp18_1.s < 10000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['s', 'd'], filters = ['dblp22_2.d < 10000', 'dblp22_2.s < 10000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['s', 'd'], filters = ['dblp22_3.d < 10000', 'dblp22_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = ['dblp14_0.d < 10000', 'dblp14_0.s < 10000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = ['dblp14_1.d < 10000', 'dblp14_1.s < 10000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = ['dblp21.d < 10000', 'dblp21.s < 10000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = ['dblp5.d < 10000', 'dblp5.s < 10000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['s', 'd'], filters = ['dblp14_0.d < 10000', 'dblp14_0.s < 10000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['s', 'd'], filters = ['dblp14_1.d < 10000', 'dblp14_1.s < 10000'], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['s', 'd'], filters = ['dblp21_2.d < 10000', 'dblp21_2.s < 10000'], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['s', 'd'], filters = ['dblp21_3.d < 10000', 'dblp21_3.s < 10000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 100000', 'dblp2_0.s < 100000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 100000', 'dblp2_1.s < 100000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 100000', 'dblp7_2.s < 100000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 100000', 'dblp7_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 100000', 'dblp2_0.s < 100000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 100000', 'dblp2_1.s < 100000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 100000', 'dblp23_2.s < 100000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 100000', 'dblp23_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 100000', 'dblp18_0.s < 100000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 100000', 'dblp18_1.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 100000', 'dblp5.s < 100000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 100000', 'dblp8_0.s < 100000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 100000', 'dblp8_1.s < 100000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 100000', 'dblp24_2.s < 100000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 100000', 'dblp24_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 100000', 'dblp2_0.s < 100000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 100000', 'dblp2_1.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 100000', 'dblp5.s < 100000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 100000', 'dblp17_0.s < 100000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 100000', 'dblp17_1.s < 100000'], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = ['dblp9_2.d < 100000', 'dblp9_2.s < 100000'], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = ['dblp9_3.d < 100000', 'dblp9_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = ['dblp26_0.d < 100000', 'dblp26_0.s < 100000'], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = ['dblp26_1.d < 100000', 'dblp26_1.s < 100000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 100000', 'dblp1.s < 100000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 100000', 'dblp25.s < 100000'], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 100000', 'dblp9_0.s < 100000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 100000', 'dblp9_1.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 100000', 'dblp5.s < 100000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 100000', 'dblp26.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 100000', 'dblp25.s < 100000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 100000', 'dblp1.s < 100000'], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['d', 's'], filters = ['dblp20_0.d < 100000', 'dblp20_0.s < 100000'], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['d', 's'], filters = ['dblp20_1.d < 100000', 'dblp20_1.s < 100000'], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['d', 's'], filters = ['dblp20_2.d < 100000', 'dblp20_2.s < 100000'], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['d', 's'], filters = ['dblp20_3.d < 100000', 'dblp20_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 100000', 'dblp17_0.s < 100000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 100000', 'dblp17_1.s < 100000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 100000', 'dblp7_2.s < 100000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 100000', 'dblp7_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 100000', 'dblp25_0.s < 100000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 100000', 'dblp25_1.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 100000', 'dblp26.s < 100000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 100000', 'dblp25_0.s < 100000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 100000', 'dblp25_1.s < 100000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 100000', 'dblp24_2.s < 100000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 100000', 'dblp24_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 100000', 'dblp9_0.s < 100000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 100000', 'dblp9_1.s < 100000'], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['d', 's'], filters = ['dblp12.d < 100000', 'dblp12.s < 100000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 100000', 'dblp1.s < 100000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 100000', 'dblp25_0.s < 100000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 100000', 'dblp25_1.s < 100000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 100000', 'dblp22_2.s < 100000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 100000', 'dblp22_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 100000', 'dblp8_0.s < 100000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 100000', 'dblp8_1.s < 100000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 100000', 'dblp23_2.s < 100000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 100000', 'dblp23_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 100000', 'dblp25.s < 100000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 100000', 'dblp1.s < 100000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 100000', 'dblp22_2.s < 100000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 100000', 'dblp22_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 100000', 'dblp2_0.s < 100000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 100000', 'dblp2_1.s < 100000'], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['d', 's'], filters = ['dblp5_2.d < 100000', 'dblp5_2.s < 100000'], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['d', 's'], filters = ['dblp5_3.d < 100000', 'dblp5_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = ['dblp16_0.d < 100000', 'dblp16_0.s < 100000'], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = ['dblp16_1.d < 100000', 'dblp16_1.s < 100000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 100000', 'dblp23_2.s < 100000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 100000', 'dblp23_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 100000', 'dblp18_0.s < 100000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 100000', 'dblp18_1.s < 100000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 100000', 'dblp22_2.s < 100000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 100000', 'dblp22_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 100000', 'dblp14_0.s < 100000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 100000', 'dblp14_1.s < 100000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 100000', 'dblp21.s < 100000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 100000', 'dblp5.s < 100000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 100000', 'dblp14_0.s < 100000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 100000', 'dblp14_1.s < 100000'], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = ['dblp21_2.d < 100000', 'dblp21_2.s < 100000'], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = ['dblp21_3.d < 100000', 'dblp21_3.s < 100000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 1000000', 'dblp2_0.s < 1000000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 1000000', 'dblp2_1.s < 1000000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 1000000', 'dblp7_2.s < 1000000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 1000000', 'dblp7_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 1000000', 'dblp2_0.s < 1000000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 1000000', 'dblp2_1.s < 1000000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 1000000', 'dblp23_2.s < 1000000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 1000000', 'dblp23_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 1000000', 'dblp18_0.s < 1000000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 1000000', 'dblp18_1.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 1000000', 'dblp5.s < 1000000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 1000000', 'dblp8_0.s < 1000000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 1000000', 'dblp8_1.s < 1000000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 1000000', 'dblp24_2.s < 1000000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 1000000', 'dblp24_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 1000000', 'dblp2_0.s < 1000000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 1000000', 'dblp2_1.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 1000000', 'dblp5.s < 1000000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 1000000', 'dblp17_0.s < 1000000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 1000000', 'dblp17_1.s < 1000000'], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = ['dblp9_2.d < 1000000', 'dblp9_2.s < 1000000'], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = ['dblp9_3.d < 1000000', 'dblp9_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = ['dblp26_0.d < 1000000', 'dblp26_0.s < 1000000'], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = ['dblp26_1.d < 1000000', 'dblp26_1.s < 1000000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 1000000', 'dblp1.s < 1000000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 1000000', 'dblp25.s < 1000000'], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 1000000', 'dblp9_0.s < 1000000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 1000000', 'dblp9_1.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 1000000', 'dblp5.s < 1000000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 1000000', 'dblp26.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 1000000', 'dblp25.s < 1000000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 1000000', 'dblp1.s < 1000000'], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['d', 's'], filters = ['dblp20_0.d < 1000000', 'dblp20_0.s < 1000000'], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['d', 's'], filters = ['dblp20_1.d < 1000000', 'dblp20_1.s < 1000000'], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['d', 's'], filters = ['dblp20_2.d < 1000000', 'dblp20_2.s < 1000000'], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['d', 's'], filters = ['dblp20_3.d < 1000000', 'dblp20_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 1000000', 'dblp17_0.s < 1000000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 1000000', 'dblp17_1.s < 1000000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 1000000', 'dblp7_2.s < 1000000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 1000000', 'dblp7_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 1000000', 'dblp25_0.s < 1000000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 1000000', 'dblp25_1.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 1000000', 'dblp26.s < 1000000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 1000000', 'dblp25_0.s < 1000000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 1000000', 'dblp25_1.s < 1000000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 1000000', 'dblp24_2.s < 1000000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 1000000', 'dblp24_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 1000000', 'dblp9_0.s < 1000000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 1000000', 'dblp9_1.s < 1000000'], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['d', 's'], filters = ['dblp12.d < 1000000', 'dblp12.s < 1000000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 1000000', 'dblp1.s < 1000000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 1000000', 'dblp25_0.s < 1000000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 1000000', 'dblp25_1.s < 1000000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 1000000', 'dblp22_2.s < 1000000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 1000000', 'dblp22_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 1000000', 'dblp8_0.s < 1000000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 1000000', 'dblp8_1.s < 1000000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 1000000', 'dblp23_2.s < 1000000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 1000000', 'dblp23_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 1000000', 'dblp25.s < 1000000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 1000000', 'dblp1.s < 1000000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 1000000', 'dblp22_2.s < 1000000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 1000000', 'dblp22_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 1000000', 'dblp2_0.s < 1000000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 1000000', 'dblp2_1.s < 1000000'], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['d', 's'], filters = ['dblp5_2.d < 1000000', 'dblp5_2.s < 1000000'], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['d', 's'], filters = ['dblp5_3.d < 1000000', 'dblp5_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = ['dblp16_0.d < 1000000', 'dblp16_0.s < 1000000'], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = ['dblp16_1.d < 1000000', 'dblp16_1.s < 1000000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 1000000', 'dblp23_2.s < 1000000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 1000000', 'dblp23_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 1000000', 'dblp18_0.s < 1000000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 1000000', 'dblp18_1.s < 1000000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 1000000', 'dblp22_2.s < 1000000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 1000000', 'dblp22_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 1000000', 'dblp14_0.s < 1000000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 1000000', 'dblp14_1.s < 1000000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 1000000', 'dblp21.s < 1000000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 1000000', 'dblp5.s < 1000000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 1000000', 'dblp14_0.s < 1000000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 1000000', 'dblp14_1.s < 1000000'], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = ['dblp21_2.d < 1000000', 'dblp21_2.s < 1000000'], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = ['dblp21_3.d < 1000000', 'dblp21_3.s < 1000000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 2000000', 'dblp2_0.s < 1200000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 2000000', 'dblp2_1.s < 1200000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 2000000', 'dblp7_2.s < 1200000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 2000000', 'dblp7_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 2000000', 'dblp2_0.s < 1200000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 2000000', 'dblp2_1.s < 1200000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 2000000', 'dblp23_2.s < 1200000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 2000000', 'dblp23_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 2000000', 'dblp18_0.s < 1200000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 2000000', 'dblp18_1.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 2000000', 'dblp5.s < 1200000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 2000000', 'dblp8_0.s < 1200000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 2000000', 'dblp8_1.s < 1200000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 2000000', 'dblp24_2.s < 1200000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 2000000', 'dblp24_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 2000000', 'dblp2_0.s < 1200000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 2000000', 'dblp2_1.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 2000000', 'dblp5.s < 1200000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 2000000', 'dblp17_0.s < 1200000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 2000000', 'dblp17_1.s < 1200000'], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = ['dblp9_2.d < 2000000', 'dblp9_2.s < 1200000'], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = ['dblp9_3.d < 2000000', 'dblp9_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = ['dblp26_0.d < 2000000', 'dblp26_0.s < 1200000'], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = ['dblp26_1.d < 2000000', 'dblp26_1.s < 1200000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 2000000', 'dblp1.s < 1200000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 2000000', 'dblp25.s < 1200000'], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 2000000', 'dblp9_0.s < 1200000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 2000000', 'dblp9_1.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 2000000', 'dblp5.s < 1200000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 2000000', 'dblp26.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 2000000', 'dblp25.s < 1200000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 2000000', 'dblp1.s < 1200000'], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['d', 's'], filters = ['dblp20_0.d < 2000000', 'dblp20_0.s < 1200000'], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['d', 's'], filters = ['dblp20_1.d < 2000000', 'dblp20_1.s < 1200000'], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['d', 's'], filters = ['dblp20_2.d < 2000000', 'dblp20_2.s < 1200000'], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['d', 's'], filters = ['dblp20_3.d < 2000000', 'dblp20_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = ['dblp17_0.d < 2000000', 'dblp17_0.s < 1200000'], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = ['dblp17_1.d < 2000000', 'dblp17_1.s < 1200000'], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = ['dblp7_2.d < 2000000', 'dblp7_2.s < 1200000'], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = ['dblp7_3.d < 2000000', 'dblp7_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 2000000', 'dblp25_0.s < 1200000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 2000000', 'dblp25_1.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = ['dblp26.d < 2000000', 'dblp26.s < 1200000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 2000000', 'dblp25_0.s < 1200000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 2000000', 'dblp25_1.s < 1200000'], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = ['dblp24_2.d < 2000000', 'dblp24_2.s < 1200000'], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = ['dblp24_3.d < 2000000', 'dblp24_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = ['dblp9_0.d < 2000000', 'dblp9_0.s < 1200000'], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = ['dblp9_1.d < 2000000', 'dblp9_1.s < 1200000'], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['d', 's'], filters = ['dblp12.d < 2000000', 'dblp12.s < 1200000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 2000000', 'dblp1.s < 1200000'], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = ['dblp25_0.d < 2000000', 'dblp25_0.s < 1200000'], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = ['dblp25_1.d < 2000000', 'dblp25_1.s < 1200000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 2000000', 'dblp22_2.s < 1200000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 2000000', 'dblp22_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = ['dblp8_0.d < 2000000', 'dblp8_0.s < 1200000'], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = ['dblp8_1.d < 2000000', 'dblp8_1.s < 1200000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 2000000', 'dblp23_2.s < 1200000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 2000000', 'dblp23_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = ['dblp25.d < 2000000', 'dblp25.s < 1200000'], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = ['dblp1.d < 2000000', 'dblp1.s < 1200000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 2000000', 'dblp22_2.s < 1200000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 2000000', 'dblp22_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = ['dblp2_0.d < 2000000', 'dblp2_0.s < 1200000'], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = ['dblp2_1.d < 2000000', 'dblp2_1.s < 1200000'], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['d', 's'], filters = ['dblp5_2.d < 2000000', 'dblp5_2.s < 1200000'], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['d', 's'], filters = ['dblp5_3.d < 2000000', 'dblp5_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = ['dblp16_0.d < 2000000', 'dblp16_0.s < 1200000'], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = ['dblp16_1.d < 2000000', 'dblp16_1.s < 1200000'], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = ['dblp23_2.d < 2000000', 'dblp23_2.s < 1200000'], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = ['dblp23_3.d < 2000000', 'dblp23_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = ['dblp18_0.d < 2000000', 'dblp18_0.s < 1200000'], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = ['dblp18_1.d < 2000000', 'dblp18_1.s < 1200000'], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = ['dblp22_2.d < 2000000', 'dblp22_2.s < 1200000'], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = ['dblp22_3.d < 2000000', 'dblp22_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 2000000', 'dblp14_0.s < 1200000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 2000000', 'dblp14_1.s < 1200000'], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = ['dblp21.d < 2000000', 'dblp21.s < 1200000'], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = ['dblp5.d < 2000000', 'dblp5.s < 1200000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = ['dblp14_0.d < 2000000', 'dblp14_0.s < 1200000'], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = ['dblp14_1.d < 2000000', 'dblp14_1.s < 1200000'], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = ['dblp21_2.d < 2000000', 'dblp21_2.s < 1200000'], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = ['dblp21_3.d < 2000000', 'dblp21_3.s < 1200000'], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_20():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp7_2, dblp7_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_21():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp23_2, dblp23_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_22():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_19():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp24_2, dblp24_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_18():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_8():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp1, dblp25]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp25, ["d"], ["s"])
	j3 = Join(dblp1, dblp25, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_3():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_2():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp25, dblp1]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp25, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["d"], ["s"])
	j3 = Join(dblp25, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_1():
	dblp20_0 = Relation(name = "dblp20", alias = "dblp20_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_1 = Relation(name = "dblp20", alias = "dblp20_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_2 = Relation(name = "dblp20", alias = "dblp20_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_3 = Relation(name = "dblp20", alias = "dblp20_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp20_0, dblp20_1, dblp20_2, dblp20_3]

	j0 = Join(dblp20_0, dblp20_1, ["s"], ["s"])
	j1 = Join(dblp20_0, dblp20_2, ["d"], ["s"])
	j2 = Join(dblp20_1, dblp20_3, ["d"], ["s"])
	j3 = Join(dblp20_2, dblp20_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_5():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp7_2 = Relation(name = "dblp7", alias = "dblp7_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp7_3 = Relation(name = "dblp7", alias = "dblp7_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp7_2, dblp7_3]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp7_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp7_3, ["d"], ["s"])
	j3 = Join(dblp7_2, dblp7_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_4():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_6():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp24_2 = Relation(name = "dblp24", alias = "dblp24_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp24_3 = Relation(name = "dblp24", alias = "dblp24_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp24_2, dblp24_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp24_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp24_3, ["d"], ["s"])
	j3 = Join(dblp24_2, dblp24_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_7():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp12 = Relation(name = "dblp12", alias = "dblp12", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp12, dblp1]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp12, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp1, ["d"], ["s"])
	j3 = Join(dblp12, dblp1, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_15():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp22_2, dblp22_3]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_14():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp23_2, dblp23_3]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_16():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp25, dblp1, dblp22_2, dblp22_3]

	j0 = Join(dblp25, dblp1, ["s"], ["s"])
	j1 = Join(dblp25, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_17():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp5_2, dblp5_3]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp5_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5_3, ["d"], ["s"])
	j3 = Join(dblp5_2, dblp5_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_13():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_2 = Relation(name = "dblp23", alias = "dblp23_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_3 = Relation(name = "dblp23", alias = "dblp23_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp23_2, dblp23_3]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp23_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp23_3, ["d"], ["s"])
	j3 = Join(dblp23_2, dblp23_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_12():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_2 = Relation(name = "dblp22", alias = "dblp22_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp22_3 = Relation(name = "dblp22", alias = "dblp22_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp22_2, dblp22_3]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp22_2, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp22_3, ["d"], ["s"])
	j3 = Join(dblp22_2, dblp22_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_10():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21, dblp5]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q2_11():
	dblp14_0 = Relation(name = "dblp14", alias = "dblp14_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp14_1 = Relation(name = "dblp14", alias = "dblp14_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp14_0, dblp14_1, dblp21_2, dblp21_3]

	j0 = Join(dblp14_0, dblp14_1, ["s"], ["s"])
	j1 = Join(dblp14_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp14_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q9_2():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_4 = Relation(name = "dblp9", alias = "dblp9_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_6 = Relation(name = "dblp9", alias = "dblp9_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp9_7 = Relation(name = "dblp9", alias = "dblp9_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp21, dblp2_2, dblp2_3, dblp9_4, dblp5, dblp9_6, dblp9_7]

	j0 = Join(dblp9_0, dblp2_2, ["s"], ["d"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp21, dblp9_6, ["s"], ["d"])
	j3 = Join(dblp21, dblp2_2, ["d"], ["s"])
	j4 = Join(dblp2_2, dblp2_3, ["s"], ["s"])
	j5 = Join(dblp2_3, dblp5, ["s"], ["d"])
	j6 = Join(dblp2_3, dblp9_4, ["d"], ["s"])
	j7 = Join(dblp9_4, dblp5, ["d"], ["s"])
	j8 = Join(dblp5, dblp9_7, ["s"], ["d"])
	j9 = Join(dblp9_6, dblp9_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_3():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_6 = Relation(name = "dblp17", alias = "dblp17_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_7 = Relation(name = "dblp17", alias = "dblp17_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp21, dblp2_2, dblp2_3, dblp17_4, dblp5, dblp17_6, dblp17_7]

	j0 = Join(dblp17_0, dblp2_2, ["s"], ["d"])
	j1 = Join(dblp17_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp21, dblp17_6, ["s"], ["d"])
	j3 = Join(dblp21, dblp2_2, ["d"], ["s"])
	j4 = Join(dblp2_2, dblp2_3, ["s"], ["s"])
	j5 = Join(dblp2_3, dblp5, ["s"], ["d"])
	j6 = Join(dblp2_3, dblp17_4, ["d"], ["s"])
	j7 = Join(dblp17_4, dblp5, ["d"], ["s"])
	j8 = Join(dblp5, dblp17_7, ["s"], ["d"])
	j9 = Join(dblp17_6, dblp17_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_1():
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_2 = Relation(name = "dblp18", alias = "dblp18_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_3 = Relation(name = "dblp18", alias = "dblp18_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_4 = Relation(name = "dblp5", alias = "dblp5_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_5 = Relation(name = "dblp17", alias = "dblp17_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_6 = Relation(name = "dblp5", alias = "dblp5_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_7 = Relation(name = "dblp5", alias = "dblp5_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp21, dblp17_1, dblp18_2, dblp18_3, dblp5_4, dblp17_5, dblp5_6, dblp5_7]

	j0 = Join(dblp21, dblp18_2, ["s"], ["d"])
	j1 = Join(dblp21, dblp17_1, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp5_6, ["s"], ["d"])
	j3 = Join(dblp17_1, dblp18_2, ["d"], ["s"])
	j4 = Join(dblp18_2, dblp18_3, ["s"], ["s"])
	j5 = Join(dblp18_3, dblp17_5, ["s"], ["d"])
	j6 = Join(dblp18_3, dblp5_4, ["d"], ["s"])
	j7 = Join(dblp5_4, dblp17_5, ["d"], ["s"])
	j8 = Join(dblp17_5, dblp5_7, ["s"], ["d"])
	j9 = Join(dblp5_6, dblp5_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_4():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_5 = Relation(name = "dblp2", alias = "dblp2_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26_6 = Relation(name = "dblp26", alias = "dblp26_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26_7 = Relation(name = "dblp26", alias = "dblp26_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp26_0, dblp2_1, dblp1, dblp25, dblp21, dblp2_5, dblp26_6, dblp26_7]

	j0 = Join(dblp26_0, dblp1, ["s"], ["d"])
	j1 = Join(dblp26_0, dblp2_1, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp26_6, ["s"], ["d"])
	j3 = Join(dblp2_1, dblp1, ["d"], ["s"])
	j4 = Join(dblp1, dblp25, ["s"], ["s"])
	j5 = Join(dblp25, dblp2_5, ["s"], ["d"])
	j6 = Join(dblp25, dblp21, ["d"], ["s"])
	j7 = Join(dblp21, dblp2_5, ["d"], ["s"])
	j8 = Join(dblp2_5, dblp26_7, ["s"], ["d"])
	j9 = Join(dblp26_6, dblp26_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_13():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_4 = Relation(name = "dblp2", alias = "dblp2_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_6 = Relation(name = "dblp2", alias = "dblp2_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_7 = Relation(name = "dblp2", alias = "dblp2_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp1, dblp21, dblp26, dblp2_4, dblp25, dblp2_6, dblp2_7]

	j0 = Join(dblp2_0, dblp21, ["s"], ["d"])
	j1 = Join(dblp2_0, dblp1, ["d"], ["s"])
	j2 = Join(dblp1, dblp2_6, ["s"], ["d"])
	j3 = Join(dblp1, dblp21, ["d"], ["s"])
	j4 = Join(dblp21, dblp26, ["s"], ["s"])
	j5 = Join(dblp26, dblp25, ["s"], ["d"])
	j6 = Join(dblp26, dblp2_4, ["d"], ["s"])
	j7 = Join(dblp2_4, dblp25, ["d"], ["s"])
	j8 = Join(dblp25, dblp2_7, ["s"], ["d"])
	j9 = Join(dblp2_6, dblp2_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_12():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_6 = Relation(name = "dblp17", alias = "dblp17_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_7 = Relation(name = "dblp17", alias = "dblp17_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp18_1, dblp21, dblp5, dblp17_4, dblp18_5, dblp17_6, dblp17_7]

	j0 = Join(dblp17_0, dblp21, ["s"], ["d"])
	j1 = Join(dblp17_0, dblp18_1, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp17_6, ["s"], ["d"])
	j3 = Join(dblp18_1, dblp21, ["d"], ["s"])
	j4 = Join(dblp21, dblp5, ["s"], ["s"])
	j5 = Join(dblp5, dblp18_5, ["s"], ["d"])
	j6 = Join(dblp5, dblp17_4, ["d"], ["s"])
	j7 = Join(dblp17_4, dblp18_5, ["d"], ["s"])
	j8 = Join(dblp18_5, dblp17_7, ["s"], ["d"])
	j9 = Join(dblp17_6, dblp17_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_5():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25_4 = Relation(name = "dblp25", alias = "dblp25_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1 = Relation(name = "dblp1", alias = "dblp1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp25_7 = Relation(name = "dblp25", alias = "dblp25_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp21, dblp2_2, dblp2_3, dblp25_4, dblp26, dblp1, dblp25_7]

	j0 = Join(dblp25_0, dblp2_2, ["s"], ["d"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp21, dblp1, ["s"], ["d"])
	j3 = Join(dblp21, dblp2_2, ["d"], ["s"])
	j4 = Join(dblp2_2, dblp2_3, ["s"], ["s"])
	j5 = Join(dblp2_3, dblp26, ["s"], ["d"])
	j6 = Join(dblp2_3, dblp25_4, ["d"], ["s"])
	j7 = Join(dblp25_4, dblp26, ["d"], ["s"])
	j8 = Join(dblp26, dblp25_7, ["s"], ["d"])
	j9 = Join(dblp1, dblp25_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_7():
	dblp10_0 = Relation(name = "dblp10", alias = "dblp10_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_1 = Relation(name = "dblp10", alias = "dblp10_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_2 = Relation(name = "dblp10", alias = "dblp10_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_3 = Relation(name = "dblp10", alias = "dblp10_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_4 = Relation(name = "dblp10", alias = "dblp10_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_5 = Relation(name = "dblp10", alias = "dblp10_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_6 = Relation(name = "dblp10", alias = "dblp10_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp10_7 = Relation(name = "dblp10", alias = "dblp10_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp10_0, dblp10_1, dblp10_2, dblp10_3, dblp10_4, dblp10_5, dblp10_6, dblp10_7]

	j0 = Join(dblp10_0, dblp10_2, ["s"], ["d"])
	j1 = Join(dblp10_0, dblp10_1, ["d"], ["s"])
	j2 = Join(dblp10_1, dblp10_6, ["s"], ["d"])
	j3 = Join(dblp10_1, dblp10_2, ["d"], ["s"])
	j4 = Join(dblp10_2, dblp10_3, ["s"], ["s"])
	j5 = Join(dblp10_3, dblp10_5, ["s"], ["d"])
	j6 = Join(dblp10_3, dblp10_4, ["d"], ["s"])
	j7 = Join(dblp10_4, dblp10_5, ["d"], ["s"])
	j8 = Join(dblp10_5, dblp10_7, ["s"], ["d"])
	j9 = Join(dblp10_6, dblp10_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_10():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_6 = Relation(name = "dblp17", alias = "dblp17_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_7 = Relation(name = "dblp17", alias = "dblp17_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp18_1, dblp5, dblp21, dblp17_4, dblp18_5, dblp17_6, dblp17_7]

	j0 = Join(dblp17_0, dblp5, ["s"], ["d"])
	j1 = Join(dblp17_0, dblp18_1, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp17_6, ["s"], ["d"])
	j3 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j4 = Join(dblp5, dblp21, ["s"], ["s"])
	j5 = Join(dblp21, dblp18_5, ["s"], ["d"])
	j6 = Join(dblp21, dblp17_4, ["d"], ["s"])
	j7 = Join(dblp17_4, dblp18_5, ["d"], ["s"])
	j8 = Join(dblp18_5, dblp17_7, ["s"], ["d"])
	j9 = Join(dblp17_6, dblp17_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_11():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_6 = Relation(name = "dblp17", alias = "dblp17_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_7 = Relation(name = "dblp17", alias = "dblp17_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp18_1, dblp21_2, dblp21_3, dblp17_4, dblp18_5, dblp17_6, dblp17_7]

	j0 = Join(dblp17_0, dblp21_2, ["s"], ["d"])
	j1 = Join(dblp17_0, dblp18_1, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp17_6, ["s"], ["d"])
	j3 = Join(dblp18_1, dblp21_2, ["d"], ["s"])
	j4 = Join(dblp21_2, dblp21_3, ["s"], ["s"])
	j5 = Join(dblp21_3, dblp18_5, ["s"], ["d"])
	j6 = Join(dblp21_3, dblp17_4, ["d"], ["s"])
	j7 = Join(dblp17_4, dblp18_5, ["d"], ["s"])
	j8 = Join(dblp18_5, dblp17_7, ["s"], ["d"])
	j9 = Join(dblp17_6, dblp17_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_6():
	dblp25 = Relation(name = "dblp25", alias = "dblp25", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1_4 = Relation(name = "dblp1", alias = "dblp1_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1_6 = Relation(name = "dblp1", alias = "dblp1_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp1_7 = Relation(name = "dblp1", alias = "dblp1_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp25, dblp21, dblp2_2, dblp2_3, dblp1_4, dblp26, dblp1_6, dblp1_7]

	j0 = Join(dblp25, dblp2_2, ["s"], ["d"])
	j1 = Join(dblp25, dblp21, ["d"], ["s"])
	j2 = Join(dblp21, dblp1_6, ["s"], ["d"])
	j3 = Join(dblp21, dblp2_2, ["d"], ["s"])
	j4 = Join(dblp2_2, dblp2_3, ["s"], ["s"])
	j5 = Join(dblp2_3, dblp26, ["s"], ["d"])
	j6 = Join(dblp2_3, dblp1_4, ["d"], ["s"])
	j7 = Join(dblp1_4, dblp26, ["d"], ["s"])
	j8 = Join(dblp26, dblp1_7, ["s"], ["d"])
	j9 = Join(dblp1_6, dblp1_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_8():
	dblp21_0 = Relation(name = "dblp21", alias = "dblp21_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_4 = Relation(name = "dblp21", alias = "dblp21_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_5 = Relation(name = "dblp2", alias = "dblp2_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp21_7 = Relation(name = "dblp21", alias = "dblp21_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp21_0, dblp2_1, dblp17_2, dblp17_3, dblp21_4, dblp2_5, dblp5, dblp21_7]

	j0 = Join(dblp21_0, dblp17_2, ["s"], ["d"])
	j1 = Join(dblp21_0, dblp2_1, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["s"], ["d"])
	j3 = Join(dblp2_1, dblp17_2, ["d"], ["s"])
	j4 = Join(dblp17_2, dblp17_3, ["s"], ["s"])
	j5 = Join(dblp17_3, dblp2_5, ["s"], ["d"])
	j6 = Join(dblp17_3, dblp21_4, ["d"], ["s"])
	j7 = Join(dblp21_4, dblp2_5, ["d"], ["s"])
	j8 = Join(dblp2_5, dblp21_7, ["s"], ["d"])
	j9 = Join(dblp5, dblp21_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_9():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_2 = Relation(name = "dblp5", alias = "dblp5_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp5_3 = Relation(name = "dblp5", alias = "dblp5_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_4 = Relation(name = "dblp2", alias = "dblp2_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp17_5 = Relation(name = "dblp17", alias = "dblp17_5", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_6 = Relation(name = "dblp2", alias = "dblp2_6", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	dblp2_7 = Relation(name = "dblp2", alias = "dblp2_7", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp17_1, dblp5_2, dblp5_3, dblp2_4, dblp17_5, dblp2_6, dblp2_7]

	j0 = Join(dblp2_0, dblp5_2, ["s"], ["d"])
	j1 = Join(dblp2_0, dblp17_1, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp2_6, ["s"], ["d"])
	j3 = Join(dblp17_1, dblp5_2, ["d"], ["s"])
	j4 = Join(dblp5_2, dblp5_3, ["s"], ["s"])
	j5 = Join(dblp5_3, dblp17_5, ["s"], ["d"])
	j6 = Join(dblp5_3, dblp2_4, ["d"], ["s"])
	j7 = Join(dblp2_4, dblp17_5, ["d"], ["s"])
	j8 = Join(dblp17_5, dblp2_7, ["s"], ["d"])
	j9 = Join(dblp2_6, dblp2_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q10_7():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp9_2, dblp9_3, dblp19, dblp20_5, dblp20_6]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp21, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp19, ["d"], ["s"])
	j5 = Join(dblp19, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp19, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_26():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp17_2, dblp17_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_32():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp2_2, dblp2_3, dblp9, dblp20_5, dblp20_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp9, ["d"], ["s"])
	j5 = Join(dblp9, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp9, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_33():
	dblp19_0 = Relation(name = "dblp19", alias = "dblp19_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_1 = Relation(name = "dblp19", alias = "dblp19_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_4 = Relation(name = "dblp19", alias = "dblp19_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19_0, dblp19_1, dblp9_2, dblp9_3, dblp19_4, dblp20_5, dblp20_6]

	j0 = Join(dblp19_0, dblp19_1, ["s"], ["s"])
	j1 = Join(dblp19_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp19_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp19_4, ["d"], ["s"])
	j5 = Join(dblp19_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp19_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_27():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp9_2, dblp9_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_6():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp8_2, dblp8_3, dblp17, dblp20_5, dblp20_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp17, ["d"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_4():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_2 = Relation(name = "dblp16", alias = "dblp16_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_3 = Relation(name = "dblp16", alias = "dblp16_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_4 = Relation(name = "dblp2", alias = "dblp2_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp16_2, dblp16_3, dblp2_4, dblp20_5, dblp20_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp16_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp16_3, ["d"], ["s"])
	j3 = Join(dblp16_2, dblp16_3, ["d"], ["d"])
	j4 = Join(dblp16_3, dblp2_4, ["d"], ["s"])
	j5 = Join(dblp2_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_31():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp2_2, dblp2_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_25():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp21_2, dblp21_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	j4 = Join(dblp21_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_19():
	dblp26_0 = Relation(name = "dblp26", alias = "dblp26_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_1 = Relation(name = "dblp26", alias = "dblp26_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26_0, dblp26_1, dblp5, dblp21, dblp17, dblp20_5, dblp20_6]

	j0 = Join(dblp26_0, dblp26_1, ["s"], ["s"])
	j1 = Join(dblp26_0, dblp5, ["d"], ["s"])
	j2 = Join(dblp26_1, dblp21, ["d"], ["s"])
	j3 = Join(dblp5, dblp21, ["d"], ["d"])
	j4 = Join(dblp21, dblp17, ["d"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_18():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp2_2, dblp2_3, dblp9, dblp20_5, dblp20_6]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp9, ["d"], ["s"])
	j5 = Join(dblp9, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp9, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_24():
	dblp19_0 = Relation(name = "dblp19", alias = "dblp19_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_1 = Relation(name = "dblp19", alias = "dblp19_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19_0, dblp19_1, dblp9_2, dblp9_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp19_0, dblp19_1, ["s"], ["s"])
	j1 = Join(dblp19_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp19_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_30():
	dblp19_0 = Relation(name = "dblp19", alias = "dblp19_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_1 = Relation(name = "dblp19", alias = "dblp19_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_4 = Relation(name = "dblp2", alias = "dblp2_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp19_0, dblp19_1, dblp2_2, dblp2_3, dblp2_4, dblp20_5, dblp20_6]

	j0 = Join(dblp19_0, dblp19_1, ["s"], ["s"])
	j1 = Join(dblp19_0, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp19_1, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp2_4, ["d"], ["s"])
	j5 = Join(dblp2_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_5():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_4 = Relation(name = "dblp2", alias = "dblp2_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp17_2, dblp17_3, dblp2_4, dblp20_5, dblp20_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp2_4, ["d"], ["s"])
	j5 = Join(dblp2_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_1():
	dblp23_0 = Relation(name = "dblp23", alias = "dblp23_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_1 = Relation(name = "dblp23", alias = "dblp23_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_2 = Relation(name = "dblp26", alias = "dblp26_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_3 = Relation(name = "dblp26", alias = "dblp26_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp23_0, dblp23_1, dblp26_2, dblp26_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp23_0, dblp23_1, ["s"], ["s"])
	j1 = Join(dblp23_0, dblp26_2, ["d"], ["s"])
	j2 = Join(dblp23_1, dblp26_3, ["d"], ["s"])
	j3 = Join(dblp26_2, dblp26_3, ["d"], ["d"])
	j4 = Join(dblp26_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_34():
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19 = Relation(name = "dblp19", alias = "dblp19", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp21, dblp5, dblp2_2, dblp2_3, dblp19, dblp20_5, dblp20_6]

	j0 = Join(dblp21, dblp5, ["s"], ["s"])
	j1 = Join(dblp21, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp5, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp19, ["d"], ["s"])
	j5 = Join(dblp19, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp19, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_20():
	dblp25_0 = Relation(name = "dblp25", alias = "dblp25_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp25_1 = Relation(name = "dblp25", alias = "dblp25_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_6 = Relation(name = "dblp18", alias = "dblp18_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp25_0, dblp25_1, dblp21, dblp26, dblp9, dblp18_5, dblp18_6]

	j0 = Join(dblp25_0, dblp25_1, ["s"], ["s"])
	j1 = Join(dblp25_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp25_1, dblp26, ["d"], ["s"])
	j3 = Join(dblp21, dblp26, ["d"], ["d"])
	j4 = Join(dblp26, dblp9, ["d"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["s"], ["s"])
	j6 = Join(dblp9, dblp18_6, ["d"], ["s"])
	j7 = Join(dblp18_5, dblp18_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_21():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_35():
	dblp26 = Relation(name = "dblp26", alias = "dblp26", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_6 = Relation(name = "dblp18", alias = "dblp18_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp26, dblp21, dblp8_2, dblp8_3, dblp9, dblp18_5, dblp18_6]

	j0 = Join(dblp26, dblp21, ["s"], ["s"])
	j1 = Join(dblp26, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp21, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp9, ["d"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["s"], ["s"])
	j6 = Join(dblp9, dblp18_6, ["d"], ["s"])
	j7 = Join(dblp18_5, dblp18_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_2():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp9_2, dblp9_3, dblp8_4, dblp20_5, dblp20_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp8_4, ["d"], ["s"])
	j5 = Join(dblp8_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_23():
	dblp23_0 = Relation(name = "dblp23", alias = "dblp23_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_1 = Relation(name = "dblp23", alias = "dblp23_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_2 = Relation(name = "dblp26", alias = "dblp26_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp26_3 = Relation(name = "dblp26", alias = "dblp26_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17 = Relation(name = "dblp17", alias = "dblp17", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp23_0, dblp23_1, dblp26_2, dblp26_3, dblp17, dblp20_5, dblp20_6]

	j0 = Join(dblp23_0, dblp23_1, ["s"], ["s"])
	j1 = Join(dblp23_0, dblp26_2, ["d"], ["s"])
	j2 = Join(dblp23_1, dblp26_3, ["d"], ["s"])
	j3 = Join(dblp26_2, dblp26_3, ["d"], ["d"])
	j4 = Join(dblp26_3, dblp17, ["d"], ["s"])
	j5 = Join(dblp17, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_37():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp17_2, dblp17_3, dblp17_4, dblp20_5, dblp20_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp17_4, ["d"], ["s"])
	j5 = Join(dblp17_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_36():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp8_2, dblp8_3, dblp8_4, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp8_4, ["d"], ["s"])
	j5 = Join(dblp8_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_22():
	dblp16_0 = Relation(name = "dblp16", alias = "dblp16_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp16_1 = Relation(name = "dblp16", alias = "dblp16_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp16_0, dblp16_1, dblp9_2, dblp9_3, dblp5, dblp20_5, dblp20_6]

	j0 = Join(dblp16_0, dblp16_1, ["s"], ["s"])
	j1 = Join(dblp16_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp16_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp5, ["d"], ["s"])
	j5 = Join(dblp5, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp5, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_3():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp8_2, dblp8_3, dblp8_4, dblp20_5, dblp20_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp8_4, ["d"], ["s"])
	j5 = Join(dblp8_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_40():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_5 = Relation(name = "dblp8", alias = "dblp8_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_6 = Relation(name = "dblp8", alias = "dblp8_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp21, dblp5, dblp8_4, dblp8_5, dblp8_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	j4 = Join(dblp5, dblp8_4, ["d"], ["s"])
	j5 = Join(dblp8_4, dblp8_5, ["s"], ["s"])
	j6 = Join(dblp8_4, dblp8_6, ["d"], ["s"])
	j7 = Join(dblp8_5, dblp8_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_13():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp10 = Relation(name = "dblp10", alias = "dblp10", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp17_2, dblp17_3, dblp10, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp10, ["d"], ["s"])
	j5 = Join(dblp10, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp10, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_12():
	dblp23_0 = Relation(name = "dblp23", alias = "dblp23_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp23_1 = Relation(name = "dblp23", alias = "dblp23_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_2 = Relation(name = "dblp21", alias = "dblp21_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21_3 = Relation(name = "dblp21", alias = "dblp21_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp23_0, dblp23_1, dblp21_2, dblp21_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp23_0, dblp23_1, ["s"], ["s"])
	j1 = Join(dblp23_0, dblp21_2, ["d"], ["s"])
	j2 = Join(dblp23_1, dblp21_3, ["d"], ["s"])
	j3 = Join(dblp21_2, dblp21_3, ["d"], ["d"])
	j4 = Join(dblp21_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_10():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_4 = Relation(name = "dblp9", alias = "dblp9_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_6 = Relation(name = "dblp18", alias = "dblp18_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp21, dblp5, dblp9_4, dblp18_5, dblp18_6]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	j4 = Join(dblp5, dblp9_4, ["d"], ["s"])
	j5 = Join(dblp9_4, dblp18_5, ["s"], ["s"])
	j6 = Join(dblp9_4, dblp18_6, ["d"], ["s"])
	j7 = Join(dblp18_5, dblp18_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_38():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_4 = Relation(name = "dblp8", alias = "dblp8_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_5 = Relation(name = "dblp8", alias = "dblp8_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_6 = Relation(name = "dblp8", alias = "dblp8_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp17_2, dblp17_3, dblp8_4, dblp8_5, dblp8_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp8_4, ["d"], ["s"])
	j5 = Join(dblp8_4, dblp8_5, ["s"], ["s"])
	j6 = Join(dblp8_4, dblp8_6, ["d"], ["s"])
	j7 = Join(dblp8_5, dblp8_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_39():
	dblp2_0 = Relation(name = "dblp2", alias = "dblp2_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_1 = Relation(name = "dblp2", alias = "dblp2_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9 = Relation(name = "dblp9", alias = "dblp9", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_5 = Relation(name = "dblp18", alias = "dblp18_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_6 = Relation(name = "dblp18", alias = "dblp18_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp2_0, dblp2_1, dblp17_2, dblp17_3, dblp9, dblp18_5, dblp18_6]

	j0 = Join(dblp2_0, dblp2_1, ["s"], ["s"])
	j1 = Join(dblp2_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp2_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp9, ["d"], ["s"])
	j5 = Join(dblp9, dblp18_5, ["s"], ["s"])
	j6 = Join(dblp9, dblp18_6, ["d"], ["s"])
	j7 = Join(dblp18_5, dblp18_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_11():
	dblp18_0 = Relation(name = "dblp18", alias = "dblp18_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp18_1 = Relation(name = "dblp18", alias = "dblp18_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp21 = Relation(name = "dblp21", alias = "dblp21", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp5 = Relation(name = "dblp5", alias = "dblp5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp18_0, dblp18_1, dblp21, dblp5, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp18_0, dblp18_1, ["s"], ["s"])
	j1 = Join(dblp18_0, dblp21, ["d"], ["s"])
	j2 = Join(dblp18_1, dblp5, ["d"], ["s"])
	j3 = Join(dblp21, dblp5, ["d"], ["d"])
	j4 = Join(dblp5, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_8():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_2 = Relation(name = "dblp2", alias = "dblp2_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2_3 = Relation(name = "dblp2", alias = "dblp2_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp2_2, dblp2_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp2_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp2_3, ["d"], ["s"])
	j3 = Join(dblp2_2, dblp2_3, ["d"], ["d"])
	j4 = Join(dblp2_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_29():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp17_2, dblp17_3, dblp17_4, dblp20_5, dblp20_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp17_4, ["d"], ["s"])
	j5 = Join(dblp17_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_15():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp17_2, dblp17_3, dblp17_4, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp17_4, ["d"], ["s"])
	j5 = Join(dblp17_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_14():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_2 = Relation(name = "dblp9", alias = "dblp9_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_3 = Relation(name = "dblp9", alias = "dblp9_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8 = Relation(name = "dblp8", alias = "dblp8", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp9_2, dblp9_3, dblp8, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp9_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp9_3, ["d"], ["s"])
	j3 = Join(dblp9_2, dblp9_3, ["d"], ["d"])
	j4 = Join(dblp9_3, dblp8, ["d"], ["s"])
	j5 = Join(dblp8, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp8, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_28():
	dblp8_0 = Relation(name = "dblp8", alias = "dblp8_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_1 = Relation(name = "dblp8", alias = "dblp8_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_2 = Relation(name = "dblp17", alias = "dblp17_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_3 = Relation(name = "dblp17", alias = "dblp17_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp8_0, dblp8_1, dblp17_2, dblp17_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp8_0, dblp8_1, ["s"], ["s"])
	j1 = Join(dblp8_0, dblp17_2, ["d"], ["s"])
	j2 = Join(dblp8_1, dblp17_3, ["d"], ["s"])
	j3 = Join(dblp17_2, dblp17_3, ["d"], ["d"])
	j4 = Join(dblp17_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_9():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp8_2, dblp8_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_16():
	dblp9_0 = Relation(name = "dblp9", alias = "dblp9_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp9_1 = Relation(name = "dblp9", alias = "dblp9_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_2 = Relation(name = "dblp19", alias = "dblp19_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp19_3 = Relation(name = "dblp19", alias = "dblp19_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp2 = Relation(name = "dblp2", alias = "dblp2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp9_0, dblp9_1, dblp19_2, dblp19_3, dblp2, dblp20_5, dblp20_6]

	j0 = Join(dblp9_0, dblp9_1, ["s"], ["s"])
	j1 = Join(dblp9_0, dblp19_2, ["d"], ["s"])
	j2 = Join(dblp9_1, dblp19_3, ["d"], ["s"])
	j3 = Join(dblp19_2, dblp19_3, ["d"], ["d"])
	j4 = Join(dblp19_3, dblp2, ["d"], ["s"])
	j5 = Join(dblp2, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp2, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q10_17():
	dblp17_0 = Relation(name = "dblp17", alias = "dblp17_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_1 = Relation(name = "dblp17", alias = "dblp17_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_2 = Relation(name = "dblp8", alias = "dblp8_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp8_3 = Relation(name = "dblp8", alias = "dblp8_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp17_4 = Relation(name = "dblp17", alias = "dblp17_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_5 = Relation(name = "dblp20", alias = "dblp20_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	dblp20_6 = Relation(name = "dblp20", alias = "dblp20_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [dblp17_0, dblp17_1, dblp8_2, dblp8_3, dblp17_4, dblp20_5, dblp20_6]

	j0 = Join(dblp17_0, dblp17_1, ["s"], ["s"])
	j1 = Join(dblp17_0, dblp8_2, ["d"], ["s"])
	j2 = Join(dblp17_1, dblp8_3, ["d"], ["s"])
	j3 = Join(dblp8_2, dblp8_3, ["d"], ["d"])
	j4 = Join(dblp8_3, dblp17_4, ["d"], ["s"])
	j5 = Join(dblp17_4, dblp20_5, ["s"], ["s"])
	j6 = Join(dblp17_4, dblp20_6, ["d"], ["s"])
	j7 = Join(dblp20_5, dblp20_6, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_25():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_19():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_18():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_24():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45160_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_20():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_21():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45173, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160, hetio45173, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_9():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_23():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_3 = Relation(name = "hetio45173", alias = "hetio45173_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_4 = Relation(name = "hetio45173", alias = "hetio45173_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45173_3, hetio45173_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45173_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45173_4, ["d"], ["s"])
	j5 = Join(hetio45173_3, hetio45173_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_22():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_8():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_5():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_13():
	hetio45161 = Relation(name = "hetio45161", alias = "hetio45161", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45166_1 = Relation(name = "hetio45166", alias = "hetio45166_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45166_2 = Relation(name = "hetio45166", alias = "hetio45166_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45167 = Relation(name = "hetio45167", alias = "hetio45167", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161, hetio45166_1, hetio45166_2, hetio45167, hetio45177]

	j0 = Join(hetio45161, hetio45166_1, ["s"], ["s"])
	j1 = Join(hetio45161, hetio45166_2, ["d"], ["s"])
	j2 = Join(hetio45166_2, hetio45167, ["s"], ["s"])
	j3 = Join(hetio45166_1, hetio45166_2, ["d"], ["d"])
	j4 = Join(hetio45166_2, hetio45177, ["d"], ["s"])
	j5 = Join(hetio45167, hetio45177, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_12():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_4():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_3 = Relation(name = "hetio45176", alias = "hetio45176_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45176_3, hetio45176_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45176_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45176_4, ["d"], ["s"])
	j5 = Join(hetio45176_3, hetio45176_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_6():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45177_2, hetio45160_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_10():
	hetio45161_0 = Relation(name = "hetio45161", alias = "hetio45161_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_1 = Relation(name = "hetio45161", alias = "hetio45161_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_2 = Relation(name = "hetio45161", alias = "hetio45161_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_3 = Relation(name = "hetio45161", alias = "hetio45161_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_4 = Relation(name = "hetio45161", alias = "hetio45161_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161_0, hetio45161_1, hetio45161_2, hetio45161_3, hetio45161_4]

	j0 = Join(hetio45161_0, hetio45161_1, ["s"], ["s"])
	j1 = Join(hetio45161_0, hetio45161_2, ["d"], ["s"])
	j2 = Join(hetio45161_2, hetio45161_3, ["s"], ["s"])
	j3 = Join(hetio45161_1, hetio45161_2, ["d"], ["d"])
	j4 = Join(hetio45161_2, hetio45161_4, ["d"], ["s"])
	j5 = Join(hetio45161_3, hetio45161_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_11():
	hetio45166 = Relation(name = "hetio45166", alias = "hetio45166", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45167 = Relation(name = "hetio45167", alias = "hetio45167", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45166, hetio45167, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45166, hetio45167, ["s"], ["s"])
	j1 = Join(hetio45166, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45167, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_7():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_3():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45177_1, hetio45177_2, hetio45160_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_15():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_14():
	hetio45178_0 = Relation(name = "hetio45178", alias = "hetio45178_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45178_1 = Relation(name = "hetio45178", alias = "hetio45178_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45178_0, hetio45178_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45178_0, hetio45178_1, ["s"], ["s"])
	j1 = Join(hetio45178_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45178_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_2():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_16():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_3 = Relation(name = "hetio45176", alias = "hetio45176_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45176_3, hetio45176_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45176_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45176_4, ["d"], ["s"])
	j5 = Join(hetio45176_3, hetio45176_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_17():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45160]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45160, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45160, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_hetio_cyclic_q4_1():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_25():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_19():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_18():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_24():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45160_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_20():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_21():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45173, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160, hetio45173, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_9():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_23():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_3 = Relation(name = "hetio45173", alias = "hetio45173_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_4 = Relation(name = "hetio45173", alias = "hetio45173_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45173_3, hetio45173_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45173_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45173_4, ["d"], ["s"])
	j5 = Join(hetio45173_3, hetio45173_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_22():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_8():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_3 = Relation(name = "hetio45180", alias = "hetio45180_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45180_3, hetio45180_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45180_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45180_4, ["d"], ["s"])
	j5 = Join(hetio45180_3, hetio45180_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_5():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_13():
	hetio45161 = Relation(name = "hetio45161", alias = "hetio45161", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45166_1 = Relation(name = "hetio45166", alias = "hetio45166_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45166_2 = Relation(name = "hetio45166", alias = "hetio45166_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45167 = Relation(name = "hetio45167", alias = "hetio45167", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161, hetio45166_1, hetio45166_2, hetio45167, hetio45177]

	j0 = Join(hetio45161, hetio45166_1, ["s"], ["s"])
	j1 = Join(hetio45161, hetio45166_2, ["d"], ["s"])
	j2 = Join(hetio45166_2, hetio45167, ["s"], ["s"])
	j3 = Join(hetio45166_1, hetio45166_2, ["d"], ["d"])
	j4 = Join(hetio45166_2, hetio45177, ["d"], ["s"])
	j5 = Join(hetio45167, hetio45177, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_12():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_4():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_3 = Relation(name = "hetio45176", alias = "hetio45176_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45176_3, hetio45176_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45176_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45176_4, ["d"], ["s"])
	j5 = Join(hetio45176_3, hetio45176_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_6():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45177_2, hetio45160_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_10():
	hetio45161_0 = Relation(name = "hetio45161", alias = "hetio45161_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_1 = Relation(name = "hetio45161", alias = "hetio45161_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_2 = Relation(name = "hetio45161", alias = "hetio45161_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_3 = Relation(name = "hetio45161", alias = "hetio45161_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_4 = Relation(name = "hetio45161", alias = "hetio45161_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161_0, hetio45161_1, hetio45161_2, hetio45161_3, hetio45161_4]

	j0 = Join(hetio45161_0, hetio45161_1, ["s"], ["s"])
	j1 = Join(hetio45161_0, hetio45161_2, ["d"], ["s"])
	j2 = Join(hetio45161_2, hetio45161_3, ["s"], ["s"])
	j3 = Join(hetio45161_1, hetio45161_2, ["d"], ["d"])
	j4 = Join(hetio45161_2, hetio45161_4, ["d"], ["s"])
	j5 = Join(hetio45161_3, hetio45161_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_11():
	hetio45166 = Relation(name = "hetio45166", alias = "hetio45166", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45167 = Relation(name = "hetio45167", alias = "hetio45167", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45166, hetio45167, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45166, hetio45167, ["s"], ["s"])
	j1 = Join(hetio45166, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45167, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_7():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_3 = Relation(name = "hetio45159", alias = "hetio45159_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45177, hetio45159_3, hetio45159_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45177, ["d"], ["s"])
	j2 = Join(hetio45177, hetio45159_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45177, ["d"], ["d"])
	j4 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	j5 = Join(hetio45159_3, hetio45159_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_3():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45177_1, hetio45177_2, hetio45160_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_15():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_14():
	hetio45178_0 = Relation(name = "hetio45178", alias = "hetio45178_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45178_1 = Relation(name = "hetio45178", alias = "hetio45178_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45178_0, hetio45178_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45178_0, hetio45178_1, ["s"], ["s"])
	j1 = Join(hetio45178_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45178_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_2():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45160_4, ["d"], ["s"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_16():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_3 = Relation(name = "hetio45176", alias = "hetio45176_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45176_3, hetio45176_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45176_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45176_4, ["d"], ["s"])
	j5 = Join(hetio45176_3, hetio45176_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_17():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45160]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45160, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45160, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_1():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["s"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_11():
	hetio45166 = Relation(name = "hetio45166", alias = "hetio45166", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45167 = Relation(name = "hetio45167", alias = "hetio45167", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45166, hetio45167, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45166, hetio45167, ["s"], ["s"])
	j1 = Join(hetio45166, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45167, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_10():
	hetio45161_0 = Relation(name = "hetio45161", alias = "hetio45161_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_1 = Relation(name = "hetio45161", alias = "hetio45161_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_2 = Relation(name = "hetio45161", alias = "hetio45161_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_3 = Relation(name = "hetio45161", alias = "hetio45161_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_4 = Relation(name = "hetio45161", alias = "hetio45161_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161_0, hetio45161_1, hetio45161_2, hetio45161_3, hetio45161_4]

	j0 = Join(hetio45161_0, hetio45161_1, ["s"], ["s"])
	j1 = Join(hetio45161_0, hetio45161_2, ["d"], ["s"])
	j2 = Join(hetio45161_2, hetio45161_3, ["s"], ["s"])
	j3 = Join(hetio45161_1, hetio45161_2, ["d"], ["d"])
	j4 = Join(hetio45161_2, hetio45161_4, ["d"], ["d"])
	j5 = Join(hetio45161_3, hetio45161_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_12():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_1 = Relation(name = "hetio45159", alias = "hetio45159_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_2 = Relation(name = "hetio45159", alias = "hetio45159_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45159_1, hetio45159_2, hetio45173, hetio45159_4]

	j0 = Join(hetio45160, hetio45159_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45159_2, ["d"], ["s"])
	j2 = Join(hetio45159_2, hetio45173, ["s"], ["s"])
	j3 = Join(hetio45159_1, hetio45159_2, ["d"], ["d"])
	j4 = Join(hetio45159_2, hetio45159_4, ["d"], ["d"])
	j5 = Join(hetio45173, hetio45159_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_13():
	hetio45161_0 = Relation(name = "hetio45161", alias = "hetio45161_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45181_1 = Relation(name = "hetio45181", alias = "hetio45181_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45181_2 = Relation(name = "hetio45181", alias = "hetio45181_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_3 = Relation(name = "hetio45161", alias = "hetio45161_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45181_4 = Relation(name = "hetio45181", alias = "hetio45181_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45161_0, hetio45181_1, hetio45181_2, hetio45161_3, hetio45181_4]

	j0 = Join(hetio45161_0, hetio45181_1, ["s"], ["s"])
	j1 = Join(hetio45161_0, hetio45181_2, ["d"], ["s"])
	j2 = Join(hetio45181_2, hetio45161_3, ["s"], ["s"])
	j3 = Join(hetio45181_1, hetio45181_2, ["d"], ["d"])
	j4 = Join(hetio45181_2, hetio45181_4, ["d"], ["d"])
	j5 = Join(hetio45161_3, hetio45181_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_17():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_1 = Relation(name = "hetio45159", alias = "hetio45159_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_2 = Relation(name = "hetio45159", alias = "hetio45159_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45159_1, hetio45159_2, hetio45177_3, hetio45159_4]

	j0 = Join(hetio45177_0, hetio45159_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45159_2, ["d"], ["s"])
	j2 = Join(hetio45159_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45159_1, hetio45159_2, ["d"], ["d"])
	j4 = Join(hetio45159_2, hetio45159_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45159_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_9():
	hetio45173_0 = Relation(name = "hetio45173", alias = "hetio45173_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_1 = Relation(name = "hetio45173", alias = "hetio45173_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_2 = Relation(name = "hetio45173", alias = "hetio45173_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_3 = Relation(name = "hetio45173", alias = "hetio45173_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173_4 = Relation(name = "hetio45173", alias = "hetio45173_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173_0, hetio45173_1, hetio45173_2, hetio45173_3, hetio45173_4]

	j0 = Join(hetio45173_0, hetio45173_1, ["s"], ["s"])
	j1 = Join(hetio45173_0, hetio45173_2, ["d"], ["s"])
	j2 = Join(hetio45173_2, hetio45173_3, ["s"], ["s"])
	j3 = Join(hetio45173_1, hetio45173_2, ["d"], ["d"])
	j4 = Join(hetio45173_2, hetio45173_4, ["d"], ["d"])
	j5 = Join(hetio45173_3, hetio45173_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_8():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_16():
	hetio45175_0 = Relation(name = "hetio45175", alias = "hetio45175_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45175_1 = Relation(name = "hetio45175", alias = "hetio45175_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_2 = Relation(name = "hetio45161", alias = "hetio45161_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_3 = Relation(name = "hetio45161", alias = "hetio45161_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45161_4 = Relation(name = "hetio45161", alias = "hetio45161_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45175_0, hetio45175_1, hetio45161_2, hetio45161_3, hetio45161_4]

	j0 = Join(hetio45175_0, hetio45175_1, ["s"], ["s"])
	j1 = Join(hetio45175_0, hetio45161_2, ["d"], ["s"])
	j2 = Join(hetio45161_2, hetio45161_3, ["s"], ["s"])
	j3 = Join(hetio45175_1, hetio45161_2, ["d"], ["d"])
	j4 = Join(hetio45161_2, hetio45161_4, ["d"], ["d"])
	j5 = Join(hetio45161_3, hetio45161_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_14():
	hetio45178_0 = Relation(name = "hetio45178", alias = "hetio45178_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45178_1 = Relation(name = "hetio45178", alias = "hetio45178_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45178_0, hetio45178_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45178_0, hetio45178_1, ["s"], ["s"])
	j1 = Join(hetio45178_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45178_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_15():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45160, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_18():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45160_3, hetio45160_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["d"])
	j5 = Join(hetio45160_3, hetio45160_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_24():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45160]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45160, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45160, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_6():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_1 = Relation(name = "hetio45160", alias = "hetio45160_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_2 = Relation(name = "hetio45160", alias = "hetio45160_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_4 = Relation(name = "hetio45160", alias = "hetio45160_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45160_1, hetio45160_2, hetio45177, hetio45160_4]

	j0 = Join(hetio45160_0, hetio45160_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45160_2, ["d"], ["s"])
	j2 = Join(hetio45160_2, hetio45177, ["s"], ["s"])
	j3 = Join(hetio45160_1, hetio45160_2, ["d"], ["d"])
	j4 = Join(hetio45160_2, hetio45160_4, ["d"], ["d"])
	j5 = Join(hetio45177, hetio45160_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_7():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_1 = Relation(name = "hetio45176", alias = "hetio45176_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_2 = Relation(name = "hetio45176", alias = "hetio45176_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45176_1, hetio45176_2, hetio45173, hetio45176_4]

	j0 = Join(hetio45160, hetio45176_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45176_2, ["d"], ["s"])
	j2 = Join(hetio45176_2, hetio45173, ["s"], ["s"])
	j3 = Join(hetio45176_1, hetio45176_2, ["d"], ["d"])
	j4 = Join(hetio45176_2, hetio45176_4, ["d"], ["d"])
	j5 = Join(hetio45173, hetio45176_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_19():
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_1 = Relation(name = "hetio45159", alias = "hetio45159_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_2 = Relation(name = "hetio45159", alias = "hetio45159_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173, hetio45159_1, hetio45159_2, hetio45160, hetio45159_4]

	j0 = Join(hetio45173, hetio45159_1, ["s"], ["s"])
	j1 = Join(hetio45173, hetio45159_2, ["d"], ["s"])
	j2 = Join(hetio45159_2, hetio45160, ["s"], ["s"])
	j3 = Join(hetio45159_1, hetio45159_2, ["d"], ["d"])
	j4 = Join(hetio45159_2, hetio45159_4, ["d"], ["d"])
	j5 = Join(hetio45160, hetio45159_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_5():
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_1 = Relation(name = "hetio45180", alias = "hetio45180_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_2 = Relation(name = "hetio45180", alias = "hetio45180_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173, hetio45180_1, hetio45180_2, hetio45160, hetio45180_4]

	j0 = Join(hetio45173, hetio45180_1, ["s"], ["s"])
	j1 = Join(hetio45173, hetio45180_2, ["d"], ["s"])
	j2 = Join(hetio45180_2, hetio45160, ["s"], ["s"])
	j3 = Join(hetio45180_1, hetio45180_2, ["d"], ["d"])
	j4 = Join(hetio45180_2, hetio45180_4, ["d"], ["d"])
	j5 = Join(hetio45160, hetio45180_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_4():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45160, hetio45177_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45160, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45160, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_22():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_1 = Relation(name = "hetio45176", alias = "hetio45176_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_2 = Relation(name = "hetio45176", alias = "hetio45176_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45176_1, hetio45176_2, hetio45160_3, hetio45176_4]

	j0 = Join(hetio45160_0, hetio45176_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45176_2, ["d"], ["s"])
	j2 = Join(hetio45176_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45176_1, hetio45176_2, ["d"], ["d"])
	j4 = Join(hetio45176_2, hetio45176_4, ["d"], ["d"])
	j5 = Join(hetio45160_3, hetio45176_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_1():
	hetio45177_0 = Relation(name = "hetio45177", alias = "hetio45177_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_1 = Relation(name = "hetio45177", alias = "hetio45177_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_2 = Relation(name = "hetio45177", alias = "hetio45177_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_3 = Relation(name = "hetio45177", alias = "hetio45177_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177_4 = Relation(name = "hetio45177", alias = "hetio45177_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45177_0, hetio45177_1, hetio45177_2, hetio45177_3, hetio45177_4]

	j0 = Join(hetio45177_0, hetio45177_1, ["s"], ["s"])
	j1 = Join(hetio45177_0, hetio45177_2, ["d"], ["s"])
	j2 = Join(hetio45177_2, hetio45177_3, ["s"], ["s"])
	j3 = Join(hetio45177_1, hetio45177_2, ["d"], ["d"])
	j4 = Join(hetio45177_2, hetio45177_4, ["d"], ["d"])
	j5 = Join(hetio45177_3, hetio45177_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_23():
	hetio45173 = Relation(name = "hetio45173", alias = "hetio45173", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_1 = Relation(name = "hetio45176", alias = "hetio45176_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_2 = Relation(name = "hetio45176", alias = "hetio45176_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45176_4 = Relation(name = "hetio45176", alias = "hetio45176_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45173, hetio45176_1, hetio45176_2, hetio45160, hetio45176_4]

	j0 = Join(hetio45173, hetio45176_1, ["s"], ["s"])
	j1 = Join(hetio45173, hetio45176_2, ["d"], ["s"])
	j2 = Join(hetio45176_2, hetio45160, ["s"], ["s"])
	j3 = Join(hetio45176_1, hetio45176_2, ["d"], ["d"])
	j4 = Join(hetio45176_2, hetio45176_4, ["d"], ["d"])
	j5 = Join(hetio45160, hetio45176_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_21():
	hetio45160 = Relation(name = "hetio45160", alias = "hetio45160", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_1 = Relation(name = "hetio45159", alias = "hetio45159_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_2 = Relation(name = "hetio45159", alias = "hetio45159_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45177 = Relation(name = "hetio45177", alias = "hetio45177", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160, hetio45159_1, hetio45159_2, hetio45177, hetio45159_4]

	j0 = Join(hetio45160, hetio45159_1, ["s"], ["s"])
	j1 = Join(hetio45160, hetio45159_2, ["d"], ["s"])
	j2 = Join(hetio45159_2, hetio45177, ["s"], ["s"])
	j3 = Join(hetio45159_1, hetio45159_2, ["d"], ["d"])
	j4 = Join(hetio45159_2, hetio45159_4, ["d"], ["d"])
	j5 = Join(hetio45177, hetio45159_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_3():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45174_1 = Relation(name = "hetio45174", alias = "hetio45174_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45174_2 = Relation(name = "hetio45174", alias = "hetio45174_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45174_4 = Relation(name = "hetio45174", alias = "hetio45174_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45174_1, hetio45174_2, hetio45160_3, hetio45174_4]

	j0 = Join(hetio45160_0, hetio45174_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45174_2, ["d"], ["s"])
	j2 = Join(hetio45174_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45174_1, hetio45174_2, ["d"], ["d"])
	j4 = Join(hetio45174_2, hetio45174_4, ["d"], ["d"])
	j5 = Join(hetio45160_3, hetio45174_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_2():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_1 = Relation(name = "hetio45180", alias = "hetio45180_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_2 = Relation(name = "hetio45180", alias = "hetio45180_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45180_4 = Relation(name = "hetio45180", alias = "hetio45180_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45180_1, hetio45180_2, hetio45160_3, hetio45180_4]

	j0 = Join(hetio45160_0, hetio45180_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45180_2, ["d"], ["s"])
	j2 = Join(hetio45180_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45180_1, hetio45180_2, ["d"], ["d"])
	j4 = Join(hetio45180_2, hetio45180_4, ["d"], ["d"])
	j5 = Join(hetio45160_3, hetio45180_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q5_20():
	hetio45160_0 = Relation(name = "hetio45160", alias = "hetio45160_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_1 = Relation(name = "hetio45159", alias = "hetio45159_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_2 = Relation(name = "hetio45159", alias = "hetio45159_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45160_3 = Relation(name = "hetio45160", alias = "hetio45160_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	hetio45159_4 = Relation(name = "hetio45159", alias = "hetio45159_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [hetio45160_0, hetio45159_1, hetio45159_2, hetio45160_3, hetio45159_4]

	j0 = Join(hetio45160_0, hetio45159_1, ["s"], ["s"])
	j1 = Join(hetio45160_0, hetio45159_2, ["d"], ["s"])
	j2 = Join(hetio45159_2, hetio45160_3, ["s"], ["s"])
	j3 = Join(hetio45159_1, hetio45159_2, ["d"], ["d"])
	j4 = Join(hetio45159_2, hetio45159_4, ["d"], ["d"])
	j5 = Join(hetio45160_3, hetio45159_4, ["d"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_5():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052644, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052651_0, watdiv1052651_1, ["s"], ["s"])
	j1 = Join(watdiv1052651_0, watdiv1052644, ["d"], ["s"])
	j2 = Join(watdiv1052644, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052651_1, watdiv1052644, ["d"], ["d"])
	j4 = Join(watdiv1052644, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_4():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052651_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052651_0, watdiv1052651_1, ["s"], ["s"])
	j1 = Join(watdiv1052651_0, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_6():
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644, watdiv1052651_1, watdiv1052651_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052644, watdiv1052651_1, ["s"], ["s"])
	j1 = Join(watdiv1052644, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_7():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052648_3 = Relation(name = "watdiv1052648", alias = "watdiv1052648_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052648_4 = Relation(name = "watdiv1052648", alias = "watdiv1052648_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052644_2, watdiv1052648_3, watdiv1052648_4]

	j0 = Join(watdiv1052644_0, watdiv1052644_1, ["s"], ["s"])
	j1 = Join(watdiv1052644_0, watdiv1052644_2, ["d"], ["s"])
	j2 = Join(watdiv1052644_2, watdiv1052648_3, ["s"], ["s"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["d"])
	j4 = Join(watdiv1052644_2, watdiv1052648_4, ["d"], ["s"])
	j5 = Join(watdiv1052648_3, watdiv1052648_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_3():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052644_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052644_0, watdiv1052644_1, ["s"], ["s"])
	j1 = Join(watdiv1052644_0, watdiv1052644_2, ["d"], ["s"])
	j2 = Join(watdiv1052644_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["d"])
	j4 = Join(watdiv1052644_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_2():
	watdiv1052608 = Relation(name = "watdiv1052608", alias = "watdiv1052608", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052593 = Relation(name = "watdiv1052593", alias = "watdiv1052593", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608, watdiv1052593, watdiv1052644, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052608, watdiv1052593, ["s"], ["s"])
	j1 = Join(watdiv1052608, watdiv1052644, ["d"], ["s"])
	j2 = Join(watdiv1052644, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052593, watdiv1052644, ["d"], ["d"])
	j4 = Join(watdiv1052644, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_1():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052608_1 = Relation(name = "watdiv1052608", alias = "watdiv1052608_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052608_1, watdiv1052644, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052608_0, watdiv1052608_1, ["s"], ["s"])
	j1 = Join(watdiv1052608_0, watdiv1052644, ["d"], ["s"])
	j2 = Join(watdiv1052644, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052608_1, watdiv1052644, ["d"], ["d"])
	j4 = Join(watdiv1052644, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_15():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651, watdiv1052644_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052644_0, watdiv1052651, ["s"], ["s"])
	j1 = Join(watdiv1052644_0, watdiv1052644_2, ["d"], ["s"])
	j2 = Join(watdiv1052644_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052651, watdiv1052644_2, ["d"], ["d"])
	j4 = Join(watdiv1052644_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_14():
	watdiv1052608 = Relation(name = "watdiv1052608", alias = "watdiv1052608", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052593 = Relation(name = "watdiv1052593", alias = "watdiv1052593", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608, watdiv1052593, watdiv1052651, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052608, watdiv1052593, ["s"], ["s"])
	j1 = Join(watdiv1052608, watdiv1052651, ["d"], ["s"])
	j2 = Join(watdiv1052651, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052593, watdiv1052651, ["d"], ["d"])
	j4 = Join(watdiv1052651, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_16():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052644_0, watdiv1052644_1, ["s"], ["s"])
	j1 = Join(watdiv1052644_0, watdiv1052651, ["d"], ["s"])
	j2 = Join(watdiv1052651, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052644_1, watdiv1052651, ["d"], ["d"])
	j4 = Join(watdiv1052651, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_17():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_3 = Relation(name = "watdiv1052645", alias = "watdiv1052645_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_4 = Relation(name = "watdiv1052645", alias = "watdiv1052645_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052651_2, watdiv1052645_3, watdiv1052645_4]

	j0 = Join(watdiv1052651_0, watdiv1052651_1, ["s"], ["s"])
	j1 = Join(watdiv1052651_0, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052645_3, ["s"], ["s"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052645_4, ["d"], ["s"])
	j5 = Join(watdiv1052645_3, watdiv1052645_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_13():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052608_1 = Relation(name = "watdiv1052608", alias = "watdiv1052608_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052608_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644]

	j0 = Join(watdiv1052608_0, watdiv1052608_1, ["s"], ["s"])
	j1 = Join(watdiv1052608_0, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j3 = Join(watdiv1052608_1, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052644, ["d"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_12():
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651, watdiv1052644_1, watdiv1052644_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052651, watdiv1052644_1, ["s"], ["s"])
	j1 = Join(watdiv1052651, watdiv1052644_2, ["d"], ["s"])
	j2 = Join(watdiv1052644_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["d"])
	j4 = Join(watdiv1052644_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_10():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_3 = Relation(name = "watdiv1052645", alias = "watdiv1052645_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_4 = Relation(name = "watdiv1052645", alias = "watdiv1052645_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651, watdiv1052645_3, watdiv1052645_4]

	j0 = Join(watdiv1052644_0, watdiv1052644_1, ["s"], ["s"])
	j1 = Join(watdiv1052644_0, watdiv1052651, ["d"], ["s"])
	j2 = Join(watdiv1052651, watdiv1052645_3, ["s"], ["s"])
	j3 = Join(watdiv1052644_1, watdiv1052651, ["d"], ["d"])
	j4 = Join(watdiv1052651, watdiv1052645_4, ["d"], ["s"])
	j5 = Join(watdiv1052645_3, watdiv1052645_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_11():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644, watdiv1052651_2, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052651_0, watdiv1052644, ["s"], ["s"])
	j1 = Join(watdiv1052651_0, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052644, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_18():
	watdiv1052593 = Relation(name = "watdiv1052593", alias = "watdiv1052593", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052608 = Relation(name = "watdiv1052608", alias = "watdiv1052608", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052593, watdiv1052608, watdiv1052651, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052593, watdiv1052608, ["s"], ["s"])
	j1 = Join(watdiv1052593, watdiv1052651, ["d"], ["s"])
	j2 = Join(watdiv1052651, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052608, watdiv1052651, ["d"], ["d"])
	j4 = Join(watdiv1052651, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_9():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052608_1 = Relation(name = "watdiv1052608", alias = "watdiv1052608_1", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651 = Relation(name = "watdiv1052651", alias = "watdiv1052651", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_3 = Relation(name = "watdiv1052584", alias = "watdiv1052584_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052584_4 = Relation(name = "watdiv1052584", alias = "watdiv1052584_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052608_1, watdiv1052651, watdiv1052584_3, watdiv1052584_4]

	j0 = Join(watdiv1052608_0, watdiv1052608_1, ["s"], ["s"])
	j1 = Join(watdiv1052608_0, watdiv1052651, ["d"], ["s"])
	j2 = Join(watdiv1052651, watdiv1052584_3, ["s"], ["s"])
	j3 = Join(watdiv1052608_1, watdiv1052651, ["d"], ["d"])
	j4 = Join(watdiv1052651, watdiv1052584_4, ["d"], ["s"])
	j5 = Join(watdiv1052584_3, watdiv1052584_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q4_8():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_3 = Relation(name = "watdiv1052645", alias = "watdiv1052645_3", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	watdiv1052645_4 = Relation(name = "watdiv1052645", alias = "watdiv1052645_4", attributes = ['s', 'd'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644, watdiv1052651_2, watdiv1052645_3, watdiv1052645_4]

	j0 = Join(watdiv1052651_0, watdiv1052644, ["s"], ["s"])
	j1 = Join(watdiv1052651_0, watdiv1052651_2, ["d"], ["s"])
	j2 = Join(watdiv1052651_2, watdiv1052645_3, ["s"], ["s"])
	j3 = Join(watdiv1052644, watdiv1052651_2, ["d"], ["d"])
	j4 = Join(watdiv1052651_2, watdiv1052645_4, ["d"], ["s"])
	j5 = Join(watdiv1052645_3, watdiv1052645_4, ["d"], ["d"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q9_22():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052644_2, watdiv1052644_3, watdiv1052651_4, watdiv1052651_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052651_0, watdiv1052644_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052644_2, ["d"], ["s"])
	j4 = Join(watdiv1052644_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_23():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052644_2, watdiv1052644_3, watdiv1052644_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052644_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["s"])
	j4 = Join(watdiv1052644_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_21():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_20():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_4 = Relation(name = "watdiv1052608", alias = "watdiv1052608_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052644_1, watdiv1052652_2, watdiv1052652_3, watdiv1052608_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052608_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052608_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052608_4, ["d"], ["s"])
	j7 = Join(watdiv1052608_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_18():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644 = Relation(name = "watdiv1052644", alias = "watdiv1052644", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052651_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644, ["d"], ["s"])
	j7 = Join(watdiv1052644, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_24():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052651_5, watdiv1052651_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_25():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_19():
	watdiv1052608 = Relation(name = "watdiv1052608", alias = "watdiv1052608", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652 = Relation(name = "watdiv1052652", alias = "watdiv1052652", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608, watdiv1052644_1, watdiv1052652, watdiv1052644_3, watdiv1052651_4, watdiv1052651_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052608, watdiv1052652, ["s"], ["d"])
	j1 = Join(watdiv1052608, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052652, ["d"], ["s"])
	j4 = Join(watdiv1052652, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_27():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052651_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_26():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_8():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_4 = Relation(name = "watdiv1052608", alias = "watdiv1052608_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052651_1, watdiv1052652_2, watdiv1052652_3, watdiv1052608_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052608_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052608_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052608_4, ["d"], ["s"])
	j7 = Join(watdiv1052608_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_9():
	watdiv1052624_0 = Relation(name = "watdiv1052624", alias = "watdiv1052624_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_1 = Relation(name = "watdiv1052608", alias = "watdiv1052608_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052655_2 = Relation(name = "watdiv1052655", alias = "watdiv1052655_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052655_3 = Relation(name = "watdiv1052655", alias = "watdiv1052655_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052624_4 = Relation(name = "watdiv1052624", alias = "watdiv1052624_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_5 = Relation(name = "watdiv1052608", alias = "watdiv1052608_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_6 = Relation(name = "watdiv1052652", alias = "watdiv1052652_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_7 = Relation(name = "watdiv1052652", alias = "watdiv1052652_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052624_0, watdiv1052608_1, watdiv1052655_2, watdiv1052655_3, watdiv1052624_4, watdiv1052608_5, watdiv1052652_6, watdiv1052652_7]

	j0 = Join(watdiv1052624_0, watdiv1052655_2, ["s"], ["d"])
	j1 = Join(watdiv1052624_0, watdiv1052608_1, ["d"], ["s"])
	j2 = Join(watdiv1052608_1, watdiv1052652_6, ["s"], ["d"])
	j3 = Join(watdiv1052608_1, watdiv1052655_2, ["d"], ["s"])
	j4 = Join(watdiv1052655_2, watdiv1052655_3, ["s"], ["s"])
	j5 = Join(watdiv1052655_3, watdiv1052608_5, ["s"], ["d"])
	j6 = Join(watdiv1052655_3, watdiv1052624_4, ["d"], ["s"])
	j7 = Join(watdiv1052624_4, watdiv1052608_5, ["d"], ["s"])
	j8 = Join(watdiv1052608_5, watdiv1052652_7, ["s"], ["d"])
	j9 = Join(watdiv1052652_6, watdiv1052652_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_2():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651_2, watdiv1052644_3, watdiv1052651_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_3():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052651_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052651_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_1():
	watdiv1052602_0 = Relation(name = "watdiv1052602", alias = "watdiv1052602_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052602_4 = Relation(name = "watdiv1052602", alias = "watdiv1052602_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052602_0, watdiv1052644_1, watdiv1052652_2, watdiv1052652_3, watdiv1052602_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052602_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052602_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052602_4, ["d"], ["s"])
	j7 = Join(watdiv1052602_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_4():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052651_4, watdiv1052651_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_5():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052644_2, watdiv1052644_3, watdiv1052644_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052644_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["s"])
	j4 = Join(watdiv1052644_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_7():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052651_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_6():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644_1, watdiv1052651_2, watdiv1052644_3, watdiv1052651_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052651_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_17():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052651_1, watdiv1052644_2, watdiv1052644_3, watdiv1052651_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052651_0, watdiv1052644_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052644_2, ["d"], ["s"])
	j4 = Join(watdiv1052644_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_16():
	watdiv1052595_0 = Relation(name = "watdiv1052595", alias = "watdiv1052595_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052638_1 = Relation(name = "watdiv1052638", alias = "watdiv1052638_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052595_4 = Relation(name = "watdiv1052595", alias = "watdiv1052595_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052638_5 = Relation(name = "watdiv1052638", alias = "watdiv1052638_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052595_6 = Relation(name = "watdiv1052595", alias = "watdiv1052595_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052595_7 = Relation(name = "watdiv1052595", alias = "watdiv1052595_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052595_0, watdiv1052638_1, watdiv1052652_2, watdiv1052652_3, watdiv1052595_4, watdiv1052638_5, watdiv1052595_6, watdiv1052595_7]

	j0 = Join(watdiv1052595_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052595_0, watdiv1052638_1, ["d"], ["s"])
	j2 = Join(watdiv1052638_1, watdiv1052595_6, ["s"], ["d"])
	j3 = Join(watdiv1052638_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052638_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052595_4, ["d"], ["s"])
	j7 = Join(watdiv1052595_4, watdiv1052638_5, ["d"], ["s"])
	j8 = Join(watdiv1052638_5, watdiv1052595_7, ["s"], ["d"])
	j9 = Join(watdiv1052595_6, watdiv1052595_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_14():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_28():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_4 = Relation(name = "watdiv1052608", alias = "watdiv1052608_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052644_1, watdiv1052652_2, watdiv1052652_3, watdiv1052608_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052608_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052608_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052608_4, ["d"], ["s"])
	j7 = Join(watdiv1052608_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_15():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644_1, watdiv1052651_2, watdiv1052651_3, watdiv1052651_4, watdiv1052644_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052651_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_11():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052651_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052651_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_10():
	watdiv1052651_0 = Relation(name = "watdiv1052651", alias = "watdiv1052651_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_2 = Relation(name = "watdiv1052644", alias = "watdiv1052644_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_3 = Relation(name = "watdiv1052644", alias = "watdiv1052644_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_4 = Relation(name = "watdiv1052651", alias = "watdiv1052651_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_5 = Relation(name = "watdiv1052644", alias = "watdiv1052644_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052651_0, watdiv1052644_1, watdiv1052644_2, watdiv1052644_3, watdiv1052651_4, watdiv1052644_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052651_0, watdiv1052644_2, ["s"], ["d"])
	j1 = Join(watdiv1052651_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052644_2, ["d"], ["s"])
	j4 = Join(watdiv1052644_2, watdiv1052644_3, ["s"], ["s"])
	j5 = Join(watdiv1052644_3, watdiv1052644_5, ["s"], ["d"])
	j6 = Join(watdiv1052644_3, watdiv1052651_4, ["d"], ["s"])
	j7 = Join(watdiv1052651_4, watdiv1052644_5, ["d"], ["s"])
	j8 = Join(watdiv1052644_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_12():
	watdiv1052608_0 = Relation(name = "watdiv1052608", alias = "watdiv1052608_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_1 = Relation(name = "watdiv1052651", alias = "watdiv1052651_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_2 = Relation(name = "watdiv1052652", alias = "watdiv1052652_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052652_3 = Relation(name = "watdiv1052652", alias = "watdiv1052652_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052608_4 = Relation(name = "watdiv1052608", alias = "watdiv1052608_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_6 = Relation(name = "watdiv1052644", alias = "watdiv1052644_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_7 = Relation(name = "watdiv1052644", alias = "watdiv1052644_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052608_0, watdiv1052651_1, watdiv1052652_2, watdiv1052652_3, watdiv1052608_4, watdiv1052651_5, watdiv1052644_6, watdiv1052644_7]

	j0 = Join(watdiv1052608_0, watdiv1052652_2, ["s"], ["d"])
	j1 = Join(watdiv1052608_0, watdiv1052651_1, ["d"], ["s"])
	j2 = Join(watdiv1052651_1, watdiv1052644_6, ["s"], ["d"])
	j3 = Join(watdiv1052651_1, watdiv1052652_2, ["d"], ["s"])
	j4 = Join(watdiv1052652_2, watdiv1052652_3, ["s"], ["s"])
	j5 = Join(watdiv1052652_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052652_3, watdiv1052608_4, ["d"], ["s"])
	j7 = Join(watdiv1052608_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052644_7, ["s"], ["d"])
	j9 = Join(watdiv1052644_6, watdiv1052644_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q9_13():
	watdiv1052644_0 = Relation(name = "watdiv1052644", alias = "watdiv1052644_0", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_1 = Relation(name = "watdiv1052644", alias = "watdiv1052644_1", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_2 = Relation(name = "watdiv1052651", alias = "watdiv1052651_2", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_3 = Relation(name = "watdiv1052651", alias = "watdiv1052651_3", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052644_4 = Relation(name = "watdiv1052644", alias = "watdiv1052644_4", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_5 = Relation(name = "watdiv1052651", alias = "watdiv1052651_5", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_6 = Relation(name = "watdiv1052651", alias = "watdiv1052651_6", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	watdiv1052651_7 = Relation(name = "watdiv1052651", alias = "watdiv1052651_7", attributes = ['d', 's'], filters = [], projections = ['d', 's'])
	relations = [watdiv1052644_0, watdiv1052644_1, watdiv1052651_2, watdiv1052651_3, watdiv1052644_4, watdiv1052651_5, watdiv1052651_6, watdiv1052651_7]

	j0 = Join(watdiv1052644_0, watdiv1052651_2, ["s"], ["d"])
	j1 = Join(watdiv1052644_0, watdiv1052644_1, ["d"], ["s"])
	j2 = Join(watdiv1052644_1, watdiv1052651_6, ["s"], ["d"])
	j3 = Join(watdiv1052644_1, watdiv1052651_2, ["d"], ["s"])
	j4 = Join(watdiv1052651_2, watdiv1052651_3, ["s"], ["s"])
	j5 = Join(watdiv1052651_3, watdiv1052651_5, ["s"], ["d"])
	j6 = Join(watdiv1052651_3, watdiv1052644_4, ["d"], ["s"])
	j7 = Join(watdiv1052644_4, watdiv1052651_5, ["d"], ["s"])
	j8 = Join(watdiv1052651_5, watdiv1052651_7, ["s"], ["d"])
	j9 = Join(watdiv1052651_6, watdiv1052651_7, ["s"], ["s"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

