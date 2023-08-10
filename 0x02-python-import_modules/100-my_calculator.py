#!/usr/bin/python3
if __name__ == "__main__":
    """A program that imports all functions from the file calculator"""
    from calculator_1 import add, sub, mul, div
    from sys

    arg = sys.argv 
    if len(arg) -1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if arg[2] not in list(ops.keys()):
        print('Unknown operator. Available operators: +, -, *, /')
        sys.exit(1)

        num1 = int(arg[1])
        num2 = int(argv[3])
        print("{} {} {} =  {}".format(num1, arg[2], num2, ops[arg[2]](a, b)))
