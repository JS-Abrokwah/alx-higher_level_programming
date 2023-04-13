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

    def to_json(self, attrs=None):
        """return dictionary representation of instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:"""
        for key, value in json.items():
            setattr(self, key, value)
