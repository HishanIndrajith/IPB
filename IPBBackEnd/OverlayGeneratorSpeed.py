from osgeo import ogr
import threading
import json
import os

sep = os.path.sep


def add_id(path, name):
    with open(path) as json_file:
        data = json.load(json_file)
        feature_id = 0
        for feature in data['features']:
            feature['id'] = feature_id
            feature_id = feature_id + 1
        json_file.close()
        with open('overlayproperties/' + name + '.json') as json_prop_file:
            properties = json.load(json_prop_file)
            json_data = {
                "name": name,
                "properties": properties,
                "type": "FeatureCollection",
                "features": data['features']
            }
            json_prop_file.close()
            with open(path, 'w') as outfile:
                json.dump(json_data, outfile)


def clip_overlay(battlefield, name, top, left, bottom, right):
    print(name + " overlay generating initiated")
    shape_file = "srilankadata" + sep + name + ".geojson"
    driver = ogr.GetDriverByName("geojson")
    data_source = driver.Open(shape_file, 0)
    layer = data_source.GetLayer()

    wkt = "POLYGON ((" +\
          str(left) + " " + str(bottom) + "," + \
          str(right) + " " + str(bottom) + "," + \
          str(right) + " " + str(top) + "," + \
          str(left) + " " + str(top) + "," + \
          str(left) + " " + str(bottom) + ")) "

    layer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))

    # Save extent to a new Shapefile
    out_file = "battlefields" + sep + battlefield + sep + name + ".json"
    out_driver = ogr.GetDriverByName("geojson")
    out_data_source = out_driver.CreateDataSource(out_file)
    out_data_source.CopyLayer(layer, "")

    # Save and close DataSource
    out_data_source = None
    print(name + " overlay generating finished")
    add_id(out_file, name)


def start(battlefield, top, left, bottom, right):
    thread1 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "water", top, left, bottom, right))
    thread2 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "elevation", top, left, bottom, right))
    thread3 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "roads", top, left, bottom, right))
    thread4 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "vegetation", top, left, bottom, right))
    thread5 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "buildings", top, left, bottom, right))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
