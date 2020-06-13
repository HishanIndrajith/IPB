import numpy as np
import json


def path_to_geo_json(path, cost, x1, y1, delta_x1, delta_y1):
    path = np.array(path, float).T
    path = path + 0.5
    path[0] = (path[0] * delta_y1) + y1
    path[1] = (path[1] * delta_x1) + x1
    path = np.flip(path, 0)
    path = path.T
    path = path.tolist()
    feature = {
        "type": "Feature",
        "properties": {
            "cost": cost
        },
        "geometry": {
            "type": "LineString",
            "coordinates": path
        }
    }
    json_data = {
        "name": "minimum_cost_path",
        "type": "FeatureCollection",
        "features": [feature]
    }
    return json.dumps(json_data)


def path_set_to_geo_json(path_set, x1, y1, delta_x1, delta_y1):
    feature_array = []
    for path_tuple in path_set:
        path = path_tuple[0]
        cost = path_tuple[1]
        path = np.array(path, float).T
        path = path + 0.5
        path[0] = (path[0] * delta_y1) + y1
        path[1] = (path[1] * delta_x1) + x1
        path = np.flip(path, 0)
        path = path.T
        path = path.tolist()
        feature = {
            "type": "Feature",
            "properties": {
                "cost": cost
            },
            "geometry": {
                "type": "LineString",
                "coordinates": path
            }
        }
        feature_array.append(feature)
    json_data = {
        "name": "choke_points",
        "type": "FeatureCollection",
        "features": feature_array
    }
    return json.dumps(json_data)


def add_threat_to_paths(path_set, threat, x1, y1, delta_x1, delta_y1):
    final_path_array = []
    for path_tuple in path_set:
        path = path_tuple[0]
        path_inv = np.array(path).T
        threat_array = threat[path_inv[0], path_inv[1]]
        cost = path_tuple[1]
        path = np.array(path, float).T
        path = path + 0.5
        path[0] = (path[0] * delta_y1) + y1
        path[1] = (path[1] * delta_x1) + x1
        path = np.flip(path, 0)
        path = np.append(path, [threat_array], axis=0).T
        # path = path.T
        path = path.tolist()
        final_path_array.append((path, cost))
    return final_path_array
