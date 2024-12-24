from collections import defaultdict
from itertools import combinations

def parse_network(f: str) -> dict:
    with open(f, 'r') as file:
        lines = file.readlines()
    network = defaultdict(set)
    for line in lines:
        n1, n2 = line.strip().split('-')
        network[n1].add(n2)
        network[n2].add(n1)

    return network

def inter_connected_t_computers(network: dict) -> int:
    triples = []
    for n1 in network.keys():
        if n1[0] != 't':
            continue
        for n2, n3 in combinations(network[n1], 2):
            if n2 in network[n3]:
                lan = {n1, n2, n3}
                if lan not in triples:
                    triples.append(lan)

    return len(triples)

assert inter_connected_t_computers(parse_network('example')) == 7
print(f"Part 1: {inter_connected_t_computers(parse_network('input'))}")
