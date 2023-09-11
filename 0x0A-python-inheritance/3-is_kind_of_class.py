#!/usr/bin/python3
"""function that returns True/false if the object is an instance of"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified
    class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
