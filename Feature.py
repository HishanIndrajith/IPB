from flask_restful import Resource, reqparse, Api, request
import json
import os
import ast

sep = os.path.sep


class Feature(Resource):

    def put(self, battlefield, overlay, feature_id):
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("properties")
        parser.add_argument("geometry")
        args = parser.parse_args()
        filename = 'battlefields' + sep + battlefield + sep + overlay + '.json'
        if os.path.exists(filename):
            feature = {
                "type": args["type"],
                "id": feature_id,
                "properties": ast.literal_eval(args["properties"]),
                "geometry": ast.literal_eval(args["geometry"])
            }

            with open(filename) as json_file:
                data = json.load(json_file)
                feature_list = data['features']
                feature_list_new = []
                for f in feature_list:
                    if f['id'] == feature_id:
                        f = feature
                    feature_list_new.append(f)
                data['features'] = feature_list_new
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
            return "edit success", 201
        else:
            return "overlay not found", 404

    def delete(self, battlefield, overlay, feature_id):
        filename = 'battlefields' + sep + battlefield + sep + overlay + '.json'
        if os.path.exists(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
                feature_list = data['features']
                feature_list_new = []
                for f in feature_list:
                    if f['id'] != feature_id:
                        feature_list_new.append(f)
                data['features'] = feature_list_new
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
            return "delete success", 201
        else:
            return "overlay not found", 404