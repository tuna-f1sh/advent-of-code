import heapq
from typing import Dict, Tuple

def parse_memory(f: str, falls: int, size: Tuple[int, int]) -> Tuple[Dict[Tuple[int, int], str], Tuple[int, int]]:
    memory = {(x, y): '.' for x in range(size[0]) for y in range(size[1])}
    last = (0, 0)
    with open(f) as file:
        for i, line in enumerate(file):
            if i == falls:
                break
            x, y = map(int, line.strip().split(','))
            memory[(int(x), int(y))] = '#'
            last = (int(x), int(y))

    return memory, last

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    open_set = []  # Priority queue (min-heap)
    heapq.heappush(open_set, (0, start, [start]))  # (g_score, position, path)

    g_score = {start: 0}  # Cost from start to the node

    while open_set:
        p, current_pos, path = heapq.heappop(open_set)

        if current_pos == end:
            return len(path) - 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current_pos[0] + dx, current_pos[1] + dy)
            if neighbor not in maze or maze[neighbor] == '#':
                continue

            tentative_g_score = p + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor, path + [neighbor]))

    return None

def example():
    memory, _ = parse_memory('example', 12, (7, 7))
    start = (0, 0)
    end = (6, 6)
    assert a_star(memory, start, end) == 22

def part1():
    memory, _ = parse_memory('input', 1024, (71, 71))
    start = (0, 0)
    end = (70, 70)
    print(a_star(memory, start, end))

def part2():
    f = 1024
    while True:
        # brute force...should not load map every time but works...
        memory, ret = parse_memory('input', f, (71, 71))
        if a_star(memory, (0,0), (70,70)) is None:
            print(ret)
            break
        f += 1
