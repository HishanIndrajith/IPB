from osgeo import gdal_array, gdalconst
import gdal
import numpy as np
import sys
from mobility import Slope
from mobility import Grids
from mobility import ArrayToRaster

rasin = "srilankaterrain.tif"
clipped = gdal.Warp("output.tif", rasin, outputBounds=[80.587567, 7.250265, 80.595120, 7.257939], outputBoundsSRS='EPSG:4267')

referenceProj = clipped.GetProjection()
referenceTrans = clipped.GetGeoTransform()
bandreference = clipped.GetRasterBand(1)
x = clipped.RasterXSize*10
y = clipped.RasterYSize*10

referenceTransList = list(referenceTrans)
referenceTransList[1] = referenceTrans[1]/10
referenceTransList[5] = referenceTrans[5]/10
referenceTrans = tuple(referenceTransList)

print(referenceTrans)

driver= gdal.GetDriverByName('GTiff')
output = driver.Create("outputsample.tif", x, y, 1, bandreference.DataType)
output.SetGeoTransform(referenceTrans)
output.SetProjection(referenceProj)

gdal.ReprojectImage(clipped, output, referenceProj, referenceProj, gdalconst.GRA_Bilinear)

rasterArray = output.ReadAsArray()
elevation_array = np.expand_dims(rasterArray, axis=2)

np.set_printoptions(threshold=sys.maxsize)

# print(elevation_array[:, 0])
# print(elevation_array.shape)
# print(result)
# (row,column)

x1 = referenceTrans[0]
delta_x1 = referenceTrans[1]
y1 = referenceTrans[3]
delta_y1 = referenceTrans[5]
# print((x1, y1, delta_x1, delta_y1))
# print(result[280,270])
latitude_grid = Grids.get_latitude_grid(elevation_array, y1, delta_y1)
longitude_grid = Grids.get_longitude_grid(elevation_array, x1, delta_x1)
coordinates_grid = np.concatenate((latitude_grid, longitude_grid), axis=2)
coordinates_elevation_grid = np.concatenate((coordinates_grid, elevation_array), axis=2)
float_formatter = "{:.15f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})
print(coordinates_elevation_grid[279][269])
slope_grid = Slope.slope(coordinates_elevation_grid)
coordinates_ele_slope_grid = np.concatenate((coordinates_elevation_grid, slope_grid), axis=2)
print(coordinates_ele_slope_grid.shape)

# uncomment below line to print final array
# print(coordinates_ele_slope_grid)

# convert final array to a raster
# print(np.max(slope))
# rasterOrigin = (x1, y1)
# pixelWidth = delta_x1
# pixelHeight = delta_y1
# newRasterfn = 'test.tif'
# ArrayToRaster.main(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,slope)