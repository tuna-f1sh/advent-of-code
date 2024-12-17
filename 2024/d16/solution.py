"""A* Raindeer path finding"""
import heapq

TURN_COST = 1000 # to turn 90 degrees
MOVE_COST = 1
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def parse_map(file: str):
    maze = {}
    start = None
    end = None
    with open(file) as f:
        for y, line in enumerate(f):
            for x, v in enumerate(line.strip()):
                pos = (x, y)
                if v == 'S':
                    start = pos
                    maze[pos] = '.'
                elif v == 'E':
                    end = pos
                    maze[pos] = '.'
                else:
                    maze[pos] = v
    return maze, start, end

def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    open_set = []  # Priority queue (min-heap)
    heapq.heappush(open_set, (0, start, (0,1)))  # (f_score, position, direction)

    g_score = {start: 0}  # Cost from start to the node
    f_score = {start: heuristic(start, end)}  # Estimated total cost of path through the node

    while open_set:
        _, current_pos, current_dir = heapq.heappop(open_set)

        if current_pos == end:
            return g_score[current_pos]

        for dx, dy in DIRECTIONS:
            neighbor = (current_pos[0] + dx, current_pos[1] + dy)
            if neighbor not in maze or maze[neighbor] == '#':
                continue

            # Got confused for a while thinking 180 would be twice but would never turn 180 so doesn't matter...
            move_cost = MOVE_COST if current_dir == (dx, dy) else TURN_COST + MOVE_COST
            tentative_g_score = g_score[current_pos] + move_cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor, (dx, dy)))

    return None

def a_star_tiles(maze, start, end):
    open_set = []  # Priority queue (min-heap)
    heapq.heappush(open_set, (0, start, (0,1), [start]))  # (f_score, position, direction, path)

    g_score = {start: 0}  # Cost from start to the node
    f_score = {start: heuristic(start, end)}  # Estimated total cost of path through the node
    good_tiles = set()

    while open_set:
        p, current_pos, current_dir, path = heapq.heappop(open_set)

        if current_pos == end:
            print(f"Path: {path[1:-1]}")
            good_tiles |= set(path[1:-1])

        for dx, dy in DIRECTIONS:
            neighbor = (current_pos[0] + dx, current_pos[1] + dy)
            if neighbor not in maze or maze[neighbor] == '#':
                continue

            # Got confused for a while thinking 180 would be twice but would never turn 180 so doesn't matter...
            move_cost = MOVE_COST if current_dir == (dx, dy) else TURN_COST + MOVE_COST
            tentative_g_score = g_score[current_pos] + move_cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor] + p, neighbor, (dx, dy), path + [neighbor]))


    return len(good_tiles)

def part1(file: str):
    maze, start, end = parse_map(file)
    print(f"Start: {start}, End: {end}")
    score = a_star(maze, start, end)
    return score if score else "No path found"

def part2(file: str):
    maze, start, end = parse_map(file)
    print(f"Start: {start}, End: {end}")
    score = a_star_tiles(maze, start, end)
    return score if score else "No path found"

print(f"Part 1: {part1('input')}")
print(f"Part 2: {part2('input')}")
