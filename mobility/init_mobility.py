import numpy as np
import sys
from mobility import Slope
from mobility import Grids
from mobility import ArrayToRaster

long_left = 80.587567
lat_bottom = 7.250265
long_right = 80.595120
lat_top = 7.257939

# set print options of numpy
np.set_printoptions(threshold=sys.maxsize)
float_formatter = "{:.15f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})
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
print(level_3_combined_array.shape)
# uncomment below line to print final array
# print(level_3_combined_array)
ArrayToRaster.save_grid_as_raster(slope_grid, x1, delta_x1, y1, delta_y1, 'slope_grid.tif')
