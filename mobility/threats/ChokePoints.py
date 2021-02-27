# Choke Point Algorithm by Hishan Indrajith for IPB project
# 19th May 2020
import math

choke_threshold = 4  # around 12m length


def get_choke_points(restricted_grid, path):
    print('Choke Point Algorithm Started')
    # back_cell - front_cell -->
    front_cell = None
    back_cell = None
    chokes_point_sets = []
    chokes_point_set = []  #todo added for path algorithm
    continuous_set = []
    total_choke_value_of_set = 0
    for cell in path:
        back_cell = front_cell
        front_cell = cell
        if back_cell is not None and front_cell is not None:
            # get two displacements
            v_d = front_cell[0] - back_cell[0]  # vertical displacement
            h_d = front_cell[1] - back_cell[1]  # horizontal displacement
            # get direction type
            directions = None
            is_diagonal = False
            if (abs(h_d) - abs(v_d)) == 1:
                directions = (1, 0, -1, 0)
            elif (abs(h_d) - abs(v_d)) == -1:
                directions = (0, 1, 0, -1)
            elif (h_d * v_d) == 1:
                directions = (1, -1, -1, 1)
                is_diagonal = True
            elif (h_d * v_d) == -1:
                directions = (1, 1, -1, -1)
                is_diagonal = True
            # start scanning two sides
            is_choke, len1, len2 = scan(restricted_grid, back_cell, directions, is_diagonal)
            cell_choke_value = 1 + 2 * choke_threshold - (len1 + len2)
            if is_choke:
                chokes_point_set.append(back_cell) #todo added for later algorithm
                continuous_set.append(back_cell)
                total_choke_value_of_set = total_choke_value_of_set + cell_choke_value
            elif len(continuous_set) > 0:
                chokes_point_sets.append((continuous_set, total_choke_value_of_set))
                continuous_set = []
                total_choke_value_of_set = 0
    print('Choke Point Algorithm Finished')
    return chokes_point_set  # todo decide set or sets


def non_choke_points(restricted_grid, path):
    # back_cell - front_cell -->
    r_max = restricted_grid.shape[0]
    c_max = restricted_grid.shape[1]
    front_cell = None
    back_cell = None
    non_chokes_point_set = []
    for cell in path:
        back_cell = front_cell
        front_cell = cell
        if back_cell is not None and front_cell is not None:
            # get two displacements
            v_d = front_cell[0] - back_cell[0]  # vertical displacement
            h_d = front_cell[1] - back_cell[1]  # horizontal displacement
            # get direction type
            directions = None
            is_diagonal = False
            if (abs(h_d) - abs(v_d)) == 1:
                directions = (1, 0, -1, 0)
            elif (abs(h_d) - abs(v_d)) == -1:
                directions = (0, 1, 0, -1)
            elif (h_d * v_d) == 1:
                directions = (1, -1, -1, 1)
                is_diagonal = True
            elif (h_d * v_d) == -1:
                directions = (1, 1, -1, -1)
                is_diagonal = True
            # start scanning two sides
            is_choke, len1, len2 = scan(restricted_grid, back_cell, directions, is_diagonal, r_max, c_max)
            if not is_choke:
                non_chokes_point_set.append(back_cell)
    return non_chokes_point_set


def scan(restricted_grid, cell, directions, is_diagonal, r_max, c_max):
    restricted_1_found = False
    restricted_1_distance = 0
    restricted_2_found = False
    restricted_2_distance = 0
    distance_travelled = 0
    distance_step = 1
    if is_diagonal:
        distance_step = math.sqrt(2)
    current_cell1 = (cell[0], cell[1])
    current_cell2 = (cell[0], cell[1])
    while distance_travelled <= choke_threshold:
        distance_travelled = distance_travelled + distance_step
        current_cell1 = (current_cell1[0] + directions[0], current_cell1[1] + directions[1])
        current_cell2 = (current_cell2[0] + directions[2], current_cell2[1] + directions[3])
        if not (r_max > current_cell1[0] >= 0 and c_max > current_cell1[1] >= 0 and r_max > current_cell2[0] >= 0 and c_max > current_cell2[1] >= 0):
            break
        if not restricted_1_found and restricted_grid[current_cell1] == 1:
            restricted_1_found = True
            restricted_1_distance = distance_travelled
        if not restricted_2_found and restricted_grid[current_cell2] == 1:
            restricted_2_found = True
            restricted_2_distance = distance_travelled
        if restricted_1_found and restricted_2_found:
            return True, restricted_1_distance, restricted_2_distance
    return False, 0, 0
