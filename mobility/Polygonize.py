from osgeo import gdal
from osgeo import ogr
import os

def polygonize(infile, outfile):
    sourceRaster = gdal.Open(infile)
    band = sourceRaster.GetRasterBand(1)
    bandArray = band.ReadAsArray()
    outShapefile = "polygonized"
    driver = ogr.GetDriverByName("geojson")
    if os.path.exists(outfile):
        driver.DeleteDataSource(outfile)
    outDatasource = driver.CreateDataSource(outfile)
    outLayer = outDatasource.CreateLayer("polygonized", srs=None)
    gdal.Polygonize( band, None, outLayer, -1, [], callback=None )
    outDatasource.Destroy()
    sourceRaster = None