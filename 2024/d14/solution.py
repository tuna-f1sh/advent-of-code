import math

GRID_X = 101
GRID_Y = 103

class Robot:
    def __init__(self, pos, velocity, grid = (GRID_X, GRID_Y)):
        # x tiles from left, y tiles from top
        self._pos = pos
        # veclocity in tiles/s +ve x is right, +ve y is down
        self._v = velocity
        self._grid = grid

    def __repr__(self):
        return f"Robot(pos={self._pos}, velocity={self._v})"

    def __str__(self):
        return f"p={self._pos[0]},{self._pos[1]} v={self._v[0]},{self._v[1]}>"

    def move(self, t=1):
        x, y = self._pos
        vx, vy = self._v
        # robots teleport to the other side of the grid on exit
        self._pos = ((x + vx * t) % self._grid[0], (y + vy * t) % self._grid[1])

    @property
    def pos(self):
        return self._pos

    @staticmethod
    def parse(s: str, grid = (GRID_X, GRID_Y)):
        """p=0,4 v=3,-3"""
        pos, vel = s.split(" ")
        x, y = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        return Robot((x, y), (vx, vy), grid)

def parse_robots(f: str, grid = (GRID_X, GRID_Y)):
    with open(f) as file:
        lines = file.readlines()
        return [Robot.parse(line, grid) for line in lines]

def plot_robots(robots, grid_size=(GRID_X, GRID_Y)):
    center = (grid_size[0] // 2, grid_size[1] // 2)
    grid = [[0 if x != center[0] and y != center[1] else -1 for x in range(grid_size[0])] for y in range(grid_size[1])]
    for r in robots:
        x, y = r.pos
        if x != center[0] and y != center[1]:
            grid[y][x] += 1
    for row in grid:
        print("".join([str(x) if x > 0 else '.' if x == 0 else ' ' for x in row ]))
    return grid

def calc_quadrants(robots, grid_size=(GRID_X, GRID_Y)):
    center = (grid_size[0] // 2, grid_size[1] // 2)
    quad = [0, 0, 0, 0]
    for r in robots:
        x, y = r.pos
        if x < center[0] and y < center[1]:
            quad[0] += 1
        elif x > center[0] and y < center[1]:
            quad[1] += 1
        elif x < center[0] and y > center[1]:
            quad[2] += 1
        elif x > center[0] and y > center[1]:
            quad[3] += 1
    return math.prod(quad)

def example():
    robots = parse_robots("example", grid=(11, 7))
    for r in robots:
        r.move(t=100)
    plot_robots(robots, (11, 7))
    print(calc_quadrants(robots, (11, 7)))

def part1():
    robots = parse_robots("input")
    for r in robots:
        r.move(t=100)
    plot_robots(robots)
    return calc_quadrants(robots)

def part2():
    robots = parse_robots("input")
    it = 1
    pos_set = set()
    while True:
        pos_set.clear()
        [r.move() for r in robots]
        # check for non-overlapping robots...maybe easter egg?
        for r in robots:
            # if we have a collision, keep looking
            if r.pos in pos_set:
                break
            pos_set.add(r.pos)
        # no collisions and loop is complete - we have a winner
        else:
            plot_robots(robots)
            return it
        it += 1

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
