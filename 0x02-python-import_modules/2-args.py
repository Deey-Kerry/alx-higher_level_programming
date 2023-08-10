#!/usr/bin/python3
if __name__ == "__main__":
    """A program function that prints the number and list arguements"""
    import sys
    
    arg = sys.argv
    count = len(arg) - 1
    
    if count == 0:
        print("0 arguements.")
    elif count == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(count))
    for i in range(count):
            print("{}: {}".format(i + 1, arg[i + 1]))
