from Calculator.Addition import addition
from Calculator.Division import division


def proportion(data):
    p = len(data)
    height = 0
    for values in data:
        if height > 64:
            addition(height)
    return division(values, p)