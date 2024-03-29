#!/usr/bin/python3

"""Creates a Locked Class"""

class LockedClass:
    """
    prevents the user from dynamically creating new
    instance attributes, except if the new instance
    attribute is called first_name
    """

    __slot__ = ["first_name"]
