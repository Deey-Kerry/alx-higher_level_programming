#!/usr/bin/python3
"""class Square defined based on 1-square.py"""


class Square:
    """Definition of Square"""

    def __init__(self, size=0):
        """Square initialization"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
