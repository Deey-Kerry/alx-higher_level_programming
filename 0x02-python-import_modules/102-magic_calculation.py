#!/usr/bin/python3

def magic_calculation(a, b):
    """Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode"""

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
