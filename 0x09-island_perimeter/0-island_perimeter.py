#!/bin/usr/python3
""" a module to calculate the land perimeter of an island """


def island_perimeter(grid):
    """ A function that calculates the perimeter of an island """

    if not grid:
        return 0
    perimeter = 0
    for lst in grid:
        if not all(isinstance(x, int) for x in lst):
            return 0
        for i in range(len(lst)):
            if lst[i] == 1:
                if i == 0 or lst[i - 1] == 0:
                    perimeter += 1
                if i == len(lst) - 1 or lst[i + 1] == 0:
                    perimeter += 1
                if grid.index(lst) == 0 or grid[grid.index(lst) - 1][i] == 0:
                    perimeter += 1
                if grid.index(lst) == len(grid) - 1 or grid[grid.index(lst) + 1][i] == 0:
                    perimeter += 1
    return perimeter
    