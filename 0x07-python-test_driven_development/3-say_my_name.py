#!/usr/bin/python3

def say_my_name(first_name, last_name=""):

    """
    Prints "My name is" followed by the first 
    name and last name (if provided).

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
        TypeError: If either of the inputs is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
