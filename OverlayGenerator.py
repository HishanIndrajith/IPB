import ijson
import threading
import json


def is_geometry_part_of(geometry, top, left, bottom, right):
    is_part_of = False
    p1 = geometry['coordinates']
    p1_new = []
    if geometry['type'] == 'MultiPolygon':
        for p2 in p1:
            p2_new = []
            for p3 in p2:
                p3_new = []
                for p4 in p3:
                    p5_new_0 = float(p4[0])
                    p5_new_1 = float(p4[1])
                    if left < p5_new_0 < right and bottom < p5_new_1 < top:
                        is_part_of = True
                    p3_new.append([p5_new_0, p5_new_1])
                p2_new.append(p3_new)
            p1_new.append(p2_new)
        geometry_new = p1_new
        if is_part_of:
            return True, geometry_new
        else:
            return False, geometry_new
    elif geometry['type'] == 'LineString':
        for p2 in p1:
            p3_new_0 = float(p2[0])
            p3_new_1 = float(p2[1])
            if left < p3_new_0 < right and bottom < p3_new_1 < top:
                is_part_of = True
            p1_new.append([p3_new_0, p3_new_1])
        geometry_new = p1_new
        if is_part_of:
            return True, geometry_new
        else:
            return False, geometry_new


def clip_overlay(battlefield, name, top, left, bottom, right):
    output_path = "battlefields/" + battlefield + "/" + name + ".json"
    input_path = "srilankadata" + "/" + name + ".geojson"
    print(name + " started")
    with open(input_path, 'rb') as input_file:
        # load json iteratively
        features = ijson.items(input_file, 'features.item')
        features_new = []
        feature_id=0
        for feature in features:
            geometry = feature['geometry']
            is_part, geometry_new = is_geometry_part_of(geometry, top, left, bottom, right)
            if is_part:
                feature_new = {
                    "type": "Feature",
                    "id": feature_id,
                    "properties": feature['properties'],
                    "geometry": {
                        "type": geometry['type'],
                        "coordinates": geometry_new
                    }
                }
                features_new.append(feature_new)
                feature_id = feature_id + 1
        with open('overlayproperties/' + name + '.json') as json_file:
            properties = json.load(json_file)
            json_data = {
                "name": name,
                "properties": properties,
                "type": "FeatureCollection",
                "features": features_new
            }
            with open(output_path, 'w') as outfile:
                json.dump(json_data, outfile)
                print(name + " ended")


def start(battlefield, top, left, bottom, right):
    thread1 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "buildings", top, left, bottom, right))
    thread2 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "elevation", top, left, bottom, right))
    thread3 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "roads", top, left, bottom, right))
    thread4 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "vegetation", top, left, bottom, right))
    thread5 = threading.Thread(target=clip_overlay,
                               args=(battlefield, "water", top, left, bottom, right))
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
