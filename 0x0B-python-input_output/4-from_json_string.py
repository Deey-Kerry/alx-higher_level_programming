#!/usr/bin/python3
"""
4-from_json_string.py

function that returns an object represented by a JSON string
"""


def from_json_string(my_str):
    """ returns an object represented by a JSON string"""
    import json

    return json.loads(my_str)
