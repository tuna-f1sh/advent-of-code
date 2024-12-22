from collections import deque, defaultdict
from typing import List

def parse_input(f: str) -> List[int]:
    with open(f, 'r') as fh:
        return list(map(int, fh.readlines()))

def secret(number: int):
    prune = lambda x: x % 16777216
    mix = lambda x, s: x ^ s
    s1 = prune(mix(number << 6, number))
    s2 = prune(mix(s1 >> 5, s1))
    return prune(mix(s2 << 11, s2))

def part1(numbers: List[int]):
    for _ in range(2000):
        numbers = list(map(secret, numbers))

    return numbers

def windows(num):
    last, changes = num % 10, deque(maxlen=4)
    consecutives = {}

    for _ in range(3):
        num = secret(num)
        price = num % 10
        changes.append(price - last)
        last = price

    for _ in range(1997):
        num = secret(num)
        price = num % 10
        changes.append(price - last)
        last = price
        if tuple(changes) not in consecutives:
            consecutives[tuple(changes)] = last

    return consecutives

def part2(numbers: List[int]):
    best = defaultdict(int)
    for num in numbers:
        consecutives = windows(num)
        for four_tuple, banana in consecutives.items():
            best[four_tuple] += banana

    return max(best.values())

assert part1([1, 10, 100, 2024]), [8685429, 4700978, 15273692, 8667524]
print(sum(part1(parse_input('input'))))
print(part2(parse_input('input')))
