from flask_restful import Resource, reqparse, Api, request
import json
import os
import ast


class Shape(Resource):

    def post(self):
        battlefield = request.args.get('battlefield')
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("properties")
        parser.add_argument("type")
        parser.add_argument("features")
        args = parser.parse_args()

        name = args["name"]
        filename = 'battlefields\\' + battlefield + '\\' + name + '.json'
        if not os.path.exists(filename):
            overlay = {
                "name": name,
                "properties": args["properties"],
                "type": args["type"],
                "features": args["features"]
            }
            with open(filename, 'w') as outfile:
                json.dump(overlay, outfile)
            return overlay, 201
        else:
            return "overlay already exists", 409

    def put(self, name):
        battlefield = request.args.get('battlefield')
        parser = reqparse.RequestParser()
        parser.add_argument("properties")
        parser.add_argument("type")
        parser.add_argument("features")
        args = parser.parse_args()

        filename = 'battlefields\\' + battlefield + '\\' + name + '.json'
        if os.path.exists(filename):
            overlay = {
                "name": name,
                "properties": args["properties"],
                "type": args["type"],
                "features": args["features"]
            }
            with open(filename, 'w') as outfile:
                json.dump(overlay, outfile)
            return overlay, 201
        else:
            return "overlay not found", 404