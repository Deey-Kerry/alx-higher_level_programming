#!/usr/bin/env python3
def no_c(my_string):
    """a function that removes all characters c  from a string."""
    new_string = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            new_string += i
        return new_string

