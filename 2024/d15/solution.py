import copy
import enum
from typing import Dict, Tuple

WIDE_TILES = {".": "..", "#": "##", "O": "[]"}

class Direction(enum.Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

    def move(self, pos: complex) -> complex:
        match self:
            case Direction.UP: 
                return pos - 1j
            case Direction.DOWN: 
                return pos + 1j
            case Direction.RIGHT: 
                return pos + 1
            case Direction.LEFT:
                return pos - 1

def parse_map(input_str: str) -> Tuple[complex, Dict[complex, str]]:
    m = {}
    start = 0
    for y, line in enumerate(input_str.strip().split('\n')):
        for x, c in enumerate(line.strip()):
            if c == '@':
                start = x + y * 1j
            m[x + y * 1j] = c
    return start, m

def parse_movements(input_str: str) -> list[Direction]:
    return [Direction(c) for c in input_str.strip() if c in '^v<>']

def parse_input(file: str) -> Tuple[complex, Dict[complex, str], list[Direction]]:
    with open(file) as f:
        input_str = f.read()
    ms, ps = input_str.split('\n\n')
    return *parse_map(ms), parse_movements(ps)

def checksum(m: Dict[complex, str]) -> int:
    result = 0
    for cord, c in m.items():
        if c == 'O':
            result += int(100 * cord.imag + cord.real)

    return result

class LanternFish:
    def __init__(self, start: complex, m: Dict[complex, str], movements: list[Direction]):
        self.pos = start
        self.m = copy.deepcopy(m)
        self.movements = movements

    def swim(self):
        for d in self.movements:
            self.move(d)

    def move_obj(self, pos: complex, d: Direction):
        new_pos = d.move(pos)
        if new_pos not in self.m:
            # no move
            return pos
        if self.m[new_pos] == '#':
            # no move
            return pos
        if self.m[new_pos] == 'O':
            # try to move box
            self.move_obj(new_pos, d)

        if self.m[new_pos] == '.':
            # update
            self.m[new_pos] = self.m[pos]
            self.m[pos] = '.'
            return new_pos

        return pos

    def move(self, d: Direction):
        self.pos = self.move_obj(self.pos, d)

def print_map(m: Dict[complex, str]):
    min_x = int(min(p.real for p in m))
    max_x = int(max(p.real for p in m))
    min_y = int(min(p.imag for p in m))
    max_y = int(max(p.imag for p in m))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(m.get(x + y * 1j, ' '), end='')
        print()

f = LanternFish(*parse_input('input'))
f.swim()
print(checksum(f.m))
