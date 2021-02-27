# Dijkstra's minimum cost path algorithm used
import numpy as np
import math
from mobility import ArrayToRaster

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
    path = route_through_array(cost_surface_array, (start_index_y, start_index_x), (stop_index_y, stop_index_x))
    return path


def dijkistra(array, start):
    height = array.shape[0]
    width = array.shape[1]
    array_this = np.copy(array)

    traceback_array = np.zeros((array.shape[0], array.shape[1], 1)).tolist()
    total_cost_array = np.ones_like(array) * 1e308
    queue = dict()
    queue[(start[0], start[1])] = 0
    total_cost_array[start[0], start[1]] = 0

    def get_minimum():
        min_dist = 1e308
        min_dist_element = tuple()
        for element in queue:
            dis = queue.get(element)
            if dis < min_dist:
                min_dist_element = element
                min_dist = dis
        return min_dist_element

    def get_cost(current_node_cost, next_node_cost, is_diagonal):
        k = 1
        if is_diagonal:
            k = math.sqrt(2)
        return k * (current_node_cost + next_node_cost) / 2

    def process_neighbour(row_id, col_id, direction, is_diagonal):
        next_cell_cost = array_this[row_id, col_id]
        next_cell_total_cost = current_cell_total_cost + get_cost(current_cell_cost, next_cell_cost, is_diagonal)
        if next_cell_total_cost == total_cost_array[row_id, col_id]:
            traceback_array[row_id][col_id].append(direction)
        if next_cell_total_cost < total_cost_array[row_id, col_id]:
            total_cost_array[row_id, col_id] = next_cell_total_cost
            queue[(row_id, col_id)] = next_cell_total_cost
            traceback_array[row_id][col_id] = []
            traceback_array[row_id][col_id] = [direction]
            #     start processing queue

    while len(queue) != 0:
        # print(traceback_array)
        current_cell = get_minimum()
        queue.pop(current_cell)
        current_row = current_cell[0]
        current_col = current_cell[1]
        current_cell_cost = array_this[current_row][current_col]
        current_cell_total_cost = total_cost_array[current_row][current_col]
        array_this[current_row][current_col] = 0

        if current_row > 0 and array_this[current_row - 1][current_col] > 0:
            process_neighbour(current_row - 1, current_col, 1, False)
        if current_row > 0 and current_col < width - 1 and array_this[current_row - 1][current_col + 1] > 0:
            process_neighbour(current_row - 1, current_col + 1, 2, True)
        if current_col < width - 1 and array_this[current_row][current_col + 1] > 0:
            process_neighbour(current_row, current_col + 1, 3, False)
        if current_col < width - 1 and current_row < height - 1 and array_this[current_row + 1][current_col + 1] > 0:
            process_neighbour(current_row + 1, current_col + 1, 4, True)
        if current_row < height - 1 and array_this[current_row + 1][current_col] > 0:
            process_neighbour(current_row + 1, current_col, 5, False)
        if current_col > 0 and current_row < height - 1 and array_this[current_row + 1][current_col - 1] > 0:
            process_neighbour(current_row + 1, current_col - 1, 6, True)
        if current_col > 0 and array_this[current_row][current_col - 1] > 0:
            process_neighbour(current_row, current_col - 1, 7, False)
        if current_row > 0 and current_col > 0 and array_this[current_row - 1][current_col - 1] > 0:
            process_neighbour(current_row - 1, current_col - 1, 8, True)
    return total_cost_array, traceback_array


#
# def get_path(shape, traceback_array, end):
#     path_array = np.zeros(shape)
#     row_id = end[0]
#     col_id = end[1]
#     while traceback_array[row_id][col_id][0] > 0:
#         path_array[row_id, col_id] = 1
#         if traceback_array[row_id][col_id][0] == 1:
#             row_id = row_id + 1
#         elif traceback_array[row_id][col_id][0] == 2:
#             row_id = row_id + 1
#             col_id = col_id - 1
#         elif traceback_array[row_id][col_id][0] == 3:
#             col_id = col_id - 1
#         elif traceback_array[row_id][col_id][0] == 4:
#             row_id = row_id - 1
#             col_id = col_id - 1
#         elif traceback_array[row_id][col_id][0] == 5:
#             row_id = row_id - 1
#         elif traceback_array[row_id][col_id][0] == 6:
#             row_id = row_id - 1
#             col_id = col_id + 1
#         elif traceback_array[row_id][col_id][0] == 7:
#             col_id = col_id + 1
#         elif traceback_array[row_id][col_id][0] == 8:
#             row_id = row_id + 1
#             col_id = col_id + 1
#     path_array[row_id, col_id] = 1
#     return path_array


def get_all_paths(shape, traceback_array, end):
    paths = np.zeros(shape)

    def find_next_node(row, col):
        while len(traceback_array[row][col]) == 1 and traceback_array[row][col][0] != 0:
            paths[row, col] = 1
            if traceback_array[row][col][0] == 1:
                row = row + 1
            elif traceback_array[row][col][0] == 2:
                row = row + 1
                col = col - 1
            elif traceback_array[row][col][0] == 3:
                col = col - 1
            elif traceback_array[row][col][0] == 4:
                row = row - 1
                col = col - 1
            elif traceback_array[row][col][0] == 5:
                row = row - 1
            elif traceback_array[row][col][0] == 6:
                row = row - 1
                col = col + 1
            elif traceback_array[row][col][0] == 7:
                col = col + 1
            elif traceback_array[row][col][0] == 8:
                row = row + 1
                col = col + 1
        return row, col

    row_id = end[0]
    col_id = end[1]
    queue = set([])
    queue.add((row_id, col_id))

    while len(queue) > 0:
        print(queue)
        cell = queue.pop()
        row = cell[0]
        col = cell[1]
        if len(queue) == 0 and traceback_array[row][col][0] == 0:
            break
        for each_dir in traceback_array[row][col]:
            x = False
            r = row
            c = col
            paths[row, col] = 1
            if r == 24 and c == 235:
                print(each_dir)
                x = True
            if each_dir == 1:
                r = r + 1
            elif each_dir == 2:
                r = r + 1
                c = c - 1
            elif each_dir == 3:
                c = c - 1
            elif each_dir == 4:
                r = r - 1
                c = c - 1
            elif each_dir == 5:
                r = r - 1
            elif each_dir == 6:
                r = r - 1
                c = c + 1
            elif each_dir == 7:
                c = c + 1
            elif each_dir == 8:
                r = r + 1
                c = c + 1
            t = find_next_node(r, c)
            if x:
                print(r, c, t, len(traceback_array[r][c]))
            queue.add(t)
    return paths


# def find_family_bdf(row_id, col_id):
#     family = []
#     queue = set([])
#     queue.add((row_id, col_id))
#     #     start processing queue
#     while len(queue) != 0:
#         current_cell = queue.pop()
#         current_row = current_cell[0]
#         current_col = current_cell[1]
#         family.append([current_col, current_row])
#         grid[current_row][current_col] = 1
#         if current_row > 0 and grid[current_row - 1][current_col] == 0:
#             queue.add((current_row - 1, current_col))
#         if current_row > 0 and current_col < width - 1 and grid[current_row - 1][current_col + 1] == 0:
#             queue.add((current_row - 1, current_col + 1))
#         if current_col < width - 1 and grid[current_row][current_col + 1] == 0:
#             queue.add((current_row, current_col + 1))
#         if current_col < width - 1 and current_row < height - 1 and grid[current_row + 1][current_col + 1] == 0:
#             queue.add((current_row + 1, current_col + 1))
#         if current_row < height - 1 and grid[current_row + 1][current_col] == 0:
#             queue.add((current_row + 1, current_col))
#         if current_col > 0 and current_row < height - 1 and grid[current_row + 1][current_col - 1] == 0:
#             queue.add((current_row + 1, current_col - 1))
#         if current_col > 0 and grid[current_row][current_col - 1] == 0:
#             queue.add((current_row, current_col - 1))
#         if current_row > 0 and current_col > 0 and grid[current_row - 1][current_col - 1] == 0:
#             queue.add((current_row - 1, current_col - 1))
#     return family


def route_through_array(array, start, end):
    start, end = tuple(start), tuple(end)
    costs, traceback_array = dijkistra(array, start)
    print('path')
    # print(costs)
    # print(traceback_array[0])
    # print(traceback_array[1])
    # print(traceback_array[2])
    # print(traceback_array[3])
    # print(traceback_array[4])
    path = get_all_paths(costs.shape, traceback_array, end)
    # print(path)

    # print(path)
    dim = (80.59049999999999,2.7988000000050304e-05,7.255960999999999, - 2.7670833333333827e-05)
    ArrayToRaster.save_2d_grid_as_raster(costs, dim[0], dim[1], dim[2], dim[3],
                                         'mobility\\tempfiles\\costs2.tif')
    # ArrayToRaster.save_2d_grid_as_raster(traceback_array, dim[0], dim[1], dim[2], dim[3],
    #                                      'mobility\\tempfiles\\traceback_array.tif')
    # return path
    return path
