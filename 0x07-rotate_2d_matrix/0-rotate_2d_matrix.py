#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""
    new_matrix = []

    for i in range(len(matrix[0])):
        arr = []
        for row in matrix:
            arr.append(row[i])
        arr.reverse()
        new_matrix.append(arr)

    matrix.clear()
    for row in new_matrix:
        matrix.append(row)
