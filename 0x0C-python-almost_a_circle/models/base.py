#!/usr/bin/python3
"""Create Base class and it's definition"""
import json


class Base:
    """This is the base class. It has one class private attribute
    __nb_objects, whose value is 0 by default. It increases whenever
    a new instance of the base class is created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        Args:
            id(int): the id of a new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
