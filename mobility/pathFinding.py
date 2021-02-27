##############################################################################

# import packages

##############################################################################


import numpy as np

import heapq

import matplotlib.pyplot as plt

import numpy as np
import sys
import json
import os
from mobility import Slope
from mobility import Grids
from mobility import ArrayToRaster
from mobility import Trafficability
from mobility import Rasterize
#
#
# battlefield = "Mission_Badulla_02"
# sep = os.path.sep
# with open('..' + sep + 'battlefields' + sep + battlefield + sep + 'bounds.data') as json_file:
#     data = json.load(json_file)
#     long_left = data['left']
#     lat_bottom = data['bottom']
#     long_right = data['right']
#     lat_top = data['top']
#
# # set print options of numpy
# np.set_printoptions(threshold=sys.maxsize)
# # float_formatter = "{:.15f}".format
# # np.set_printoptions(formatter={'float_kind': float_formatter})
# # get elevation grid and grid parameters
# elevation_grid, x1, delta_x1, y1, delta_y1 = Grids.get_elevation_grid(long_left, lat_bottom, long_right, lat_top)
# # get latitude grid that contain latitude of top left point of each grid cell
# latitude_grid = Grids.get_latitude_grid(elevation_grid, y1, delta_y1)
# # get longitude grid that contain longitude of top left point of each grid cell
# longitude_grid = Grids.get_longitude_grid(elevation_grid, x1, delta_x1)
# # joint latitude, longitude and elevation grids to get level 2 combined array of grids. shape = (X,Y,3)
# level_1_combined_array = np.concatenate((latitude_grid, longitude_grid), axis=2)
# level_2_combined_array = np.concatenate((level_1_combined_array, elevation_grid), axis=2)
# # get slope grid that contain slope of each cell
# slope_grid = Slope.slope(level_2_combined_array)
# # joint slope grid to level_2_combined_array to get level 3 combined array of grids. shape = (X,Y,4)
# level_3_combined_array = np.concatenate((level_2_combined_array, slope_grid), axis=2)
# # get vegetation array
# vegetation_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
#                                       battlefield, 'vegetation')
# # get buildings array
# building_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
#                                     battlefield, 'buildings')
# # get water array
# water_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
#                                  battlefield, 'water')
# # get roads array
# road_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
#                                 battlefield, 'roads')
#
# # joint vegetation, building, water and road grid to level_3_combined_array
# # to get level 4 combined array of grids. shape = (X,Y,8)
# level_4_combined_array = np.concatenate((level_3_combined_array, vegetation_grid), axis=2)
# level_4_combined_array = np.concatenate((level_4_combined_array, building_grid), axis=2)
# level_4_combined_array = np.concatenate((level_4_combined_array, water_grid), axis=2)
# level_4_combined_array = np.concatenate((level_4_combined_array, road_grid), axis=2)
#
# print(level_4_combined_array.shape)
# # uncomment below line to print final array
# # print(level_3_combined_array)
# ArrayToRaster.save_3d_grid_as_raster(slope_grid, x1, delta_x1, y1, delta_y1, 'tempfiles' + sep + 'slope_grid.tif')
#
#
# # trafficability
# trafficability_grid = Trafficability.get_trafficability_grid(level_4_combined_array)
# ArrayToRaster.save_2d_grid_as_raster(trafficability_grid, x1, delta_x1, y1, delta_y1, 'tempfiles' + sep + 'trafficability.tif')
# print(trafficability_grid)
#
#
#
#
# from matplotlib.pyplot import figure
#
# ##############################################################################
#
# # plot grid
#
# ##############################################################################
#
#
# grid = trafficability_grid
#
# # start point and goal
#
# start = (0, 0)
#
# goal = (0, 19)
#
#
# ##############################################################################
#
# # heuristic function for path scoring
#
# ##############################################################################
#
#
# def heuristic(a, b):
#     return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
#
#
# ##############################################################################
#
# # path finding function
#
# ##############################################################################
#
#
# def astar(array, start, goal):
#     neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#
#     close_set = set()
#
#     came_from = {}
#
#     gscore = {start: 0}
#
#     fscore = {start: heuristic(start, goal)}
#
#     oheap = []
#
#     heapq.heappush(oheap, (fscore[start], start))
#
#     while oheap:
#
#         current = heapq.heappop(oheap)[1]
#
#         if current == goal:
#
#             data = []
#
#             while current in came_from:
#                 data.append(current)
#
#                 current = came_from[current]
#
#             return data
#
#         close_set.add(current)
#
#         for i, j in neighbors:
#
#             neighbor = current[0] + i, current[1] + j
#
#             tentative_g_score = gscore[current] + heuristic(current, neighbor)
#
#             if 0 <= neighbor[0] < array.shape[0]:
#
#                 if 0 <= neighbor[1] < array.shape[1]:
#
#                     if array[neighbor[0]][neighbor[1]] == 1:
#                         continue
#
#                 else:
#
#                     # array bound y walls
#
#                     continue
#
#             else:
#
#                 # array bound x walls
#
#                 continue
#
#             if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
#                 continue
#
#             if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
#                 came_from[neighbor] = current
#
#                 gscore[neighbor] = tentative_g_score
#
#                 fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
#
#                 heapq.heappush(oheap, (fscore[neighbor], neighbor))
#
#     return False
#
#
# route = astar(grid, start, goal)
#
# route = route + [start]
#
# route = route[::-1]
#
# print(route)
#
# ##############################################################################
#
# # plot the path
#
# ##############################################################################
#
#
# # extract x and y coordinates from route list
#
# x_coords = []
#
# y_coords = []
#
# for i in (range(0, len(route))):
#     x = route[i][0]
#
#     y = route[i][1]
#
#     x_coords.append(x)
#
#     y_coords.append(y)
#
# # plot map and path
#
# fig, ax = plt.subplots(figsize=(20, 20))
#
# ax.imshow(grid, cmap=plt.cm.Dark2)
#
# ax.scatter(start[1], start[0], marker="*", color="yellow", s=200)
#
# ax.scatter(goal[1], goal[0], marker="*", color="red", s=200)
#
# ax.plot(y_coords, x_coords, color="black")
#
# plt.show()

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    battlefield = "Mission_Badulla_02"
    sep = os.path.sep
    with open('..' + sep + 'battlefields' + sep + battlefield + sep + 'bounds.data') as json_file:
        data = json.load(json_file)
        long_left = data['left']
        lat_bottom = data['bottom']
        long_right = data['right']
        lat_top = data['top']

    # set print options of numpy
    np.set_printoptions(threshold=sys.maxsize)
    # float_formatter = "{:.15f}".format
    # np.set_printoptions(formatter={'float_kind': float_formatter})
    # get elevation grid and grid parameters
    elevation_grid, x1, delta_x1, y1, delta_y1 = Grids.get_elevation_grid(long_left, lat_bottom, long_right, lat_top)
    # get latitude grid that contain latitude of top left point of each grid cell
    latitude_grid = Grids.get_latitude_grid(elevation_grid, y1, delta_y1)
    # get longitude grid that contain longitude of top left point of each grid cell
    longitude_grid = Grids.get_longitude_grid(elevation_grid, x1, delta_x1)
    # joint latitude, longitude and elevation grids to get level 2 combined array of grids. shape = (X,Y,3)
    level_1_combined_array = np.concatenate((latitude_grid, longitude_grid), axis=2)
    level_2_combined_array = np.concatenate((level_1_combined_array, elevation_grid), axis=2)
    # get slope grid that contain slope of each cell
    slope_grid = Slope.slope(level_2_combined_array)
    # joint slope grid to level_2_combined_array to get level 3 combined array of grids. shape = (X,Y,4)
    level_3_combined_array = np.concatenate((level_2_combined_array, slope_grid), axis=2)
    # get vegetation array
    vegetation_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
                                          battlefield, 'vegetation')
    # get buildings array
    building_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
                                        battlefield, 'buildings')
    # get water array
    water_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
                                     battlefield, 'water')
    # get roads array
    road_grid = Rasterize.rasterize(x1, y1, delta_x1, delta_y1, elevation_grid.shape[1], elevation_grid.shape[0],
                                    battlefield, 'roads')

    # joint vegetation, building, water and road grid to level_3_combined_array
    # to get level 4 combined array of grids. shape = (X,Y,8)
    level_4_combined_array = np.concatenate((level_3_combined_array, vegetation_grid), axis=2)
    level_4_combined_array = np.concatenate((level_4_combined_array, building_grid), axis=2)
    level_4_combined_array = np.concatenate((level_4_combined_array, water_grid), axis=2)
    level_4_combined_array = np.concatenate((level_4_combined_array, road_grid), axis=2)

    print(level_4_combined_array.shape)
    # uncomment below line to print final array
    # print(level_3_combined_array)
    ArrayToRaster.save_3d_grid_as_raster(slope_grid, x1, delta_x1, y1, delta_y1, 'tempfiles' + sep + 'slope_grid.tif')


    # trafficability
    trafficability_grid = Trafficability.get_trafficability_grid(level_4_combined_array)
    ArrayToRaster.save_2d_grid_as_raster(trafficability_grid, x1, delta_x1, y1, delta_y1, 'tempfiles' + sep + 'trafficability.tif')

    maze = trafficability_grid

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()