import os
from functools import wraps
from time import time


def get_input_raw(day: int, example: bool = False) -> str:
    """
    Get the raw input for the year and day

    :param day int: day to get
    :param example bool: example file rather than real
    """
    day_str = 'day{}_example.txt' if example else 'day{}.txt'

    return open(os.path.join('../input', day_str.format(day)), 'r').read()

def get_input(day: int, example: bool = False, split: str = '\n') -> list[str]:
    """
    Get the input for the year and day

    :param day int: day to get
    :param example bool: example file rather than real
    """
    day_str = 'day{}_example.txt' if example else 'day{}.txt'

    return open(os.path.join('../input', day_str.format(day)), 'r').read().strip().split(split)

def get_ints(day, **kwargs):
    """
    Return list of ints from input file

    :param day int: day to get
    :param example bool: example file rather than real
    """
    data = get_input(day, **kwargs)

    return [*map(int, data)]

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__} took: {te-ts:2.4f} sec")
        return result
    return wrap
