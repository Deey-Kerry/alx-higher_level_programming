#!/usr/bin/python3
if __name__ == "__main__":
    """A program function that prints the number and list arguements"""
    import sys
    
    arg = sys.argv
    size = len(arg) - 1
    
    if size == 0:
        print("0 arguements.")
    elif size == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(size))
    for i in range(size):
            print("{}: {}".format(i + 1, arg[i + 1]))
