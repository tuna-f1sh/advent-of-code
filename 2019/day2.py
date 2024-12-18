from itertools import combinations

"""
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""


FILE = open("./input/day2.txt", "r")
PROGRAM = [int(i) for i in FILE.read().strip().split(",")]
print(PROGRAM)


def run_intcode(program):
    position = 0
    op_code = program[position]

    while op_code is not 99:
        print("running opcode {} at intcode position {}".format(op_code, position))
        if op_code is 1 or 2:
            index = [program[position + 1], program[position + 2]]
            output = program[position + 3]
            print("indexes {} output {}".format(index, output))
            if op_code is 1:
                program[output] = program[index[0]] + program[index[1]]
            else:
                program[output] = program[index[0]] * program[index[1]]
        position += 4
        op_code = program[position]

    return program


def part_one(program):
    program[1] = "12"
    program[2] = "2"
    return run_intcode(program)


"""
not the most efficient n^2 linear search
"""
def part_two(program, addr, output):
    for noun, verb in combinations(range(100), 2):
        test = program[:]
        test[1:3] = [noun, verb]
        result = run_intcode(test)
        print("output {}".format(result[0]))
        if result[addr] == output:
            return 100 * noun + verb
    return -1


def print_result(program):
    print("final program {}".format(program))
    print("left a position zero {}".format(program[0]))


# PART_ONE = part_one(PROGRAM)
# print_result(PART_ONE)

print(part_two(PROGRAM, 0, 19690720))
