import numpy as np


def get_latitude_grid(elevation_array, y1, delta_y1):
    # x - longitude
    # y - latitude
    latitude_grid = np.zeros(elevation_array.shape)
    for x in range(elevation_array.shape[0]):
        latitude_grid[x, :] = "{0:.15f}".format(y1 + delta_y1 * x)
    return latitude_grid


def get_longitude_grid(elevation_array, x1, delta_x1):
    # x - longitude
    # y - latitude
    longitude_grid = np.zeros(elevation_array.shape)
    for y in range(elevation_array.shape[1]):
        longitude_grid[:, y] = "{0:.15f}".format(x1 + delta_x1 * y)
    return longitude_grid
