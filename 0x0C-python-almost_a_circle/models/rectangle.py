#!/usr/bin/python3

""" This file creates a Rectangle class that inherits from Base
The rectangle class defines a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Defines Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ intitalize a new Rectangle instance
        Args:
            width(int): The width of the new Rectangle instance
            height(int): The height of the new Rectangle instance
            x(int): The x coordinate of the hew Rectangle instance
            y(int): The y coordinate of the new Rectangle instance
            id(int): The new Rectangle instance's id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """Getters"""
    @property
    def width(self):
        """ A width getter """
        return self.__width

    @property
    def height(self):
        """ A height getter """
        return self.__height

    @property
    def x(self):
        """ A x coordinate getter """
        return self.__x

    @property
    def y(self):
        """ A y coordinate getter """
        return self.__y

    """ Setters """
    @width.setter
    def width(self, value):
        """A setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """A setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """A setter for x coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """A setter for y coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
