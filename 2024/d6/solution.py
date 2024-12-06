import enum
from typing import Dict, Tuple, Set

# Would be nicer as class with Direection enum...
# next_cord should be iterator
class Direction(enum.Enum):
    Up = '^'
    Down = 'v'
    Left = '<'
    Right = '>'

    def next_cord(self, cord: Tuple[int, int]) -> Tuple[int, int]:
        """Returns the next cord in the direction"""
        x, y = cord
        if self == Direction.Up:
            return x, y - 1
        if self == Direction.Down:
            return x, y + 1
        if self == Direction.Left:
            return x - 1, y
        if self == Direction.Right:
            return x + 1, y
        raise ValueError("Unknown direction")

    def turn_right(self) -> 'Direction':
        """Turns 90 right"""
        if self == Direction.Up:
            return Direction.Right
        if self == Direction.Right:
            return Direction.Down
        if self == Direction.Down:
            return Direction.Left
        if self == Direction.Left:
            return Direction.Up
        raise ValueError("Unknown direction")

    def walk(self, m: Dict[Tuple[int, int], str], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        """Walks in direction until exit or obstacle (#) is hit. When an obstacle is hit, it will turn 90 right. On exit map, returns the visited cords"""
        cord = start
        visited = set([start])
        while True:
            n = self.next_cord(cord)
            # walking off map
            char = m.get(n)
            if char is None:
                return visited
            # hit obstacle
            if char == '#':
                self = self.turn_right()
            else:
                cord = n
                visited.add(cord)

def read_map(f: str) -> Dict[Tuple[int, int], str]:
    """Read map into cord dict"""
    with open(f) as file:
        return {(x, y): c for y, line in enumerate(file) for x, c in enumerate(line.strip())}

def find_guard(map: Dict[Tuple[int, int], str]) -> Tuple[Tuple[int, int], Direction]:
    """Find the guard's walk"""
    for cord, c in map.items():
        if c in [d.value for d in Direction]:
            return cord, Direction(c)
    raise ValueError("Guard not found")

def part1(f: str) -> int:
    m = read_map(f)
    start, direction = find_guard(m)
    visited = direction.walk(m, start)
    return len(visited)
