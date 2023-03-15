#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda item: item ** item, row)) for row in matrix])
