# Dijkstra's minimum cost path algorithm used
from skimage.graph import route_through_array
import json


def coord2pixel_offset(x1, y1, delta_x1, delta_y1, x, y):
    x_offset = int((x - x1) / delta_x1)
    y_offset = int((y - y1) / delta_y1)
    return x_offset, y_offset


def create_path(cost_surface_array, x1, y1, delta_x1, delta_y1, start_coord, stop_coord):
    # coordinates to array index
    start_coord_x = start_coord[0]
    start_coord_y = start_coord[1]
    start_index_x, start_index_y = coord2pixel_offset(x1, y1, delta_x1, delta_y1, start_coord_x, start_coord_y)

    stop_coord_x = stop_coord[0]
    stop_coord_y = stop_coord[1]
    stop_index_x, stop_index_y = coord2pixel_offset(x1, y1, delta_x1, delta_y1, stop_coord_x, stop_coord_y)
    path, cost = route_through_array(cost_surface_array, (start_index_y, start_index_x), (stop_index_y, stop_index_x),
                               geometric=True, fully_connected=True)
    return path, cost



