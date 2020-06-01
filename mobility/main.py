import numpy as np
import sys
import json
import os
from mobility import Slope
from mobility import Slope2
from mobility import Grids
from mobility import ArrayToRaster
from mobility import Trafficability
from mobility import Rasterize
from mobility import Tools
from mobility.threats import ChokePoints
from mobility import voronoi
from mobility import obstacle_family
from mobility import GetBorder
from mobility import leastcostpath
from mobility import mydijkistra
from mobility.kshortest import kshortest
from mobility import IndependentRoutes
from mobility.threats import threats


def is_withing_border(point, borders):
    return borders[0] < float(point[0]) < borders[2] and borders[1] < float(point[1]) < borders[3]


def init(battlefield, start, destination, is_building, is_elevation, is_roads, is_vegetation, is_water):
    sep = os.path.sep
    battlefield_path = 'battlefields' + sep + battlefield + sep
    with open(battlefield_path + 'bounds.data') as json_file:
        data = json.load(json_file)
        long_left = data['left']
        lat_bottom = data['bottom']
        long_right = data['right']
        lat_top = data['top']

    borders = [long_left, lat_bottom, long_right, lat_top]
    if not (is_withing_border(start, borders) and is_withing_border(destination, borders)):
        return None
    # set print options of numpy
    np.set_printoptions(threshold=sys.maxsize)
    # float_formatter = "{:.15f}".format
    # np.set_printoptions(formatter={'float_kind': float_formatter})
    # get elevation grid and grid parameters
    elevation_original_grid, elevation_grid, x1, delta_x1, y1, delta_y1 = Grids.get_elevation_grid(long_left, lat_bottom, long_right, lat_top)  # TODO edit
    # get latitude grid that contain latitude of top left point of each grid cell
    latitude_grid = Grids.get_latitude_grid(elevation_grid, y1, delta_y1)
    # get longitude grid that contain longitude of top left point of each grid cell
    longitude_grid = Grids.get_longitude_grid(elevation_grid, x1, delta_x1)
    # joint latitude, longitude and elevation grids to get level 2 combined array of grids. shape = (X,Y,3)
    level_1_combined_array = np.concatenate((latitude_grid, longitude_grid), axis=2)
    level_2_combined_array = np.concatenate((level_1_combined_array, elevation_grid), axis=2)
    # get slope grid that contain slope of each cell
    slope_grid = Slope.slope(level_2_combined_array)
    # slope_grid = Slope2.slope(elevation_original_grid, elevation_grid.shape, x1, delta_x1, y1, delta_y1)  # TODO remove
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
    ArrayToRaster.save_3d_grid_as_raster(elevation_grid, x1, delta_x1, y1, delta_y1, battlefield_path + 'mobility' + sep + 'elevation_grid.tif')
    ArrayToRaster.save_3d_grid_as_raster(slope_grid, x1, delta_x1, y1, delta_y1, battlefield_path + 'mobility' + sep + 'slope_grid.tif')
    ArrayToRaster.save_3d_grid_as_raster(building_grid, x1, delta_x1, y1, delta_y1,
                                         battlefield_path + 'mobility' + sep + 'building_grid.tif')
    ArrayToRaster.save_3d_grid_as_raster(vegetation_grid, x1, delta_x1, y1, delta_y1,
                                         battlefield_path + 'mobility' + sep + 'vegetation_grid.tif')
    ArrayToRaster.save_3d_grid_as_raster(water_grid, x1, delta_x1, y1, delta_y1,
                                         battlefield_path + 'mobility' + sep + 'water_grid.tif')
    ArrayToRaster.save_3d_grid_as_raster(road_grid, x1, delta_x1, y1, delta_y1,
                                         battlefield_path + 'mobility' + sep + 'road_grid.tif')

    # trafficability
    trafficability_grid, restricted_grid = Trafficability.get_trafficability_grid(level_4_combined_array, is_building, is_elevation, is_roads, is_vegetation, is_water)
    # least cost path
    start_coord = (float(start[0]), float(start[1]))
    stop_coord = (float(destination[0]), float(destination[1]))
    # lc_path, lc_cost = leastcostpath.create_path(trafficability_grid, x1, y1, delta_x1, delta_y1, start_coord, stop_coord)
    lc_paths= IndependentRoutes.get_independent_shortest_paths(trafficability_grid, x1, y1, delta_x1, delta_y1, start_coord, stop_coord)
    # lc_paths = IndependentShortestPaths.choke_point_based_shortest_paths(trafficability_grid, restricted_grid, x1, y1, delta_x1, delta_y1, start_coord, stop_coord)
    # choke_point_sets = threat.get_choke_points(restricted_grid, lc_path)
    # lc_path_geojson = Tools.path_to_geo_json(lc_path, lc_cost, x1, y1, delta_x1, delta_y1)
    # lc_choke_points_geojson = Tools.path_set_to_geo_json(choke_point_sets, x1, y1, delta_x1, delta_y1)
    indep_paths_geojson = Tools.path_set_to_geo_json(lc_paths, x1, y1, delta_x1, delta_y1)
    # print(lc_choke_points_geojson)
    ArrayToRaster.save_2d_grid_as_raster(trafficability_grid, x1, delta_x1, y1, delta_y1,
                                         'mobility' + sep + 'tempfiles' + sep + 'trafficability.tif')
    ArrayToRaster.save_2d_grid_as_raster(restricted_grid, x1, delta_x1, y1, delta_y1,
                                         'mobility' + sep + 'tempfiles' + sep + 'restricted_grid.tif')
    # threat grid
    enemy_building_threat = threats.get_enemy_threat_range_grid(building_grid)
    # return lc_path_geojson
    return indep_paths_geojson
    # boundaries = GetBorder.get_boundary_points(trafficability_grid)
    # boundaries_edit = np.copy(boundaries)
    # obstaclefamily = obstacle_family.partition_obstacles(boundaries_edit)
    # print('no of obstacles = ' + str(len(obstacle_family)))
    # voronoi_array = voronoi.start(obstaclefamily, boundaries_edit.shape)
    # roads_2d = road_grid[:, :, 0]
    # voronoi_with_roads = np.where(roads_2d == 1, 1, voronoi_array)
    #
    # ArrayToRaster.save_2d_grid_as_raster(boundaries, x1, delta_x1, y1, delta_y1, 'tempfiles' + sep + 'boundaries.tif')
    # ArrayToRaster.save_2d_grid_as_raster(costs, x1, delta_x1, y1, delta_y1, battlefield_path + 'mobility' + sep + 'costs.tif')

    # Polygonize.polygonize(battlefield_path + 'mobility' + sep + 'path.tif', battlefield_path + 'mobility' + sep + 'path.geojson')
    # ArrayToRaster.save_2d_grid_as_raster(voronoi_array, x1, delta_x1, y1, delta_y1,
    #                                      battlefield_path + 'mobility' + sep + 'voronoi.tif')