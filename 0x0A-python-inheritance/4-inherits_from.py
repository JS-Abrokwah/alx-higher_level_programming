#!/usr/bin/python3

"""
    Defines a function the determine if an
    object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
