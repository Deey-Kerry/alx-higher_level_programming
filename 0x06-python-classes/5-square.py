#!/usr/bin/python3
"""class Square defined"""


class Square:
    """class Square starts here"""

    def __init__(self, size):
        """Initializes the Square"""
        self.size = size

    @property
    def size(self):
        """Definition of Square __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of a square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the Square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
