#!/usr/bin/python3

"""
3-to_json_string.py
returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """Returns the json representation of my_obj"""
    import json
    return json.dumps(my_obj)
