#!/usr/bin/python3
"""function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    import json

    return json.dumps(my_obj)
