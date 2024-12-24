import networkx as nx

def parse_network(f: str):
    with open(f, 'r') as file:
        lines = file.readlines()
    g = nx.Graph()
    for line in lines:
        n1, n2 = line.strip().split('-')
        g.add_node(n1)
        g.add_node(n2)
        g.add_edge(n1, n2)

    return g

g = parse_network('input')
clique = nx.approximation.max_clique(g)
clique = list(clique)
print(clique)
clique.sort()
print(",".join(clique))
