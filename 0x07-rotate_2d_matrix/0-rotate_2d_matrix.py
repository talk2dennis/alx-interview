#!/usr/bin/python3
"""
    A module to rotate matrix 90deg clockwise
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    N = len(matrix[0])
    return [[matrix[N - 1 - y][x] for y in range(N)] for x in range(N)]
