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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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

    def area(self):
        """
            Calculates and return the area of a rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Displays a rectangle instance with '#' charater
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Update a Rectangle instance

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs: keyword arguments
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        pass
                    else:
                        self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        pass
                    else:
                        self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def __str__(self):
        """Returns the string representation of rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x, self.__y,
                                                        self.__width,
                                                        self.__height))
