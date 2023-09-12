#!/usr/bin/python3
"""A function that returns the list of available attributes"""


def lookup(obj):
    """returns list of available attributes and methods of object"""
    return (dir(obj))
