#!/usr/bin/python3
"""Definition of Square based on 2-square.py"""


class Square:
    """Representation of class Square"""

    def __init__(self, size=0):
        """Initialization of Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defines area of the Square"""
        return (self.__size * self.__size)
