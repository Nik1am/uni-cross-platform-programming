#!/usr/bin/env python

from functools import reduce

lst = [1, 3, 4, 6, 10, 11, 15, 12, 14]


def product(x: int, y: int):
    return x * y


# 1:
print("1:", lst, "->", reduce(product, lst))

# 2:
print("2:", lst, "->", reduce(max, lst))

# i believe list comprehension approach is not possible here...
