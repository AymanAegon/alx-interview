#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if len(grid) < 1:
        return 0
    h = 0
    w = 0
    arr = []
    for row in grid:
        if 1 in row:
            arr.append(1)
        else:
            arr.append(0)
    for e in arr:
        if e == 1:
            h += 1

    arr = [0] * len(grid[0])
    for row in grid:
        for e in range(len(row)):
            if row[e] == 1:
                arr[e] = 1
    for e in arr:
        if e == 1:
            w += 1
    # return (h, w)
    return 2 * (h + w)
