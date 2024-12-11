"""As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""

from math import log10, floor

def blink(stones: dict):
    new_stones = {}
    for stone, n in stones.items():
        if stone == 0:
            new_stones[1] = n + new_stones.get(1, 0)
            continue
        n_digits = floor(log10(stone)) + 1
        if n_digits % 2 == 0:
            left = stone // 10 ** (n_digits // 2)
            right = stone - left * 10 ** (n_digits // 2)
            new_stones[left] = n + new_stones.get(left, 0)
            new_stones[right] = n + new_stones.get(right, 0)
        else:
            new_stones[2024 * stone] = n + new_stones.get(2024 * stone, 0)
    return new_stones

def blinker(stones: dict, count=25):
    for _ in range(count):
        stones = blink(stones)
    return sum(stones.values())

with open("input") as f:
    stones = [int(x) for x in f.readline().strip().split()]
    stones = {stone: stones.count(stone) for stone in stones}
print(f"Part 1: {blinker(stones)}")
print(f"Part 2: {blinker(stones, 75)}")
