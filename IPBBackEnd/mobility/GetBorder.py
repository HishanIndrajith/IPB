import numpy as np


def get_boundary_points(grid):
    boundary_grid = np.ones(grid.shape)
    x = 0
    for rows in grid:
        y = 0
        for _ in rows:
            if x != 0 and y != 0 and x != grid.shape[0] - 1 and y != grid.shape[1] - 1:
                if grid[x, y] == 0 and (
                        grid[x - 1, y] == 1 or grid[x - 1, y - 1] == 1 or grid[x, y - 1] == 1 or
                        grid[x + 1, y - 1] == 1 or grid[x + 1, y] == 1 or grid[
                            x + 1, y + 1] == 1 or grid[x, y + 1] == 1 or grid[x - 1, y + 1] == 1):
                    boundary_grid[x, y] = 0
            y = y + 1
        x = x + 1
    return boundary_grid
