from flask_restful import Resource, reqparse, Api
import json
import os
import ast


class Shape(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("properties")
        parser.add_argument("type")
        parser.add_argument("features")
        args = parser.parse_args()

        name = args["name"]
        filename = 'overlays\\' + name + '.json'
        if not os.path.exists(filename):
            overlay = {
                "name": name,
                "properties": args["properties"],
                "type": args["type"],
                "features": args["features"]
            }
            with open('overlays\\'+name+'.json', 'w') as outfile:
                json.dump(overlay, outfile)
            return overlay, 201
        else:
            return "overlay already exists", 409

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("properties")
        parser.add_argument("type")
        parser.add_argument("features")
        args = parser.parse_args()

        filename = 'overlays\\' + name + '.json'
        if os.path.exists(filename):
            overlay = {
                "name": name,
                "properties": args["properties"],
                "type": args["type"],
                "features": args["features"]
            }
            with open('overlays\\' + name + '.json', 'w') as outfile:
                json.dump(overlay, outfile)
            return overlay, 201
        else:
            return "overlay not found", 404