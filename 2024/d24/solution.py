from collections import defaultdict

LOGIC = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y,
        }

def parse_input(f: str):
    wires = {}
    outs = {}

    with open(f, 'r') as file:
        initial, gates = file.read().strip().split('\n\n')

    for i in initial.split('\n'):
        gate, num = i.split(':')
        wires[gate] = int(num.strip())

    for g in gates.split('\n'):
        split = g.split(' ')
        g1 = split[0]
        op = split[1]
        g2 = split[2]
        g3 = split[-1]

        outs[g3] = (g1, op, g2)

    return wires, outs

def calc(wires: dict, outs: dict, wire: str):
    """
    Recursively calculate the state of a wire based on dependent wires

    Wire states don't change once set but must have input before input to gate
    """
    g1, op, g2 = outs[wire]
    if wires.get(g1) is None:
        calc(wires, outs, g1)
    if wires.get(g2) is None:
        calc(wires, outs, g2)

    wires[wire] = LOGIC[op](wires[g1], wires[g2])

def part1(f: str):
    wires, outs = parse_input(f)
    zees = set([w for w in outs if w[0] == 'z'])
    num_zees = len(zees)
    for w in outs:
        calc(wires, outs, w)
        zees.discard(w)
        if not zees:
            break

    ret = 0
    for i in range(num_zees):
        ret += (wires[f'z{i:02}'] << i)

    return ret

assert part1('example') == 2024
print(f"Part 1: {part1('input')}")
