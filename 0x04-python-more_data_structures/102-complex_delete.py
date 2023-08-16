#!/usr/bin/python3
def complex_delete(my_dict, value):
    """a function that deletes keys with a specific value in dict"""
    temp = my_dict.copy()
    for keys, values in temp.items():
        if value == values:
            my_dict.pop(keys)
    return (my_dict)
