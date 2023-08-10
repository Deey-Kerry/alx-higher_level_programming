#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """Function that does exactly the same as below Python bytecode"""

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
