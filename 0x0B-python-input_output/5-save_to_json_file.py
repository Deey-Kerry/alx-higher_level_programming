#!/usr/bin/python3
"""
5-save_to_json_file.py

function that writes an Obj to a text file, using a JSON rep
"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
