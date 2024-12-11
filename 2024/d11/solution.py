"""As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""

from math import log, floor
from typing import List

def blink(stones: List[int]):
    new_stones = []
    for stone in stones:
        # replace with 1
        if stone == 0:
            new_stones.append(1)
        elif (digits := (floor(log(stone, 10)) + 1)) % 2 < 1:
            left = stone // 10 ** (digits // 2)
            right = stone % 10 ** (digits // 2)
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone * 2024)
    return new_stones

def blinker(stones: List[int], count=25):
    for i in range(count):
        stones = blink(stones)
        print(f"Blinked: {i}")
    return len(stones)

with open("input") as f:
    stones = [int(x) for x in f.readline().strip().split()]
print(f"Part 1: {blinker(stones)}")
print(f"Part 2: {blinker(stones, 75)}")
