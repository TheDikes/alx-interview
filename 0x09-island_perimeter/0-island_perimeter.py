#!/usr/bin/python3
"""
A function returning the perimeter of an island in grid
"""
def island_perimeter(grid):
    """
    A function returning the perimeter of an island in grid.

    Args:
    grid (List[List[int]]): A list of lists representing the grid with 0s for water and 1s for land.

    Returns:
    int: The perimter of the island.
    """

    if not grid or len(grid) == 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for cols in range(cols):
            if grid[row][col] == 1:
                # count the top boundary 
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                # count the left boundary 
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                # count the right boundary 
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

                # count the bottom boundary 
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter


