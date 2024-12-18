from computer import Computer

with open('input/day9.txt', 'r') as data:
    data = list(map(int, data.read().split(',')))

ex1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
ex2 = [1102,34915192,34915192,7,4,7,99,0]
ex3 = [104,1125899906842624,99]

tape = Computer(int_code=data, verbose=True, memory=10000)
tape.compute() #'1': Part one
