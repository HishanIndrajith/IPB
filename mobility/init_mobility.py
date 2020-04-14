import numpy as np
import sys
import json
from mobility import Slope
from mobility import Grids
from mobility import ArrayToRaster
from mobility import Trafficability
from mobility import Rasterize


battlefield = "pera_campus"
with open('..\\battlefields\\' + battlefield + '\\bounds.data') as json_file:
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
# ArrayToRaster.save_3d_grid_as_raster(slope_grid, x1, delta_x1, y1, delta_y1, 'slope_grid.tif')


# trafficability
trafficability_grid = Trafficability.get_trafficability_grid(level_4_combined_array)
ArrayToRaster.save_2d_grid_as_raster(trafficability_grid, x1, delta_x1, y1, delta_y1, 'tempfiles\\trafficability.tif')
# print(trafficability_grid)
