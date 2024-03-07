#!/usr/bin/python3
"""
0. Island Perimeter
"""
from typing import List


def island_perimeter(grid: List[List]):
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
    l = 1
    for row in range(i + 1, len(grid)):
        if grid[row][j] == 0:
            break
        h += 1
    for row in grid:
        k = 0
        for e in row:
            if e == 1:
                k += 1
        l = max(k, l)
    return 2 * (h + l)

