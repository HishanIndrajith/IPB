import numpy as np


def get_enemy_border_grid(building_grid):
    # todo add logic
    return np.zeros(building_grid.shape)


def get_building_cells(cell, enemy_border_grid):
    # todo add logic
    return []


def update_range_of_threat(building_cell, building_range_of_threat):
    max_range_of_threat = 33  # approx 100m
    # todo add logic - here building_range_of_threat updates using geometric distance
    pass


def get_building_range_of_threat(cell, enemy_border_grid):
    cell_list = get_building_cells(cell, enemy_border_grid)
    building_range_of_threat = np.zeros(enemy_border_grid.shape)
    for building_cell in cell_list:
        update_range_of_threat(building_cell, building_range_of_threat)
    return np.zeros(enemy_border_grid.shape)


def get_enemy_threat_range_grid(building_grid):
    enemy_border_grid = get_enemy_border_grid(building_grid)
    enemy_threat_range_grid = np.zeros(enemy_border_grid.shape, np.int)
    row_id = 0
    for rows in enemy_border_grid:
        column_id = 0
        for column in rows:
            if column == 1:
                # one building found
                enemy_threat_range_grid = enemy_threat_range_grid + \
                                          get_building_range_of_threat((row_id, column_id), enemy_border_grid)
            column_id = column_id + 1
        row_id = row_id + 1






