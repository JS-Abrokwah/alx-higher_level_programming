#!/usr/bin/python3
"""Definition for Square class"""


class Square:
    """The Square class"""

    def __init__(self, size=0):
        """Initializes new Square instance"""
        self.size = size

    @property
    def size(self):
        """Getter for size property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and return the size of Square"""
        return (self.__size * self.__size)
