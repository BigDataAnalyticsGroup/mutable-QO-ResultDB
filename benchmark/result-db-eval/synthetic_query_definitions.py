from query_utility import Relation, Join, JoinGraph


def create_synthetic_chain_join(selectivity: float):
    relations: list[Relation] = []
    joins: list[Join] = []

    # Fact 1
    relations.append(Relation(f"rel_{0}", f"r_{0}", ["id_0", "id_1", "w"], [f"r_0.id_1 < {selectivity}"]))
    # Dimension
    relations.append(Relation(f"rel_{1}", f"r_{1}", ["id", "fk", "w"]))
    for i in range(2, 7):
        relations.append(Relation(f"rel_{i}", f"r_{i}", ["id", "w"]))
    # Fact 2
    relations.append(Relation(f"rel_{7}", f"r_{7}", ["id", "fk", "w"]))


    joins.append(Join(relations[0], relations[1], ["id_0"], ["id"]))
    joins.append(Join(relations[7], relations[0], ["id"], ["id_0"]))
    joins.append(Join(relations[1], relations[2], ["fk"], ["id"]))
    joins.append(Join(relations[2], relations[3], ["id"], ["id"]))
    joins.append(Join(relations[4], relations[5], ["id"], ["id"]))
    joins.append(Join(relations[5], relations[6], ["id"], ["id"]))
    joins.append(Join(relations[6], relations[7], ["id"], ["fk"]))

    return JoinGraph(relations, joins)

def create_synthetic_cycle_join(selectivity: int):
    relations: list[Relation] = []
    joins: list[Join] = []

    # Fact 1
    relations.append(Relation(f"rel_{0}", f"r_{0}", ["id_0", "id_1", "w"], [f"r_0.id_1 < {selectivity}"]))
    # Dimension
    relations.append(Relation(f"rel_{1}", f"r_{1}", ["id", "fk", "w"]))
    for i in range(2, 7):
        relations.append(Relation(f"rel_{i}", f"r_{i}", ["id", "w"]))
    # Fact 2
    relations.append(Relation(f"rel_{7}", f"r_{7}", ["id", "fk", "w"]))


    joins.append(Join(relations[0], relations[1], ["id_0"], ["id"]))
    joins.append(Join(relations[1], relations[2], ["fk"], ["id"]))
    joins.append(Join(relations[2], relations[3], ["id"], ["id"]))
    joins.append(Join(relations[3], relations[4], ["id"], ["id"]))
    joins.append(Join(relations[4], relations[5], ["id"], ["id"]))
    joins.append(Join(relations[5], relations[6], ["id"], ["id"]))
    joins.append(Join(relations[6], relations[7], ["id"], ["fk"]))
    joins.append(Join(relations[7], relations[0], ["id"], ["id_0"]))

    return JoinGraph(relations, joins)

def create_synthetic_tvc_join(selectivity: int):
    relations: list[Relation] = []
    joins: list[Join] = []

    # Fact 1
    relations.append(Relation(f"rel_{0}", f"r_{0}", ["id_0", "id_1", "w"], [f"r_0.id_1 < {selectivity}"]))
    # Dimension
    relations.append(Relation(f"rel_{1}", f"r_{1}", ["id", "fk", "w"]))
    for i in range(2, 7):
        relations.append(Relation(f"rel_{i}", f"r_{i}", ["id", "w"]))
    # Fact 2
    relations.append(Relation(f"rel_{7}", f"r_{7}", ["id", "fk", "w"]))


    joins.append(Join(relations[0], relations[1], ["id_0"], ["id"]))
    joins.append(Join(relations[1], relations[2], ["fk"], ["id"]))
    joins.append(Join(relations[1], relations[6], ["fk"], ["id"]))
    joins.append(Join(relations[2], relations[5], ["id"], ["id"]))
    joins.append(Join(relations[2], relations[3], ["id"], ["id"]))
    joins.append(Join(relations[3], relations[4], ["id"], ["id"]))
    joins.append(Join(relations[4], relations[5], ["id"], ["id"]))
    joins.append(Join(relations[5], relations[6], ["id"], ["id"]))
    joins.append(Join(relations[6], relations[7], ["id"], ["fk"]))
    joins.append(Join(relations[7], relations[0], ["id"], ["id_0"]))

    return JoinGraph(relations, joins)