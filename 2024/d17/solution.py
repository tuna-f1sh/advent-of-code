import enum

class Opcode(enum.Enum):
    Adv = 0
    Bxl = 1
    Bst = 2
    Jnz = 3
    Bxc = 4
    Out = 5
    Bdv = 6
    Cdv = 7

class Computer():
    OPERANDS = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 'A',
        5: 'B',
        6: 'C',
    }

    def __init__(self, file_path: str, ia: int = 0, ib: int = 0, ic: int = 0):
        self.registers = {
            'A': ia,
            'B': ib,
            'C': ic,
        }
        self.pc = 0
        self.output = []
        self.load_program(file_path)

    def __repr__(self):
        return f'Program: {self.program}, A: {self.registers["A"]}, B: {self.registers["B"]}, C: {self.registers["C"]}, PC: {self.pc}, Output: {self.output}'

    def __str__(self):
        output = ','.join(map(str, self.output))
        return f"{output}"

    def load_program(self, file_path: str):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.registers['A'] = int(lines[0].split(': ')[1])
            self.registers['B'] = int(lines[1].split(': ')[1])
            self.registers['C'] = int(lines[2].split(': ')[1])
            self.program = list(map(int, lines[4].split(': ')[1].split(',')))

    def run(self):
        while self.pc < len(self.program):
            opcode = Opcode(self.program[self.pc])
            operand = self.program[self.pc + 1]
            self.op(opcode, operand)

    def op(self, opcode: Opcode, operand: int):
        # print(f'Executing {opcode} with operand {operand}')
        match opcode:
            case Opcode.Adv:
                self.registers['A'] = int(self.registers['A'] / 2 ** self.get_combo(self.OPERANDS[operand]))
            case Opcode.Bdv:
                self.registers['B'] = int(self.registers['A'] / 2 ** self.get_combo(self.OPERANDS[operand]))
            case Opcode.Cdv:
                self.registers['C'] = int(self.registers['A'] / 2 ** self.get_combo(self.OPERANDS[operand]))
            case Opcode.Bxl:
                # reg B XOR reg operand
                self.registers['B'] = self.registers['B'] ^ operand
            case Opcode.Bst:
                # combo operand mod 8
                self.registers['B'] = self.get_combo(self.OPERANDS[operand]) % 8
            case Opcode.Jnz:
                if self.registers['A'] != 0:
                    self.pc = operand
                else:
                    self.pc += 2
            case Opcode.Bxc:
                # reg B XOR reg C
                self.registers['B'] = self.registers['B'] ^ self.registers['C']
            case Opcode.Out:
                self.output.append(self.get_combo(self.OPERANDS[operand]) % 8)

        if opcode != Opcode.Jnz:
            self.pc += 2

    def get_combo(self, operand):
        if isinstance(operand, int):
            if operand <= 3:
                return operand
            raise ValueError(f'Invalid operand: {operand}')
        if operand not in self.registers:
            raise ValueError(f'Invalid operand: {operand}')
        return self.registers[operand]

c = Computer('input')
c.run()
print(f"Finished running computer: {c}")
