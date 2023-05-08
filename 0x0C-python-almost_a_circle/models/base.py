#!/usr/bin/python3
"""Create Base class and it's definition"""


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
