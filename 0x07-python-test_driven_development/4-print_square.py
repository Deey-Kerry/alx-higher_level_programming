#!/usr/bin/python3
"""Checks if a square-printing function."""


def print_square(size):
    """A function that prints a square with the # character.
    Args:
        size (int): Length/width of the square.
    Raises:
        TypeError: size != an integer.
        ValueError: size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
