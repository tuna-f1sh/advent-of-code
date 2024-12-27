def parse_input(f: str):
    locks = []
    keys = []

    with open(f, 'r') as fh:
        items = fh.read().strip().split('\n\n')
        for item in items:
            ref = None
            for line in item.split('\n'):
                if ref is None:
                    ref = locks if line.startswith('#') else keys
                    ref.append([0] * len(line))
                    continue
                if all(c == '.' for c in line) or all(c == '#' for c in line):
                    continue
                for j, c in enumerate(line):
                    if c == '#':
                        ref[-1][j] += 1

    return locks, keys

def check_fits(locks, keys):
    ret = 0
    for lock in locks:
        for key in keys:
            # assuming key divets of 5
            if all(l + k <= 5 for l, k in zip(lock, key)):
                ret += 1

    return ret

def part1(f: str = 'input'):
    locks, keys = parse_input(f)
    return check_fits(locks, keys)

assert part1('example') == 3
print(f"Part 1: {part1()}")
