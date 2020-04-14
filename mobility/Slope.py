# Developed by Hishan Indrajith Adikari on 6th April 2020
import math
import numpy as np


def slope(elevation_array):
    # x - longitude
    # y - latitude
    slope_grid = np.zeros((elevation_array.shape[0], elevation_array.shape[1], 1))
    row_id = 0
    for rows in elevation_array:
        column_id = 0
        for column in rows:
            slope_cells_around = []
            if column_id != 0:
                left_slope = two_point_slope(elevation_array[row_id, column_id-1], column, 1)
                slope_cells_around.append(left_slope)
            if row_id != 0:
                top_slope = two_point_slope(elevation_array[row_id-1, column_id], column, 1)
                slope_cells_around.append(top_slope)
            if column_id != elevation_array.shape[1]-1:
                right_slope = two_point_slope(elevation_array[row_id, column_id+1], column, -1)
                slope_cells_around.append(right_slope)
            if row_id != elevation_array.shape[0]-1:
                bottom_slope = two_point_slope(elevation_array[row_id+1, column_id], column, -1)
                slope_cells_around.append(bottom_slope)
            if row_id != 0 and column_id != 0:
                top_left_slope = two_point_slope(elevation_array[row_id-1, column_id-1], column, 1)
                slope_cells_around.append(top_left_slope)
            if row_id != 0 and column_id != elevation_array.shape[1]-1:
                top_right_slope = two_point_slope(elevation_array[row_id-1, column_id+1], column, -1)
                slope_cells_around.append(top_right_slope)
            if row_id != elevation_array.shape[0]-1 and column_id != elevation_array.shape[1]-1:
                bottom_right_slope = two_point_slope(elevation_array[row_id + 1, column_id + 1], column, 1)
                slope_cells_around.append(bottom_right_slope)
            if row_id != elevation_array.shape[0]-1 and column_id != 0:
                bottom_left_slope = two_point_slope(elevation_array[row_id + 1, column_id - 1], column, -1)
                slope_cells_around.append(bottom_left_slope)

            total_slope = 0
            for slp in slope_cells_around:
                total_slope = total_slope + slp
            slope_grid[row_id, column_id] = abs(total_slope/len(slope_cells_around))
            column_id = column_id + 1
        row_id = row_id + 1
    return slope_grid


def two_point_slope(point, center, priority):
    elevation_this_cell = center[2]
    elevation_other_cell = point[2]
    distance_points = distance(center[1], center[0], point[1], point[0])
    point_slope = (priority * (elevation_this_cell - elevation_other_cell)) / distance_points
    return point_slope


def distance(x1, y1, x2, y2):
    # Great-circle distance theory
    # https://en.wikipedia.org/wiki/Great-circle_distance
    # d = r*cos−1(siny1 * siny2 + cosy1*cosy2*cosΔx)
    x1_r = math.radians(x1)
    x2_r = math.radians(x2)
    y1_r = math.radians(y1)
    y2_r = math.radians(y2)
    r = 6378137  # earth's radius
    d = r * math.acos(math.sin(y1_r) * math.sin(y2_r) + math.cos(y1_r) * math.cos(y2_r) * math.cos(x1_r - x2_r))
    return d
