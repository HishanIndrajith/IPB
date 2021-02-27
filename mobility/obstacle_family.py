import numpy as np

grid = []
families = []
height = 0
width = 0


def partition_obstacles(grd):
    global grid
    global families
    global height
    global width
    grid = grd
    height = grid.shape[0]
    width = grid.shape[1]
    rest_point = (0, 0)
    row_id = 0
    for rows in grid:
        col_id = 0
        for column in rows:
            if column == 0:
                rest_point = (col_id, row_id)
                point_family = find_family_bdf(row_id, col_id)
                if len(point_family) > 0:
                    families.append(point_family)
            col_id = col_id + 1
        row_id = row_id + 1
    return families


def find_family_bdf(row_id, col_id):
    family = []
    queue = set([])
    queue.add((row_id, col_id))
    #     start processing queue
    while len(queue) != 0:
        current_cell = queue.pop()
        current_row = current_cell[0]
        current_col = current_cell[1]
        family.append([current_col, current_row])
        grid[current_row][current_col] = 1
        if current_row > 0 and grid[current_row - 1][current_col] == 0:
            queue.add((current_row - 1, current_col))
        if current_row > 0 and current_col < width - 1 and grid[current_row - 1][current_col + 1] == 0:
            queue.add((current_row - 1, current_col + 1))
        if current_col < width - 1 and grid[current_row][current_col + 1] == 0:
            queue.add((current_row, current_col + 1))
        if current_col < width - 1 and current_row < height - 1 and grid[current_row + 1][current_col + 1] == 0:
            queue.add((current_row + 1, current_col + 1))
        if current_row < height - 1 and grid[current_row + 1][current_col] == 0:
            queue.add((current_row + 1, current_col))
        if current_col > 0 and current_row < height - 1 and grid[current_row + 1][current_col - 1] == 0:
            queue.add((current_row + 1, current_col - 1))
        if current_col > 0 and grid[current_row][current_col - 1] == 0:
            queue.add((current_row, current_col - 1))
        if current_row > 0 and current_col > 0 and grid[current_row - 1][current_col - 1] == 0:
            queue.add((current_row - 1, current_col - 1))
    return family


# def find_family(row_id, col_id):
#     if 0 < row_id < height - 1 and 0 < col_id < width - 1:
#         family.append([col_id, row_id])
#         grid[row_id][col_id] = 1
#         if grid[row_id - 1][col_id] == 0:
#             find_family(row_id - 1, col_id)
#         if grid[row_id - 1][col_id + 1] == 0:
#             find_family(row_id - 1, col_id + 1)
#         if grid[row_id][col_id + 1] == 0:
#             find_family(row_id, col_id + 1)
#         if grid[row_id + 1][col_id + 1] == 0:
#             find_family(row_id + 1, col_id + 1)
#         if grid[row_id + 1][col_id] == 0:
#             find_family(row_id + 1, col_id)
#         if grid[row_id + 1][col_id - 1] == 0:
#             find_family(row_id + 1, col_id - 1)
#         if grid[row_id][col_id - 1] == 0:
#             find_family(row_id, col_id - 1)
#         if grid[row_id - 1][col_id - 1] == 0:
#             find_family(row_id - 1, col_id - 1)


def point_list_to_grid(point_list):
    family_grid = np.zeros(grid.shape)
    for cord in point_list:
        family_grid[cord[1], cord[0]] = 1
    return family_grid


def get_boundary_family(point_list):
    family_grid = point_list_to_grid(point_list)
    boundary_list = []
    x = 0
    for rows in grid:
        y = 0
        for _ in rows:
            if x != 0 and y != 0 and x != family_grid.shape[0] - 1 and y != family_grid.shape[1] - 1:
                if family_grid[x, y] == 1 and (
                        family_grid[x - 1, y] == 0 or family_grid[x - 1, y - 1] == 0 or family_grid[x, y - 1] == 0 or
                        family_grid[x + 1, y - 1] == 0 or family_grid[x + 1, y] == 0 or family_grid[
                            x + 1, y + 1] == 0 or family_grid[x, y + 1] == 0 or family_grid[x - 1, y + 1] == 0):
                    boundary_list.append([y, x])
            y = y + 1
        x = x + 1
    return boundary_list
