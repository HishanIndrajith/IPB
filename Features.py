from flask_restful import Resource, reqparse, Api, request
import json
import os
import ast


class Features(Resource):
    def post(self, battlefield, overlay):
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("id")
        parser.add_argument("properties")
        parser.add_argument("geometry")
        args = parser.parse_args()
        filename = 'battlefields\\' + battlefield + '\\' + overlay + '.json'
        if os.path.exists(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
                feature_list = data['features']
                feature = {
                    "type": args["type"],
                    "id": len(feature_list),
                    "properties": ast.literal_eval(args["properties"]),
                    "geometry": ast.literal_eval(args["geometry"])
                }
                feature_list.append(feature)
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
            return data, 201
        else:
            return "overlay not found", 404