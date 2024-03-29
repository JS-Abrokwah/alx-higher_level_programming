#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
        Divides all elements of a matrix by a given number and
        returns a new matrix.

        Parameters:
        matrix (list of list of int or float): The matrix to divide.
        div (int or float): The number to divide by.

        Returns:
        list of list of float: The new matrix with all elements divided by div.

        Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
        or if div is not a number.

        TypeError: If each row of the matrix is not the same size.
        ZeroDivisionError: If div is 0.
    """

    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(val / div, 2) for val in row] for row in matrix]
