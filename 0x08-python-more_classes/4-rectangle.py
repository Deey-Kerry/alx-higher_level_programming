#!/usr/bin/python3
"""Representation of a Rectangle class."""


class Rectangle:
    """Class that represents a rectangle."""

    def __init__(self, width=0, height=0):
        """A function that initializes a new Rectangle.
        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """A function that gets/sets the width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A function that gets/sets the height of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function that returns the area of a Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """A function that returns the perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """A function that returns the printable representation of the Rectangle.
        It represents the rectangle with the # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """A function that returns the string representation of rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
