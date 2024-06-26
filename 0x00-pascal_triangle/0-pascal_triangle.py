#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        p_row = triangle[-1]

        new_row = [1] + [p_row[j - 1] + p_row[j] for j in range(1, i)] + [1]
        triangle.append(new_row)
    return triangle
