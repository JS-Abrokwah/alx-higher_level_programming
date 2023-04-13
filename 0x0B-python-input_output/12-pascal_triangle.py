#!/usr/bin/python3

"""Creates a pascal's triangle"
"""


def pascal_triangle(n):
    """create a pascal's triangle of height equal to n"""

    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) < n:
        row_ele = pascal[-1]
        row = [1]

        for i in range(len(row_ele) - 1):
            row.append(row_ele[i] + row_ele[i + 1])
        row.append(1)
        pascal.append(row)

    return pascal
