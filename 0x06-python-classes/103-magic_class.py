#!/usr/bin/python3
"""function to match MagicClass"""

import math


class MagicClass:
    """Representation of a circle in MagicClass"""

    def __init__(self, radius=0):
        """Initialization of the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """function that checks for the area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """function that checks the circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
