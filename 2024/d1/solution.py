from typing import List, Tuple
from collections import Counter

def make_lists(file: str = 'd1/input') -> Tuple[List[int], List[int]]:
    """
    Takes a text file with two columns of integers and returns them as two lists.

    Sorts the lists in ascending order by checking if the first element is greater than the second element on insertion.

    Example data:

    12823   12823
    74540   88907
    37687   50218
    """

    with open(file, 'r') as f:
        data = f.readlines()

    list1 = []
    list2 = []

    def check_insert_pos(l: List[int], n: int) -> int:
        """
        Works down the list from the end to find the position to insert the new number.
        """
        for i in range(len(l) - 1, -1, -1):
            if l[i] < n:
                return i + 1
        return 0

    for line in data:
        a, b = line.split()
        a, b = int(a), int(b)

        if len(list1) == 0:
            list1.append(a)
            list2.append(b)
            continue
        if a > list1[-1]:
            list1.append(a)
        else:
            list1.insert(check_insert_pos(list1, a), a)
        if b > list2[-1]:
            list2.append(b)
        else:
            list2.insert(check_insert_pos(list2, b), b)

    return list1, list2

def part2(l1: List[int], l2: List[int]) -> int:
    counter = Counter(l2)
    ret = 0
    for v in l1:
        ret += counter[v] * v

    return ret

l1, l2 = make_lists()
part1 = sum([abs(a - b) for a, b in zip(l1, l2)])
print(f"Part 1: {part1}")
print(f"Part 2: {part2(l1, l2)}")
