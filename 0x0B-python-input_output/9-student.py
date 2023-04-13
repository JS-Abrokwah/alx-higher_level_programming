#!/usr/bin/python3

"""
Defines class Student that defines a student with
public instance attributes: first_name, last_name and age
"""


class Student:
    """ A student Class"""

    def __init__(self, first_name, last_name, age):
        """initialize instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation of instance"""
        return self.__dict__
