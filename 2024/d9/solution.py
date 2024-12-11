from typing import List, Optional, Tuple

def parse_disk_map(f: str) -> List[int]:
    with open(f) as fh:
        return [int(x) for x in list(fh.read().strip())]

def build_disk_map(disk_map: List[int]) -> List[Tuple[Optional[int], int]]:
    dm = []
    id = 0
    is_odd = len(disk_map) % 2 != 0
    if is_odd:
        end = len(disk_map) - 1
    else:
        end = len(disk_map)
    for i in range(0, end, 2):
        disk, space = disk_map[i], disk_map[i+1]
        dm.append((id, disk))
        if space > 0:
            dm.append((None, space))
        id += 1
    if is_odd:
        dm.append((id, disk_map[-1]))
    return dm

def compact_disk(disk: List[Tuple[Optional[int], int]]) -> List[Optional[int]]:
    """Take file block one at a time from end (right) and move to empty space starting far left"""
    j = 0
    for i in range(len(disk)-1, 0, -1):
        if j >= i:
            break
        if disk[i][0] is None:
            continue
        else:
            while disk[j] is not None and j < i:
                j += 1
            if disk[j] is None:
                disk[j] = disk[i]
                disk[i] = None
    return disk[:j+1]

def calc_checksum(compacted: List[int]) -> int:
    """Disk ID * index sum"""
    return sum([c * i for i, c in enumerate(compacted)])

def part1(f: str) -> int:
    disk_map = parse_disk_map(f)
    print(disk_map)
    disk = build_disk_map(disk_map)
    print(disk)
    compacted = compact_disk(disk)
    print(compacted)
    return calc_checksum(compacted)
