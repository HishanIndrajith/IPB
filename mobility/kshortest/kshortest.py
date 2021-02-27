import numpy as np
import collections
import math
import copy
import datetime


def find_k_shortest_paths(array, s, t, k):
    count = np.zeros(array.shape)
    temp_path_list = collections.deque()  # B
    final_path_list = collections.deque()  # P

    # Algorithm

    temp_path_list.append((s, [s], 0))

    def shortest_path():
        min_len = 1e308
        min_len_path = tuple()
        for path in temp_path_list:
            if path[2] < min_len:
                min_len = path[2]
                min_len_path = path
        return min_len_path

    def get_cost(current_node_cost, next_node_cost, is_diagonal):
        x = 1
        if is_diagonal != 0:
            x = math.sqrt(2)
        return x * (current_node_cost + next_node_cost) / 2

    def is_coord_available_in_path(path, coord):
        for path_coord in path:
            if path_coord == coord:
                return True
        return False

    def get_new_path(current_path, row_change, col_change):
        row_max = array.shape[0] - 1
        col_max = array.shape[1] - 1
        coord = current_path[0]
        new_row = coord[0] + row_change
        new_col = coord[1] + col_change
        new_coord = (new_row, new_col)
        path = current_path[1]
        if 0 <= new_row <= row_max and 0 <= new_col <= col_max and not is_coord_available_in_path(path, new_coord):
            cost = current_path[2]
            path.append(new_coord)
            new_cost = cost + get_cost(array[coord], array[new_coord], row_change * col_change)
            new_path_data = (new_coord, path, new_cost)
            return new_path_data
        return None

    changes = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    while len(temp_path_list) > 0 and count[t] < k:
        current_shortest = shortest_path()
        temp_path_list.remove(current_shortest)
        current_shortest_coord = current_shortest[0]
        count[current_shortest_coord] = count[current_shortest_coord] + 1
        if current_shortest_coord == t:
            final_path_list.append(current_shortest)
        if count[current_shortest_coord] <= k:
            for [r_change, c_change] in changes:
                current_path_copy = copy.deepcopy(current_shortest)
                new_path = get_new_path(current_path_copy, r_change, c_change)
                if new_path is not None:
                    temp_path_list.append(new_path)
    return final_path_list


def coord2pixel_offset(x1, y1, delta_x1, delta_y1, x, y):
    x_offset = int((x - x1) / delta_x1)
    y_offset = int((y - y1) / delta_y1)
    return x_offset, y_offset


def create_path(cost_surface_array, x1, y1, delta_x1, delta_y1, start_coord, stop_coord):
    print('started k-shortest algorithm')
    a = datetime.datetime.now()
    # coordinates to array index
    start_coord_x = start_coord[0]
    start_coord_y = start_coord[1]
    start_index_x, start_index_y = coord2pixel_offset(x1, y1, delta_x1, delta_y1, start_coord_x, start_coord_y)

    stop_coord_x = stop_coord[0]
    stop_coord_y = stop_coord[1]
    stop_index_x, stop_index_y = coord2pixel_offset(x1, y1, delta_x1, delta_y1, stop_coord_x, stop_coord_y)
    paths = find_k_shortest_paths(cost_surface_array, (start_index_y, start_index_x), (stop_index_y, stop_index_x), 10)
    # paths = find_k_shortest_paths(cost_surface_array, (82,75), (24, 235), 100)
    # return json.dumps(make_geo_json(paths, x1, y1, delta_x1, delta_y1))
    b = datetime.datetime.now()
    print('time taken')
    print(b - a)
    return make_geo_json(paths, x1, y1, delta_x1, delta_y1)


def make_geo_json(paths, x1, y1, delta_x1, delta_y1):
    feature_array = []
    for path in paths:
        path_array = path[1]
        cost = path[2]
        path_array = np.array(path_array, float).T
        path_array = path_array + 0.5
        path_array[0] = (path_array[0] * delta_y1) + y1
        path_array[1] = (path_array[1] * delta_x1) + x1
        path_array = np.flip(path_array, 0)
        path_array = path_array.T
        path_array = path_array.tolist()
        feature = {
            "type": "Feature",
            "properties": {
                "cost": cost
            },
            "geometry": {
                "type": "LineString",
                "coordinates": path_array
            }
        }
        feature_array.append(feature)
    json_data = {
        "name": "minimum_cost_path",
        "type": "FeatureCollection",
        "features": feature_array
    }
    return json_data


# ar = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 5, 5, 5, 5, 5, 5, 1],
#                [1, 1, 1, 1, 1, 1, 1, 1]])
#
# k = 2
# s = (0, 0)
# t = (7, 7)
# final_paths = find_k_shortest_paths(ar, s, t, k)
# for final_path in final_paths:
#     print(final_path)
