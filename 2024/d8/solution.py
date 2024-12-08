from typing import Dict, Tuple

def parse_antenna_map(f: str) -> Dict[Tuple[int, int], str]:
    with open(f) as file:
        return {(x, y): v for y, row in enumerate(file) for x, v in enumerate(row.strip())}

def map_antinodes(antennas: Dict[Tuple[int, int], str]) -> Dict[Tuple[int, int], str]:
    antinodes = {}
    for (x1, y1), f1 in antennas.items():
        if f1 == '.':
            continue
        for (x2, y2), f2 in antennas.items():
            if f1 == f2 and (x1, y1) != (x2, y2):
                # distance between two points
                # anti-nodes at double the distance from each point
                dx, dy = x2 - x1, y2 - y1
                # check it's inside map
                # would be fast to pass grid size as argument rather than get...
                if antennas.get((x1 + 2 * dx, y1 + 2 * dy)) is not None:
                    antinodes[(x1 + 2 * dx, y1 + 2 * dy)] = '#'

    return antinodes

def map_antinodes_p2(antennas: Dict[Tuple[int, int], str]) -> Dict[Tuple[int, int], str]:
    antinodes = {}
    for (x1, y1), f1 in antennas.items():
        if f1 == '.':
            continue
        for (x2, y2), f2 in antennas.items():
            if f1 == f2 and (x1, y1) != (x2, y2):
                # distance between two points
                # anti-nodes at double the distance from each point
                dx, dy = x2 - x1, y2 - y1
                # iterate over all multiples of the distance until we hit the edge
                m = 1
                # would be fast to pass grid size as argument rather than get...
                while antennas.get((x1 + m * dx, y1 + m * dy)) is not None:
                    antinodes[(x1 + m * dx, y1 + m * dy)] = '#'
                    m += 1

    return antinodes

def plot_antinodes(antinodes: Dict[Tuple[int, int], str]) -> None:
    min_x, max_x = min(x for x, _ in antinodes), max(x for x, _ in antinodes)
    min_y, max_y = min(y for _, y in antinodes), max(y for _, y in antinodes)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(antinodes.get((x, y), '.'), end='')
        print()

def part1(f: str) -> int:
    antennas = parse_antenna_map(f)
    antinodes = map_antinodes(antennas)
    return len(antinodes)

def part2(f: str) -> int:
    antennas = parse_antenna_map(f)
    antinodes = map_antinodes_p2(antennas)
    return len(antinodes)

print(f"Part 1: {part1('input')}")
print(f"Part 2: {part2('input')}")
