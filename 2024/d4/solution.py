example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def make_letter_map(file: str) -> dict[tuple[int, int], str]:
    with open(file) as f:
        return {(i, j): c for i, line in enumerate(f) for j, c in enumerate(line.strip())}

def word_search(m: dict[tuple[int, int], str], start: tuple[int,int], dirc: tuple[int,int], chars: list[str]) -> bool:
    x, y = start
    i, j = dirc
    if (x, y) in m and m[(x, y)] == chars[0]:
        if len(chars) == 1:
            return True
        return word_search(m, (x + i, y + j), dirc, chars[1:])
    return False

def part1(file: str) -> int:
    letter_map = make_letter_map(file)
    ret = 0

    for cord, letter in letter_map.items():
        if letter == "X":
            # look around neighbours for M in all directionsthen keep searching in that direction for AS
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    start = (cord[0] + i, cord[1] + j)
                    if word_search(letter_map, start, (i, j), ["M", "A", "S"]):
                        ret += 1
                        break

    return ret
