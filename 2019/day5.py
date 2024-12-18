from computer import Computer

with open('input/day5.txt', 'r') as data:
    data = list(map(int, data.read().split(',')))

tape = Computer(int_code=data, verbose=True)
tape.compute() #'1': Part one
tape.compute() #'5': Part two
