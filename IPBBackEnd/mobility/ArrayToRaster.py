import gdal
import osr


def array2raster(new_raster_fn, raster_origin, pixel_width, pixel_height, array):

    cols = array.shape[1]
    rows = array.shape[0]
    origin_x = raster_origin[0]
    origin_y = raster_origin[1]

    driver = gdal.GetDriverByName('GTiff')
    out_raster = driver.Create(new_raster_fn, cols, rows, 1, gdal.GDT_Float32)
    out_raster.SetGeoTransform((origin_x, pixel_width, 0, origin_y, 0, pixel_height))
    out_band = out_raster.GetRasterBand(1)
    out_band.WriteArray(array)
    out_raster_srs = osr.SpatialReference()
    out_raster_srs.ImportFromEPSG(4326)
    out_raster.SetProjection(out_raster_srs.ExportToWkt())
    out_band.FlushCache()


def save_3d_grid_as_raster(grid, x1, delta_x1, y1, delta_y1, name):
    grid_2d = grid[:, :, 0]
    raster_origin = (x1, y1)
    pixel_width = delta_x1
    pixel_height = delta_y1
    array2raster(name, raster_origin, pixel_width, pixel_height, grid_2d)  # convert array to raster


def save_2d_grid_as_raster(grid, x1, delta_x1, y1, delta_y1, name):
    raster_origin = (x1, y1)
    pixel_width = delta_x1
    pixel_height = delta_y1
    array2raster(name, raster_origin, pixel_width, pixel_height, grid)  # convert array to raster
