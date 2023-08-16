#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ a function that replaces all occurrences of an element"""
    return [replace if search == n else n for n in my_list]
