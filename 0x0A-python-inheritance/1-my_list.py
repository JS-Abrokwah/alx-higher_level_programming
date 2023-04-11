#!/usr/bin/python3

"""
    defines class MyList that inherits list
    with method print_sorted(), that prints the list,
    but sorted (ascending sort)
"""


class MyList(list):
    """Inherits list object and implement the sort method"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
