from collections import Counter

def parse_grid(f: str) -> dict:
    """Parse the grid from the input file into a dictionary with complex coordinates as keys."""
    return {x + y * 1j: int(val) for y, line in enumerate(open(f).readlines()) for x, val in enumerate(line.strip())}

grid = parse_grid('input')

def step(ans, h, pos):
    if pos in grid and h == grid[pos]:
        if h == 9:
            breakpoint()
            ans[pos] += 1
        else:
            for d in [1, -1, 1j, -1j]:
                step(ans, h+1, pos+d)
    return ans

# Find all trails starting from each position with height 0
# recursively stepping along trail (increasing height) until we reach the end. Keeping track of the number of times we reach a 9 height and the position (score) and distict (rating)
trails = [step(Counter(), 0, pos) for pos, h in grid.items() if h == 0]

print(f"Part 1: {sum(len(trail) for trail in trails)}")
print(f"Part 2: {sum(trail.total() for trail in trails)}")
