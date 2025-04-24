from query_utility import Relation, Join, JoinGraph


def create_synthetic_tvc_join(selectivity: int):
    relations: list[Relation] = []
    joins: list[Join] = []

    # Fact 1
    relations.append(Relation(f"rel_{0}", f"r_{0}", ["id", "d1", "d2", "w"], [f"r_0.id < {selectivity}"]))
    # Dimension
    relations.append(Relation(f"rel_{1}", f"r_{1}", ["f", "a", "w"]))
    for i in range(2, 7):
        relations.append(Relation(f"rel_{i}", f"r_{i}", ["a1", "a2", "a3", "w"]))
    # Fact 2
    relations.append(Relation(f"rel_{7}", f"r_{7}", ["f", "a", "w"]))

    joins.append(Join(relations[0], relations[1], ["d1"], ["f"]))
    joins.append(Join(relations[1], relations[2], ["a"], ["a1"]))
    joins.append(Join(relations[1], relations[6], ["a"], ["a3"]))
    joins.append(Join(relations[2], relations[5], ["a3"], ["a3"]))
    joins.append(Join(relations[2], relations[3], ["a2"], ["a1"]))
    joins.append(Join(relations[3], relations[4], ["a2"], ["a1"]))
    joins.append(Join(relations[4], relations[5], ["a2"], ["a1"]))
    joins.append(Join(relations[5], relations[6], ["a2"], ["a2"]))
    joins.append(Join(relations[6], relations[7], ["a1"], ["a"]))
    joins.append(Join(relations[7], relations[0], ["f"], ["d2"]))

    return JoinGraph(relations, joins)