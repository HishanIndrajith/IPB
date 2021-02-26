import copy
from mobility import leastcostpath
import numpy as np
from mobility.threats import ChokePoints
from skimage.graph import route_through_array


def get_independent_shortest_paths(trafficability_grid, restricted_grid, x1, y1, delta_x1, delta_y1, start_coord, stop_coord):
    max_factor = 5
    paths = []
    trafficability_grid_copy = copy.deepcopy(trafficability_grid)
    lc_path, lc_cost = leastcostpath.create_path(trafficability_grid_copy, x1, y1, delta_x1, delta_y1, start_coord,
                                                 stop_coord)
    paths.append(copy.copy(lc_path))
    limit = max_factor * lc_cost
    start = lc_path[0]
    end = lc_path[len(lc_path) - 1]
    non_choke_point_set = ChokePoints.non_choke_points(restricted_grid, lc_path)
    while True:
        lc_path_inv = np.array(non_choke_point_set).T
        trafficability_grid_copy[lc_path_inv[0], lc_path_inv[1]] = 100000
        trafficability_grid_copy[start] = trafficability_grid[start]
        trafficability_grid_copy[end] = trafficability_grid[end]
        lc_path, lc_cost = leastcostpath.create_path(trafficability_grid_copy, x1, y1, delta_x1, delta_y1, start_coord,
                                                     stop_coord)
        non_choke_point_set = ChokePoints.non_choke_points(restricted_grid, lc_path)
        if lc_cost > limit:
            break
        paths.append(copy.copy(lc_path))
    return correct_paths(paths, trafficability_grid, start, end)


def choke_point_based_shortest_paths(trafficability_grid, restricted_grid, x1, y1, delta_x1, delta_y1, start_coord,
                                     stop_coord):
    max_factor = 3
    paths = []
    trafficability_grid_copy = copy.deepcopy(trafficability_grid)
    lc_path, lc_cost = leastcostpath.create_path(trafficability_grid_copy, x1, y1, delta_x1, delta_y1, start_coord,
                                                 stop_coord)
    paths.append((copy.copy(lc_path), copy.copy(lc_cost)))
    limit = max_factor * lc_cost
    start = lc_path[0]
    end = lc_path[len(lc_path) - 1]
    choke_point_set = ChokePoints.get_choke_points(restricted_grid, lc_path)
    while len(choke_point_set) != 0:
        print(lc_cost, limit)
        choke_point_sets_inv = np.array(choke_point_set).T
        trafficability_grid_copy[choke_point_sets_inv[0], choke_point_sets_inv[1]] = 50000
        trafficability_grid_copy[start] = trafficability_grid[start]
        trafficability_grid_copy[end] = trafficability_grid[end]
        lc_path, lc_cost = leastcostpath.create_path(trafficability_grid_copy, x1, y1, delta_x1, delta_y1, start_coord,
                                                     stop_coord)
        choke_point_set = ChokePoints.get_choke_points(restricted_grid, lc_path)
        if lc_cost > limit or len(choke_point_set) == 0:
            break
        paths.append((copy.copy(lc_path), copy.copy(lc_cost)))
    return paths


def correct_paths(paths, trafficability_grid, start, end):
    new_paths = []
    array = np.ones(trafficability_grid.shape, np.int) * 100000
    path_id = 0
    for path in paths:
        path_id = path_id + 1
        path_inv = np.array(path).T
        array[path_inv[0], path_inv[1]] = trafficability_grid[path_inv[0], path_inv[1]]

    for i in range(len(paths)):
        path_section, cost = route_through_array(array, start, end, geometric=True,
                                                 fully_connected=True)
        new_paths.append((path_section, cost))
        max_section = cut_point(path_section, array)
        remove_section(path_section, max_section, array)

    return new_paths


def remove_section(path, section, array):
    in_section = False
    for cell in path:
        if cell == section[0]:
            in_section = True
        if cell == section[1]:
            in_section = False
        if in_section:
            array[cell] = 100000


def cut_point(path, array):
    r_max = array.shape[0]
    c_max = array.shape[1]
    max_section = (path[2], path[len(path) - 3], 0)
    sections = []
    threshold = 6
    while len(sections) == 0 and threshold >= 0:
        sections = []
        changes = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        inside_section = False
        length = 0
        start_r = 0
        start_c = 0
        for cell in path:
            r = cell[0]
            c = cell[1]
            empty_count = 0
            for [r_change, c_change] in changes:
                if 0 <= (r + r_change) < r_max and 0 <= (c + c_change) < c_max and array[r + r_change, c + c_change] == 100000:
                    empty_count = empty_count + 1
            if not inside_section and empty_count >= threshold:
                inside_section = True
                start_r = cell[0]
                start_c = cell[1]
                length = 0
            if inside_section and empty_count >= threshold:
                length = length + 1
            if inside_section and empty_count < threshold:
                inside_section = False
                sections.append(((start_r, start_c), (cell[0], cell[1]), length))

        max_length = 0

        for section in sections:
            if section[2] > max_length:
                max_section = section
                max_length = section[2]
        threshold = threshold - 2
    return max_section
