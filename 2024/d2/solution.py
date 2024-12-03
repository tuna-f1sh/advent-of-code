import sys

def read_reports(filename: str):
    with open(filename) as f:
        reports = []
        for line in f:
            levels = [int(x) for x in line.split()]
            reports.append(levels)

    return reports

def part1(reports: list[list[int]], part2: bool = False) -> int:
    safe = 0 

    for report in reports:
        d = 0
        skip_count = 0 if part2 else 1
        for last, n in zip(report, report[1:]):
            delta = (last - n)
            # capture direction on first and multiply to keep delta in that direction - or it will flip if changes
            if d == 0:
                d = -1 if delta < 0 else 1
            delta *= d
            if delta < 1:
                if skip_count > 0:
                    break
                skip_count += 1
            if delta > 3:
                if skip_count > 0:
                    break
                skip_count += 1
        else:
            safe += 1

    return safe

file = sys.argv[1] if len(sys.argv) > 1 else 'input'
print(part1(read_reports(file)))
print(part1(read_reports(file), True))
