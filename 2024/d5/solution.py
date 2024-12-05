from collections import defaultdict
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

print(f"Part 1: {part1(*process_file('input'))}")
