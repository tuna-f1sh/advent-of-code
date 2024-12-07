from typing import Tuple, List

def parse_input(f: str) -> List[Tuple[int, List[int]]]:
    with open(f, 'r') as file:
        ret = []
        for l in file:
            target, numbers = l.split(':')
            ret.append((int(target), [int(x) for x in numbers.split()]))
    return ret

def find_target(t: int, n: List[int], operators) -> int:
    """See if any combination of operators with numbers in n (keeping order) can reach the target, applying the operators from left to right"""

    if len(n) == 1:
        return n[0] == t
    wrong = 0
    # can walk through pairs, performing the operation and replacing target - output of pair as new target for list
    for i in range(1, len(n)):
        for op in operators:
            op = operators[op](n[i-1], n[i])
            if find_target(t, [op] + n[i+1:], operators):
                return True
            wrong += 1
        # if all operators fail, break early
        if wrong == len(operators):
            return False
    return False

def part1(f: str) -> int:
    operators = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}

    data = parse_input(f)
    return sum(k for k, v in data if find_target(k, v, operators))

def part2(f: str) -> int:
    operators = {'+': lambda x, y: x + y, '*': lambda x, y: x * y, '||': lambda x, y: int(str(x) + str(y))}

    data = parse_input(f)
    return sum(k for k, v in data if find_target(k, v, operators))
