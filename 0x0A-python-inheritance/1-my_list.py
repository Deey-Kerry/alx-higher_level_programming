#!/usr/bin/python3
"""
1-my_list.py

Writes a class MyList
which inherits from list and has public instance method to print sorted
"""


class MyList(list):
    """This class inherits from list

    methods:
    public instance method: print_sorted(self)
    """
    def print_sorted(self):
        """prints the list in ascending sort"""
        print(sorted(self))
