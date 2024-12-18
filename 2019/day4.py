import re

"""
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).
"""

RANGE = [246540, 787419]
TOTAL = 0

def get_digit(number, index):
    return int((number % pow(10, index + 1)) / pow(10, index))

def check_doubles(number, part):
    num = str(number)
    matches = re.findall('00+|22+|33+|44+|55+|66+|77+|88+|99+', num)
    if part == 'one':
        if matches and min([len(match) for match in matches]) >= 2:
            print('string {} is a match!'.format(num))
            return 1
    elif part == 'two':
        if matches and min([len(match) for match in matches]) == 2:
            print('string {} is a match!'.format(num))
            return 1
    else:
        assert False, 'Invalid part'

    return 0


def check_num(num):
    for digit in range(5):
        if get_digit(num, digit) < get_digit(num, digit+1):
            return 0
    print('num {} is a match!'.format(num))
    return 1

NUMBER = RANGE[0]
while NUMBER <= RANGE[1]:
    # increase base 10 until increasing left to right
    for i in range(5):
        while get_digit(NUMBER, 5-i) > get_digit(NUMBER, 4-i):
            NUMBER += pow(10, 4-i)

    # is 9 out?
    # TOTAL += check_num(NUMBER)
    TOTAL += check_doubles(NUMBER, 'two')
    NUMBER += 1

print(TOTAL)
