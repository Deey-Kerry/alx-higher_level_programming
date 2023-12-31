#!/usr/bin/python3
"""
function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
