#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    arr = ["1"]
    lastRow = ""
    row = ""
    for i in range(n - 1):
        row = "1"
        for j in range(len(lastRow) - 1):
            row += str(int(lastRow[j]) + int(lastRow[j + 1]))
        row += "1"
        lastRow = row
        arr.append(row)

    return arr