example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def find_instructions(s: str, p2=False) -> list[tuple[int, int]]:
    """Finds mul(x,y) instructions in a string"""

    instructions = []
    do = True
    for i in range(len(s)):
        # mul(x,y) is 8 characters long
        if i + 8 > len(s):
            break
        if s[i:i+4] == "mul(" and do:
            start = i + 4
            x = None
            y = None
            j = start
            for j in range(start, len(s)):
                if s[j].isdigit():
                    continue
                else:
                    if s[j] == "," and x is None:
                        x = s[start:j]
                        start = j + 1
                    elif s[j] == ")" and x is not None:
                        y = s[start:j]
                        instructions.append((int(x), int(y)))
                        break
                    else:
                        break
            i = j
        if p2:
            if s[i:i+3] == "do(":
                do = True
            if s[i:i+6] == "don't(":
                do = False
    return instructions

def part1() -> int:
    with open("input") as f:
        s = f.read()

    instructions = find_instructions(s)
    return sum(x * y for x, y in instructions)

def part2() -> int:
    with open("input") as f:
        s = f.read()

    instructions = find_instructions(s, p2=True)
    return sum(x * y for x, y in instructions)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
