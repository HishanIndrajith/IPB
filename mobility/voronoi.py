import numpy as np
from PIL import Image
import datetime


def voronoi(point_families, shape):
    depthmap = np.ones(shape, np.float) * 1e308
    colormap = np.zeros(shape, np.int)

    def hypot(X, Y):
        min_length = np.ones(shape, np.float) * 1e308
        for [x, y] in family:
            length = (X - x) ** 2 + (Y - y) ** 2
            min_length = np.where(length < min_length, length, min_length)
        return min_length
    for i, family in enumerate(point_families):
        paraboloid = np.fromfunction(hypot, shape)
        colormap = np.where(paraboloid < depthmap, i + 1, colormap)
        depthmap = np.where(paraboloid < depthmap, paraboloid, depthmap)
    return colormap

#
# def voronoi_default(points, shape):
#     depthmap = np.ones(shape, np.float) * 1e308
#     colormap = np.zeros(shape, np.int)
#
#     def hypot(X, Y):
#         return (X - x) ** 2 + (Y - y) ** 2
#     for i, (x, y) in enumerate(points):
#         paraboloid = np.fromfunction(hypot, shape)
#         colormap = np.where(paraboloid < depthmap, i + 1, colormap)
#         depthmap = np.where(paraboloid < depthmap, paraboloid, depthmap)
#
#     # for (x, y) in points:
#     #     colormap[x - 1:x + 2, y - 1:y + 2] = 0
#
#     return colormap


def draw_map(colormap):
    shape = colormap.shape

    palette = np.array([
        0x000000FF,
        0xFF0000FF,
        0x00FF00FF,
        0xFFFF00FF,
        0x0000FFFF,
        0xFF00FFFF,
        0x00FFFFFF,
        0xFFFFFFFF,
    ])

    colormap = np.transpose(colormap)
    pixels = np.empty(colormap.shape + (4,), np.int8)

    pixels[:, :, 3] = palette[colormap] & 0xFF
    pixels[:, :, 2] = (palette[colormap] >> 8) & 0xFF
    pixels[:, :, 1] = (palette[colormap] >> 16) & 0xFF
    pixels[:, :, 0] = (palette[colormap] >> 24) & 0xFF

    image = Image.frombytes("RGBA", shape, pixels)
    image.save('voronoi.png')


def border(colormap):
    max_value = np.max(colormap)
    boundary_grid = np.ones((colormap.shape[0], colormap.shape[1]), np.int)
    for i in range(1, max_value+1):
        x = 0
        for rows in colormap:
            y = 0
            for _ in rows:
                if x != 0 and y != 0 and x != colormap.shape[0] - 1 and y != colormap.shape[1] - 1:
                    if colormap[x - 1, y] == i and colormap[x - 1, y - 1] == i and colormap[x, y - 1] == i and colormap[
                        x + 1, y - 1] == i and colormap[x + 1, y] == i and colormap[x + 1, y + 1] == i and colormap[x, y + 1] == i and \
                            colormap[x - 1, y + 1] == i:
                        boundary_grid[x, y] = 0
                y = y + 1
            x = x + 1
    boundary_grid[0, :] = 0
    boundary_grid[:, 0] = 0
    boundary_grid[colormap.shape[0] - 1, :] = 0
    boundary_grid[:, colormap.shape[1] - 1] = 0
    return boundary_grid


# def get_points(grid):
#     points = list()
#     x = 0
#     for rows in grid:
#         y = 0
#         for column in rows:
#             if column == 1:
#                 points.append([x, y])
#             y = y + 1
#         x = x + 1
#     return points


def start(point_families, shape):
    print("start voronoi algorithm")
    a = datetime.datetime.now()
    voronoi_array = voronoi(point_families, (shape[1], shape[0]))
    # print(points)
    # points = ([10,30],[30,20],[40,40])
    # voronoi_array = voronoi(points, (100,100))
    voronoi_array = np.transpose(voronoi_array)
    border_array = border(voronoi_array)
    b = datetime.datetime.now()
    print('time taken')
    print(b - a)
    return border_array

# def partition_obstacles(grid):
#     obstacles = []
#     rest_point = (0, 0)
#     x = 0
#     for rows in grid:
#         y = 0
#         for column in rows:
#             if column == 0:
#                 rest_point = (x, y)
#                 obstacles.append(find_family(x,y))
#             y = y + 1
#         x = x + 1
#     return obstacles
#
#
# grid = []
# def find_family(x, y):


# if __name__ == '__main__':
#     points = get_points(1)
#     voronoi_array = voronoi(points)
#     border_array = border(voronoi_array)
#     draw_map(border_array)
#     # print(get_points(1))
