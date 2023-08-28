#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """a function that prints the first x elements of a list and only integers."""
    sum_total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            sum_total += 1
        except (ValueError, TypeError):
            pass
        print()
        return (sum_total)
