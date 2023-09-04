#!/usr/bin/python3
"""class Rectangle that defines a rectangle
"""


class Rectangle:
    """Rectangle class definition.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Function that Initializes a Rectangle instannce in a contructor.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Function that Returns string representation of rectangle (#)
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Function that Returns internal string representation of Rectangle        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Function that Fires when a rectangle is destroyed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Function that Gets the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Function that Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function that Gets the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Function that Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that Calculates and returns the area of a Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Function that Calculates and returns the perimeter of a Rectangle        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
