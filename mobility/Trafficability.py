import numpy as np

max_slope = 0.2


def get_trafficability_grid(all_overlays_grid):
    trafficability_grid = np.zeros((all_overlays_grid.shape[0], all_overlays_grid.shape[1]))
    row_id = 0
    for rows in all_overlays_grid:
        column_id = 0
        for column in rows:
            trafficability_grid[row_id, column_id] = trafficability_of_cell_levels(column)
            column_id = column_id + 1
        row_id = row_id + 1
    trafficability_grid[0, :] = 7
    trafficability_grid[:, 0] = 7
    trafficability_grid[trafficability_grid.shape[0] - 1, :] = 7
    trafficability_grid[:, trafficability_grid.shape[1] - 1] = 7
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


def trafficability_of_cell_levels(cell):
    slope = cell[3]
    vegetation = cell[4]
    building = cell[5]
    water = cell[6]
    road = cell[7]
    # mobility levels = {1, 2, 3, 4, 5, 6, 7}
    trafficability = None
    if slope <= 0.05 or vegetation == 1:  # grassland
        trafficability = 2
    if slope > 0.05 or vegetation == 2 or vegetation == 6:  # shrubland, unknown vegetation
        trafficability = 3
    if slope > 0.1 or vegetation == 3:  # woodland
        trafficability = 4
    if slope > 0.15 or vegetation == 4 or water == 1:  # medium density forest
        trafficability = 5
    if slope > 0.2 or vegetation == 5:  # high density forest, deep water
        trafficability = 6
    if building == 1:
        trafficability = 7
    if road == 1:  # roads
        trafficability = 1
    return trafficability
