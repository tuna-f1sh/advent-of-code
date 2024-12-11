"""As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each simultaneously change according to the first applicable rule in this list:

    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""

from typing import List

def blink(stones: List[bytearray]):
    new_stones = []
    append = new_stones.append
    for stone in stones:
        # replace with 1
        if stone == b'0':
            append(bytearray(b'1'))
            continue
        # even digits, split
        length = len(stone)
        if length % 2 == 0:  # even digits, split
            half = length // 2
            left = stone[:half]
            right = stone[half:]
            left_start = 0
            while left_start < len(left) and left[left_start] == 48:
                left_start += 1
            right_start = 0
            while right_start < len(right) and right[right_start] == 48:
                right_start += 1
            append(left[left_start:] or bytearray(b'0'))
            append(right[right_start:] or bytearray(b'0'))
        else:
            num = 0
            for byte in stone:
                num = num * 10 + (byte - 48)
            num *= 2024
            append(bytearray(str(num).encode('ascii')))
    return new_stones

def blinker(stones: List[bytearray], count=75):
    for _ in range(count):
        stones = blink(stones)
    return len(stones)

if __name__ == "__main__":
    with open("input") as f:
        stones = [bytearray(x, "ascii") for x in f.readline().strip().split()]
    print(f"Part 1: {blinker(stones, 25)}")
    print(f"Part 2: {blinker(stones, 75)}")
