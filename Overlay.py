from flask_restful import Resource, reqparse, Api
import json
import os
import ast


class Overalay(Resource):
    def get(self, name):
        filename = 'overlays\\' + name + '.json'
        if os.path.exists(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
            return data, {'Access-Control-Allow-Origin': '*'}
        else:
            return "overlay not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("properties")
        parser.add_argument("geometry")
        args = parser.parse_args()
        filename = 'overlays\\' + name + '.json'
        if os.path.exists(filename):
            shape = {
                "type": args["type"],
                "properties": ast.literal_eval(args["properties"]),
                "geometry": ast.literal_eval(args["geometry"])
            }

            with open(filename) as json_file:
                data = json.load(json_file)
                shape_list = data['features']
                print(len(shape_list))
                shape_list.append(shape)
            with open('overlays\\'+name+'.json', 'w') as outfile:
                with open(filename) as json_file:
                    json.dump(data, outfile)
            print(data)
            return data, 201
        else:
            return "overlay not found", 404