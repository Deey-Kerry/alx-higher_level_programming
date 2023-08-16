#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    sorted_keys = sorted(a_dictionary.keys())
    for k in sorted_keys:
        value = a_dictionary[k]
        print("{}: {}".format(k, value))
