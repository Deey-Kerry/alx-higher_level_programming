#!/usr/bin/python3
"""
Representation of a rectangle class
"""


class Rectangle:
    """A rectangle class """

    def __init__(self, width=0, height=0):
        """A function that initializes a Rectangle properties 
        """
        self.width = width
        self.height = height

    def __str__(self):
        """A function program that returns an informal string rep
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        record_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                record_str += '#'
            record_str += '\n'
        return record_str[:-1]

    @property
    def width(self):
        """A function that gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """A function that sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A function that gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """A function that sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that calculates the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """A function that calculates the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
