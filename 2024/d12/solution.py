from typing import Dict, Set
from collections import defaultdict

def parse_plot(f: str) -> Dict[str, Set[complex]]:
    """Parse the plot from the input file into a dictionary with plot plant as keys containing a set of complex coordinates plot squares."""
    data = defaultdict(set)
    with open(f, 'r') as file:
        for y, line in enumerate(file.readlines()):
            for x, plot in enumerate(list(line.strip())):
                data[plot].add(x + y * 1j)
    return data

def flood_fill(square: complex, squares: Set[complex], visited: Set[complex]) -> Set[complex]:
    """
    Perform a flood-fill algorithm to find all connected squares forming a single region.
    """
    region = set()
    stack = [square]
    while stack:
        sq = stack.pop()
        if sq not in visited:
            visited.add(sq)
            region.add(sq)
            neighbors = [sq + d for d in [1, -1, 1j, -1j]]
            for n in neighbors:
                if n in squares and n not in visited:
                    stack.append(n)
    return region


def calculate_perimeter(region: Set[complex]) -> int:
    """
    Calculate the perimeter of a region.
    Each square has four sides, and a side counts toward the perimeter if it does not have an adjacent square in the region.
    """
    perimeter = 0
    for square in region:
        neighbors = [square + d for d in [1, -1, 1j, -1j]]
        open_sides = sum(1 for n in neighbors if n not in region)
        perimeter += open_sides
    return perimeter


def calc_prices(plots: Dict[str, Set[complex]]) -> int:
    """
    Calculate the total price for fencing the regions of each type of plant plot.
    The price is the perimeter of the plot's region.
    """
    total_price = 0
    for plot_type, squares in plots.items():
        visited = set()
        for square in squares:
            if square not in visited:
                region = flood_fill(square, squares, visited)
                area = len(region)
                perimeter = calculate_perimeter(region)
                total_price += area * perimeter
                print(f"Plot {plot_type}: {area=}, {perimeter=} {total_price=} {region=}")
    return total_price

if __name__ == '__main__':
    plot = parse_plot('input')
    print(plot)
    print(f"Part 1: {calc_prices(plot)}")
    # print(f"Part 2: {len(plot)}") # TODO calculate_sides(region)
