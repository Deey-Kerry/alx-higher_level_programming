#!/usr/bin/python3


def magic_calculation(a, b):
    """Python function that does exactly the same as the following Python bytecode"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception as e:
            result = b + a
            break
    return (result)
