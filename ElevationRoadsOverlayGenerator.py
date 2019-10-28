# Author Hishan Indrajith Adikari

import ijson
import json
import threading


def create_elevation_overlay(name, top, left, bottom, right):
    print('Thread elevation started')
    filename = "battlefields\\elevation_srilanka.json"
    with open(filename, 'r') as f:
        objects = ijson.items(f, 'features.item')
        columns = list(objects)
    features = []
    for col in columns:
        insider_found = False
        new_line = []
        elevation = col['properties']['elevation']
        for coords in col['geometry']['coordinates']:
            new_line.append([float(coords[0]), float(coords[1])])
            if (float(coords[1]) < top) & (float(coords[1]) > bottom) & (float(coords[0]) > left) & (
                    float(coords[0]) < right):
                insider_found = True
        if insider_found:
            feature = {
                "type": "Feature",
                "properties": {
                    "elevation": elevation
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": new_line
                }
            }
            features.append(feature)
    properties = {}
    with open('battlefields\\properties_elevation.json') as json_file:
        properties = json.load(json_file)
    json_data = {
        "name": "elevation",
        "properties": properties,
        "type": "FeatureCollection",
        "features": features
    }
    with open("battlefields\\"+name+"\\elevation.json", 'w') as outfile:
        json.dump(json_data, outfile)


def create_roads_overlay(name, top, left, bottom, right):
    print('Thread roads started')
    filename = "battlefields\\roads_srilanka.json"
    with open(filename, 'r', encoding="utf8") as f:
        objects = ijson.items(f, 'features.item')
        columns = list(objects)
    features = []
    for col in columns:
        insider_found = False
        new_line = []
        ntlclass = col['properties']['fclass']
        for coords in col['geometry']['coordinates']:
            new_line.append([float(coords[0]), float(coords[1])])
            if (float(coords[1]) < top) & (float(coords[1]) > bottom) & (float(coords[0]) > left) & (
                    float(coords[0]) < right):
                insider_found = True
        if insider_found:
            feature = {
                "type": "Feature",
                "properties": {
                    "ntlclass": ntlclass
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": new_line
                }
            }
            features.append(feature)
    properties = {}
    with open('battlefields\\properties_roads.json') as json_file:
        properties = json.load(json_file)
    json_data = {
        "name": "roads",
        "properties": properties,
        "type": "FeatureCollection",
        "features": features
    }
    with open("battlefields\\"+name+"\\roads.json", 'w') as outfile:
        json.dump(json_data, outfile)


class ElevationRoadsOverlayGenerator:

    def createElevationAndRoadOverlay(name, top, left, bottom, right):
        elevation_thread = threading.Thread(target=create_elevation_overlay,
                                            args=(name, top, left, bottom, right,))
        roads_thread = threading.Thread(target=create_roads_overlay,
                                        args=(name, top, left, bottom, right,))
        elevation_thread.start()
        roads_thread.start()
        elevation_thread.join()
        roads_thread.join()
