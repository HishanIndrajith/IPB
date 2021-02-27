# All rights reserved (c)
# Hishan Indrajith Adikari
# IPB Decision Support Tool

# Enemy range of threat generating

import numpy as np
import math

changes = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
default_range_of_threat = 33  # approx 100m, max threat spread in normal flat terrain with no features. unit grid cell units
# threat_decrement_normal = 1 per cell unit
# 33 >= threat value >= 0
# following values are threat value per cell unit
threat_decrement_building_max = 3
threat_decrement_grassland = 0.6
threat_decrement_shrubland = 0.8
# threat_decrement_woodland_and_unknown = 1, so need to assign as it is redundant
threat_decrement_medium_forest = 1.8
threat_decrement_high_forest = 2.5
threat_decrement_elevation_increment = 2
threat_decrement_elevation_decrement = 0.2
building_floor_height_average = 2
range_increment_per_floor = 6


def get_enemy_border_grid(building_grid):
    def is_border(r, c):
        is_enemy = 0
        is_at_border = 0
        if int(building_grid[r, c] / 1000) == 1:
            is_enemy = 1
            for [r_change, c_change] in changes:
                if building_grid.shape[0] > (r + r_change) >= 0 and building_grid.shape[1] > (c + c_change) >= 0 \
                        and int(building_grid[r + r_change, c + c_change] / 1000) != 1:
                    is_at_border = 1
                    break
        return is_enemy * is_at_border

    row_id = 0
    border_grid = np.zeros(building_grid.shape, np.int)
    for rows in building_grid:
        column_id = 0
        for _ in rows:
            border_grid[row_id, column_id] = is_border(row_id, column_id)
            column_id = column_id + 1
        row_id = row_id + 1
    return border_grid


def get_building_cells(cell, enemy_border_grid):
    height = enemy_border_grid.shape[0]
    width = enemy_border_grid.shape[1]
    queue = set()
    queue.add(cell)
    cell_list = []

    def scan_neighbour(r, c):
        queue.add((r, c))
        enemy_border_grid[r, c] = 0
        cell_list.append((r, c))

    while len(queue) != 0:
        current_cell = queue.pop()
        current_row = current_cell[0]
        current_col = current_cell[1]
        if current_row > 0 and enemy_border_grid[current_row - 1][current_col] == 1:
            scan_neighbour(current_row - 1, current_col)
        if current_col < width - 1 and enemy_border_grid[current_row][current_col + 1] == 1:
            scan_neighbour(current_row, current_col + 1)
        if current_row < height - 1 and enemy_border_grid[current_row + 1][current_col] == 1:
            scan_neighbour(current_row + 1, current_col)
        if current_row > 0 and current_col > 0 and enemy_border_grid[current_row][current_col - 1] > 0:
            scan_neighbour(current_row - 1, current_col - 1)
    return cell_list


def update_range_of_threat(building_cell, building_range_of_threat, threat_decrement_array, elevation_grid,
                           building_height_grid, range_of_threat):
    cell_r = building_cell[0]
    cell_c = building_cell[1]
    this_cell_building_height = building_height_grid[building_cell]
    building_height_gap_grid = building_height_grid - this_cell_building_height
    threat_decrement_building_grid = np.ones_like(building_height_grid, np.int)
    threat_decrement_building_grid = np.where(building_height_gap_grid >= 0,
                                              threat_decrement_building_max, threat_decrement_building_grid)
    threat_decrement_array_cell = np.where(building_height_grid > 0, threat_decrement_building_grid,
                                           threat_decrement_array)

    this_cell_elevation = elevation_grid[building_cell]
    elevation_gap_grid = elevation_grid - this_cell_elevation
    threat_decrement_elevation_grid = np.ones_like(elevation_grid, np.int)

    min_elevation_to_block_threat = this_cell_building_height * building_floor_height_average
    threat_decrement_array_cell = np.where(elevation_gap_grid > min_elevation_to_block_threat,
                                           threat_decrement_array_cell + threat_decrement_elevation_increment,
                                           threat_decrement_array_cell)
    threat_decrement_array_cell = np.where(elevation_gap_grid < 0,
                                           threat_decrement_array_cell - threat_decrement_elevation_decrement,
                                           threat_decrement_array_cell)

    def get_threat_decrement(current_node_cost, next_node_cost, is_diagonal):
        k = 1
        if is_diagonal:
            k = math.sqrt(2)
        return k * (current_node_cost + next_node_cost) / 2

    visited = np.zeros(threat_decrement_array_cell.shape, np.bool)
    queue = dict()
    queue[(cell_r, cell_c)] = range_of_threat
    building_range_of_threat[cell_r, cell_c] = range_of_threat

    def get_maximum():
        max_dist = 0
        max_dist_element = tuple()
        for element in queue:
            dis = queue.get(element)
            if dis > max_dist:
                max_dist_element = element
                max_dist = dis
        return max_dist_element

    def process_neighbour(is_diagonal):
        row_id = coord[0]
        col_id = coord[1]
        next_cell_decrement = threat_decrement_array_cell[row_id, col_id]
        next_cell_threat = current_cell_threat - get_threat_decrement(current_cell_threat_decrement,
                                                                      next_cell_decrement, is_diagonal)
        if next_cell_threat > building_range_of_threat[row_id, col_id]:
            building_range_of_threat[row_id, col_id] = next_cell_threat
            queue[(row_id, col_id)] = next_cell_threat

    while len(queue) != 0:
        current_cell = get_maximum()
        queue.pop(current_cell)
        visited[current_cell] = True
        current_row = current_cell[0]
        current_col = current_cell[1]
        current_cell_threat_decrement = threat_decrement_array_cell[current_row][current_col]
        current_cell_threat = building_range_of_threat[current_row][current_col]
        for [r_change, c_change] in changes:
            coord = (current_row + r_change, current_col + c_change)
            if threat_decrement_array.shape[0] > (current_row + r_change) >= 0 and threat_decrement_array.shape[1] > (
                    current_col + c_change) >= 0 \
                    and not visited[coord]:
                process_neighbour(abs(r_change * c_change) == 1)
    return building_range_of_threat


def get_building_range_of_threat(cell, enemy_border_grid, threat_decrement_array, elevation_grid, building_height_grid):
    building_height = building_height_grid[cell]
    range_of_threat = default_range_of_threat + range_increment_per_floor * (building_height - 1)
    divisor = range_of_threat / 10
    cell_list = get_building_cells(cell, enemy_border_grid)
    building_range_of_threat = np.zeros(enemy_border_grid.shape)
    for building_cell in cell_list:
        building_range_of_threat = update_range_of_threat(building_cell, building_range_of_threat,
                                                          threat_decrement_array, elevation_grid, building_height_grid,
                                                          range_of_threat)
    return building_range_of_threat / divisor


def get_enemy_threat_range_grid(building_grid, vegetation_grid, elevation_grid):
    building_grid_2d = building_grid[:, :, 0]
    vegetation_grid_2d = vegetation_grid[:, :, 0]
    elevation_grid_2d = elevation_grid[:, :, 0]
    building_height_grid = np.mod(building_grid_2d, 1000)
    threat_decrement_array = np.ones_like(building_grid_2d, np.int)
    threat_decrement_array = np.where(vegetation_grid_2d == 1, threat_decrement_grassland, threat_decrement_array)
    threat_decrement_array = np.where(vegetation_grid_2d == 2, threat_decrement_shrubland, threat_decrement_array)
    threat_decrement_array = np.where(vegetation_grid_2d == 4, threat_decrement_medium_forest, threat_decrement_array)
    threat_decrement_array = np.where(vegetation_grid_2d == 5, threat_decrement_high_forest, threat_decrement_array)
    enemy_border_grid = get_enemy_border_grid(building_grid_2d)
    enemy_threat_range_grid = np.zeros(enemy_border_grid.shape, np.int)
    row_id = 0
    for rows in enemy_border_grid:
        column_id = 0
        for column in rows:
            if column == 1:
                # one building found
                threat = get_building_range_of_threat((row_id, column_id),
                                                      enemy_border_grid,
                                                      threat_decrement_array,
                                                      elevation_grid_2d,
                                                      building_height_grid)
                enemy_threat_range_grid = np.where(threat > enemy_threat_range_grid, threat, enemy_threat_range_grid)
            column_id = column_id + 1
        row_id = row_id + 1
    # replace threat maximum to enemy building inside
    enemy_threat_range_grid = np.where(
        (building_grid_2d > 1000) & (building_grid_2d < 2000) & (enemy_threat_range_grid < 10),
        10, enemy_threat_range_grid)
    # replace mac 10 threat to places where threats add together
    enemy_threat_range_grid = np.where(enemy_threat_range_grid > 10, 10, enemy_threat_range_grid)
    return enemy_threat_range_grid
