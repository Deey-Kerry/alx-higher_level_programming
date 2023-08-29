#!/usr/bin/python3
"""Defining class Square"""


class Square:
    """Main function of class starts"""

    def __init__(self, size=0):
        """Initializing class Square
        Args:
            size(int)
        """
        self.size = size

    @property
    def size(self):
        """defining the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defining the area of the Square"""
        return (self.__size * self.__size)
