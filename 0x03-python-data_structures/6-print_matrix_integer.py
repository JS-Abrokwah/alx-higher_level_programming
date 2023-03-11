#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        last = len(matrix[i]) - 1
        for x in matrix[i]:
            if x == matrix[i][last]:
                print("{:d}".format(x))
            else:
                print("{:d}".format(x), end=" ")
    print("")
