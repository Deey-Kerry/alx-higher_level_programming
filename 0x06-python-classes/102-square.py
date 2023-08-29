#!/usr/bin/python3
"""compares two Squares"""


class Square:
    """ Represents class square."""

    def __init__(self, size=0):
        """Initialization of a square."""
        self.size = size

    @property
    def size(self):
        """checks for the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines area of the Square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Equals to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to a Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than < to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to <= in a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Comparison > in a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Comparison >= in a Square."""
        return self.area() >= other.area()
