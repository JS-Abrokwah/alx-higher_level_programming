#!/usr/bin/python3

def add_integer(a, b=98):

    """
        Add two integers

        :param a: an integer or a float
        :param b: an integer or a float (default 98)
        :raises TypeError: if a or b is not an integer or a float
        :return: the sum of a and b, as an integer

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
