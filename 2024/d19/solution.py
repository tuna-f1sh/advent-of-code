from collections import defaultdict
from functools import cache
from typing import List, Tuple, Dict

def parse_input(f: str) -> Tuple[Dict[str, List[str]], List[str]]:
    with open(f, 'r') as file:
        towels_str, design_strs = file.read().split('\n\n')
    towels = towels_str.split(', ')
    towels_by_char = defaultdict(list)
    for t in towels:
        towels_by_char[t[0]].append(t)
    designs = design_strs.strip().split('\n')
    return towels_by_char, designs

@cache
def match_design(design: str) -> bool:
    if design == '':
        return True
    first = design[0]
    for towel in towels[first]:
        if design.startswith(towel) and match_design(design[len(towel):]):
            return True
    return False

@cache
def match_possible(design: str) -> int:
    if design == '':
        return 1
    first = design[0]
    count = 0
    for towel in towels[first]:
        if design.startswith(towel):
            count += match_possible(design[len(towel):])
    return count

towels, desired = parse_input('example')
assert sum(map(match_design, desired)) == 6
assert sum(map(match_possible, desired)) == 16

towels, desired = parse_input('input')
print(sum(map(match_design, desired)))
print(sum(map(match_possible, desired)))
