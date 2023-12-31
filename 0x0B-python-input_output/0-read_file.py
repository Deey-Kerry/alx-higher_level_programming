#!/usr/bin/python3
"""
0-read_file.py

a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
