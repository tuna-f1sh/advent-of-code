import inputs

def find_first_last_digit(string: str) -> int:
    """
    >>> find_first_last_digit("1abc2")
    12
    """
    ret = None

    for c in string:
        if c.isdigit():
            if ret is None:
                ret = [c, c]
            else:
                ret[1] = c

    if ret:
        return int("".join(ret))
    else:
        raise ValueError("No pair")

word_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def find_replace_word_digit(string: str) -> str:
    def replace_slice(string: str, part: str):
        for word, digit in word_digit.items():
            if word in part:
                new_string = string.replace(word, digit)
                if new_string != string:
                    return (new_string, True)

        return (string, False)

    # longest digit word is 5 letters so scan from start in this chunk for first
    # digit word
    for i in range(0, len(string)):
        part = string[i:i+5]
        string, found = replace_slice(string, part)
        if found:
            break
    # do the same from the end for the last digit word
    for i in range(len(string)-5, 0, -1):
        part = string[i:i+5]
        string, found = replace_slice(string, part)
        if found:
            break
    return string

def part1(puzzle_input: list[str]) -> int:
    """
    >>> day1_input = inputs.get_input(1)
    >>> part1(day1_input)
    56506
    """
    ret = 0

    for s in puzzle_input:
        ret += find_first_last_digit(s)

    return ret

def part2(puzzle_input: list[str]) -> int:
    """
    >>> part2(["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen",])
    281
    """
    ret = 0
    for s in puzzle_input:
        ret += find_first_last_digit(find_replace_word_digit(s))

    return ret

day1_input = inputs.get_input(1)
print(f"Part 1: {part1(day1_input)}")
print(f"Part 2: {part2(day1_input)}")
