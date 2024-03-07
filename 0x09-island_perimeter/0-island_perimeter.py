#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    i = -1
    j = -1
    for row in grid:
        for e in row:
            if e == 1:
                i = grid.index(row)
                j = row.index(e)
                break
        if i != -1:
            break
    h = 1
    w = 1
    for row in range(i + 1, len(grid)):
        if grid[row][j] == 0:
            break
        h += 1
    for row in grid:
        k = 0
        for e in row:
            if e == 1:
                k += 1
        w = max(k, w)
    return 2 * (h + w)
