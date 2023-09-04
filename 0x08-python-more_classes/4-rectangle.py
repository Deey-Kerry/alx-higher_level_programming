#!/usr/bin/python3
"""
4-rectangle.py
"""


class Rectangle:
    """Rectangle class instance. """

    def __init__(self, width=0, height=0):
        """Initialization of a Rectangle properties in contructor.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returning an informal string representation
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
        """Gets the width of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
