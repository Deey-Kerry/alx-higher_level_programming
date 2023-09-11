#!/usr/bin/python3
"""Writes a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        """MyInt has =="""
        return self.real != value

    def __ne__(self, value):
        """Not equal operator"""
        return self.real == value
