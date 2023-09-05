#!/usr/bin/python3
"""Checks a name-printing function."""


def say_my_name(first_name, last_name=""):
    """A function that prints a name.
    Args:
        first_name (str): First name string to print.
        last_name (str): Last name string to print.
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
