class Button:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    @property
    def cord(self):
        return complex(self.x, self.y)

    def press(self, cord):
        return cord + self.cord

    @staticmethod
    def parse(s: str):
        tokens = s[10:].split(', ')
        return [int(token[2:]) for token in tokens]

class Prize:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def cord(self):
        return complex(self.x, self.y)

    def check(self, cord):
        return cord == self.cord

    @staticmethod
    def parse(s: str):
        tokens = s[7:].split(', ')
        return [int(token[2:]) for token in tokens]

    def calc_tokens(self, a: Button, b: Button):
        # https://en.wikipedia.org/wiki/Cramer%27s_rule#Explicit_formulas_for_small_systems
        denominator = a.x * b.y - a.y * b.x
        numerator = self.y * a.x - self.x * a.y
        b_presses = (numerator / denominator)
        if not b_presses.is_integer():
            return 0

        a_presses = (self.x - b.x * b_presses) / a.x
        if not a_presses.is_integer():
            return 0

        return int(a.cost * a_presses + b.cost * b_presses)

def parse_input(f: str):
    with open(f, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            button_a = Button(*Button.parse(lines[i]), cost=3)
            button_b = Button(*Button.parse(lines[i+1]), cost=1)
            prize = Prize(*Prize.parse(lines[i+2]))
            i += 4
            yield button_a, button_b, prize

def part1():
    ret = 0
    for button_a, button_b, prize in parse_input("input"):
        ret += prize.calc_tokens(button_a, button_b)

    return ret

def part2():
    ret = 0
    for button_a, button_b, prize in parse_input("input"):
        prize.x += 10000000000000
        prize.y += 10000000000000
        ret += prize.calc_tokens(button_a, button_b)

    return ret

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
