import math


FILE = open("./input/day1.txt", "r")
SUM = 0


def calculate_fuel(mass):
    return math.floor((mass / 3)) - 2


def calculate_module_fuel(module):
    total = 0
    print("fuel for {}".format(module))

    while calculate_fuel(module) > 0:
        module = calculate_fuel(module)
        total += module
        print(int(module))

    return total


for line in FILE.readlines():
    SUM += calculate_module_fuel(int(line))

print(SUM)
