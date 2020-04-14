import numpy as np

max_slope = 0.2


def get_trafficability_grid(all_overlays_grid):
    trafficability_grid = np.zeros((all_overlays_grid.shape[0], all_overlays_grid.shape[1]))
    row_id = 0
    for rows in all_overlays_grid:
        column_id = 0
        for column in rows:
            trafficability_grid[row_id, column_id] = trafficability_of_cell(column)
            column_id = column_id + 1
        row_id = row_id + 1
    return trafficability_grid


def trafficability_of_cell(cell):
    trafficability = 1  # GO
    slope = cell[3]
    vegetation = cell[4]
    building = cell[5]
    water = cell[6]
    road = cell[7]
    if slope > max_slope or vegetation >= 3 or building == 1 or water == 1:
        trafficability = 0  # NO GO
    if road == 1:
        trafficability = 1  # GO
    return trafficability
