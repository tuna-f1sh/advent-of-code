from collections import defaultdict
from functools import cmp_to_key
from typing import Dict, List, Tuple, Set

def process_file(f: str) -> Tuple[Dict[int, Set[int]], List[int]]:
    int_rule_map = defaultdict(set)
    updates = []
    parsing_rules = True
    with open(f, 'r') as fh:
        for line in fh:
            if line.strip() == '':
                parsing_rules = False
                continue
            if parsing_rules:
                no, rule = line.strip().split('|')
                int_rule_map[int(no)].add(int(rule))
            else:
                updates.append([int(x) for x in line.strip().split(',')])

    return int_rule_map, updates

def part1(rule_map, updates) -> int:
    ret = 0

    # walk each update filling previous into set that for each number set is checked against rule_map: if any in set is in rule_map then the number came before it so update is invalid
    for update in updates:
        prev = set()
        for num in update:
            if num in rule_map:
                if prev & rule_map[num]:
                    break
            prev.add(num)
        else:
            # add middle index in update
            ret += update[len(update) // 2]

    return ret

def part2(rule_map, updates) -> int:
    def cmp(a, b):
        # if a is in b's rule_map then a comes before b
        if a in rule_map[b]:
            return 1
        return -1

    def is_sorted(page):
        return all(cmp(page[i], page[i + 1]) == -1 for i in range(len(page) - 1))

    return sum(
        sorted(page, key=cmp_to_key(cmp))[len(page) // 2]
        for page in updates if not is_sorted(page)
    )

rule_map, updates = process_file('input')
print(f"Part 1: {part1(rule_map, updates)}")
print(f"Part 2: {part2(rule_map, updates)}")
