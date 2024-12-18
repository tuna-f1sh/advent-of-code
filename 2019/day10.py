import math
from numpy import array
from numpy.linalg import norm

"""
- The map indicates whether each position is empty (.) or contains an asteroid (#)
- The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).
- A monitoring station can detect any asteroid to which it has direct line of sight 
- The best location is the asteroid that can detect the largest number of other asteroids.
"""
##

FILE = './input/day10.txt'

def init_asteroids(filename):
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            for x, a in enumerate(line):
                if a == '#':
                    yield (x, y)

ASTERIODS = list(init_asteroids(FILE))

def angle(asteroid, target):
    (x1, y1), (x2, y2) = asteroid, target
    return math.atan2(x2 - x1, y1 - y2) % (2 * math.pi)

def unique_lines(asteroid):
    return len(set(angle(asteroid, other) for other in ASTERIODS))

def part_one():
    number_visible, laser_base = max((unique_lines(asteroid), asteroid) for asteroid in ASTERIODS)
    print('Part one count: {}'.format(number_visible))
    return laser_base

LASER = part_one()

ASTERIODS.remove(LASER)

angles = sorted(
    ((angle(LASER, end), end) for end in ASTERIODS),
    key=lambda x: (x[0], abs(LASER[0] - x[1][0]) + abs(LASER[1] - x[1][1]))
)

ASTERIODS.sort(key=lambda asteroid: norm(array(asteroid) - LASER))
# Number of asteroids closer to laser_base with same angle
rank = {asteroid : sum(angle(LASER, asteroid) == angle(LASER, other)
                       for other in ASTERIODS[:i])
        for i, asteroid in enumerate(ASTERIODS)}
x, y = sorted(ASTERIODS, key=lambda asteroid: (rank[asteroid], angle(LASER, asteroid)))[199]
print(x * 100 + y) # Part 2
