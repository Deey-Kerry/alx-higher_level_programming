#!/usr/bin/python3
"""
10-square.py

Write a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size):
        """Initializes new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
