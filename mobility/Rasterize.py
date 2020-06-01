from osgeo import gdal
from osgeo import ogr
import numpy as np
import json
import os

sep = os.path.sep


def format_vegetation_overlay(input_file):
    temp_files_folder = "mobility" + sep + "tempfiles"
    output_file = temp_files_folder + sep + 'vegetation.json'
    with open(input_file) as json_file:
        data = json.load(json_file)
        for feature in data['features']:
            vegetation_type = feature['properties']['Vegetation Type']
            if vegetation_type == 'grassland':
                feature['properties']['Vegetation Type'] = 1
            elif vegetation_type == 'shrubland':
                feature['properties']['Vegetation Type'] = 2
            elif vegetation_type == 'woodland':
                feature['properties']['Vegetation Type'] = 3
            elif vegetation_type == 'medium density forest':
                feature['properties']['Vegetation Type'] = 4
            elif vegetation_type == 'high density forest':
                feature['properties']['Vegetation Type'] = 5
            elif vegetation_type == 'unknown':
                feature['properties']['Vegetation Type'] = 6
        json_file.close()
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()


def format_building_overlay(input_file):
    temp_files_folder = "mobility" + sep + "tempfiles"
    output_file = temp_files_folder + sep + 'buildings.json'
    with open(input_file) as json_file:
        data = json.load(json_file)
        for feature in data['features']:
            status = feature['properties']['status']
            if status == 'enemy':
                feature['properties']['status'] = 1
            elif status == 'friendly':
                feature['properties']['status'] = 2
            elif status == 'neutral':
                feature['properties']['status'] = 3
            elif status == 'unknown':
                feature['properties']['status'] = 4
        json_file.close()
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()


def rasterize(origin_x, origin_y, pixel_width, pixel_height, cols, rows, battlefield, overlay):
    temp_files_folder = "mobility" + sep + "tempfiles"
    print("rasterizing " + overlay + " initiated")
    input_file = 'battlefields' + sep + battlefield + sep + overlay + ".json"
    if overlay == 'vegetation':
        format_vegetation_overlay(input_file)
        input_file = temp_files_folder + sep + 'vegetation.json'
    if overlay == 'buildings':
        format_building_overlay(input_file)
        input_file = temp_files_folder + sep + 'buildings.json'
    driver = ogr.GetDriverByName("geojson")
    data_source = driver.Open(input_file, 0)
    layer = data_source.GetLayer()
    driver = gdal.GetDriverByName('GTiff')
    output = temp_files_folder + sep + overlay + '_grid.tif'
    out_raster = driver.Create(output, cols, rows, 1, gdal.GDT_Byte)
    out_raster.SetGeoTransform((origin_x, pixel_width, 0, origin_y, 0, pixel_height))
    if overlay == 'vegetation':
        gdal.RasterizeLayer(out_raster, [1], layer, options=["ATTRIBUTE=Vegetation Type"])
    if overlay == 'buildings':
        gdal.RasterizeLayer(out_raster, [1], layer, options=["ATTRIBUTE=status"])
    else:
        gdal.RasterizeLayer(out_raster, [1], layer, burn_values=[1])
    band = out_raster.GetRasterBand(1)
    no_data_value = 0
    band.SetNoDataValue(no_data_value)
    band.FlushCache()
    print("rasterizing " + overlay + " ended")
    raster_array_2d = out_raster.ReadAsArray()
    # make it 3d array
    overlay_grid = np.expand_dims(raster_array_2d, axis=2)
    return overlay_grid
