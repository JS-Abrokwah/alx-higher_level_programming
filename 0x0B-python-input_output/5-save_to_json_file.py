#!/usr/bin/python3

"""
writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes a text to a file using json representation"""
    import json
    with open(filename, 'w', encoded='utf-8') as myjsonfile:
        json.dump(my_obj, myjsonfile)
