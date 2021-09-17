import itertools

import networkx as nx
import networkx.algorithms.clique

def generator(pool, result):
    for x in result:
        flag = True
        a=list(itertools.chain(*x))
        for y in pool:
            b=[y]
            c = list(itertools.chain(*b))
            if not set(a).isdisjoint(set(c)):
                continue
            flag = False
            yield x + b
        if flag:
            yield x

def product(*args):
    result = [[]]
    for pool in args:
        result = generator(pool, result)
    return result

def main():
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 6)
    G.add_edge(4, 7)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(3, 5)
    G.add_edge(7, 8)
    G.add_edge(6, 10)
    G.add_edge(5, 9)
    G.add_edge(10, 11)
    G.add_edge(11, 12)
    G.add_edge(11, 13)
    G.add_edge(12, 13)

    cliques = list(networkx.algorithms.clique.enumerate_all_cliques(G))
    print(cliques)
    dict={}
    for clique in cliques:
        for node in clique:
           dict.setdefault(node,[]).append(tuple(clique))
    print(dict)
    sorteddict = sorted(dict)
    combinations=product(*(dict[key] for key in sorteddict))
    print("Final Result")
    for idx,scenario in enumerate(combinations):
        print("Scenario {} is {}".format(idx, scenario))



if __name__ == '__main__':
    main()
