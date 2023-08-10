#!/usr/bin/python3
if __name__ == "__main__":
    """A program function that prints the number and list arguements"""
    import sys
    
    arg = sys.argv
    count = len(arg) - 1
    
    if count > 1:
        print("{} arguements:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, arg[i]))
    elif count == 0:
        print("{} arguements:".format(count))

    else:
        print("{} arguements:".format(count))
        print("{}: {}".format(i, arg[1]))
