# Developed by Hishan Indrajith Adikari on 7th April 2020
import numpy as np
from osgeo import gdalconst
import gdal
import os

sep = os.path.sep


def get_elevation_grid(long_left, lat_bottom, long_right, lat_top):
    temp_files_folder = "mobility" + sep + "tempfiles"
    ras_in = "mobility" + sep + "srilankaterrain.tif"
    clipped = gdal.Warp(temp_files_folder + sep + "output.tif", ras_in, outputBounds=[long_left, lat_bottom, long_right, lat_top],
                        outputBoundsSRS='EPSG:4267')

    reference_projection = clipped.GetProjection()
    reference_transform = clipped.GetGeoTransform()
    band_reference = clipped.GetRasterBand(1)
    x = clipped.RasterXSize * 10
    y = clipped.RasterYSize * 10

    reference_transform_list = list(reference_transform)
    reference_transform_list[1] = reference_transform[1] / 10
    reference_transform_list[5] = reference_transform[5] / 10
    reference_transform = tuple(reference_transform_list)

    driver = gdal.GetDriverByName('GTiff')
    output = driver.Create(temp_files_folder + sep + "outputsample.tif", x, y, 1, band_reference.DataType)
    output.SetGeoTransform(reference_transform)
    output.SetProjection(reference_projection)

    gdal.ReprojectImage(clipped, output, reference_projection, reference_projection, gdalconst.GRA_Bilinear)

    raster_array_2d = output.ReadAsArray()
    # make it 3d array
    elevation_grid = np.expand_dims(raster_array_2d, axis=2)

    x1 = reference_transform[0]
    delta_x1 = reference_transform[1]
    y1 = reference_transform[3]
    delta_y1 = reference_transform[5]
    return elevation_grid, x1, delta_x1, y1, delta_y1


def get_latitude_grid(elevation_array, y1, delta_y1):
    # x - longitude
    # y - latitude
    latitude_grid = np.zeros(elevation_array.shape)
    for x in range(elevation_array.shape[0]):
        latitude_grid[x, :] = "{0:.15f}".format(y1 + delta_y1 * x)
    return latitude_grid


def get_longitude_grid(elevation_array, x1, delta_x1):
    # x - longitude
    # y - latitude
    longitude_grid = np.zeros(elevation_array.shape)
    for y in range(elevation_array.shape[1]):
        longitude_grid[:, y] = "{0:.15f}".format(x1 + delta_x1 * y)
    return longitude_grid
