#!/usr/bin/python3
"""Definition for Square class"""


class Square:
    """The Square class"""

    def __init__(self, size=0):
        """Initializes new Square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and return the size of Square"""
        return (self.__size * self.__size)
