#!/usr/bin/python3

"""
creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """ creates an object from json file"""
    import json
    with open(filename) as myfile:
        return json.load(myfile)
