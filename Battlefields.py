from flask_restful import Resource, reqparse, Api
import json
import os
import ast
import OverlayGenerator


class Battlefields(Resource):
    def get(self):
        path = 'battlefields\\'
        battlefields = []
        # r=root, d=directories, f = files
        for x in os.listdir(path):
            directory = path + x
            if os.path.isdir(directory):
                battlefields.append(x)
        return battlefields, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("top")
        parser.add_argument("left")
        parser.add_argument("bottom")
        parser.add_argument("right")
        args = parser.parse_args()
        name = args["name"]
        filename = 'battlefields\\' + name
        if os.path.exists(filename):
            return "battlefield already there", 409
        else:
            top = ast.literal_eval(args["top"])
            left = ast.literal_eval(args["left"])
            bottom = ast.literal_eval(args["bottom"])
            right = ast.literal_eval(args["right"])
            os.mkdir(filename)
            with open(filename + "\\bounds.data", 'w') as outfile:
                bound_json = {
                    "top": top,
                    "left": left,
                    "bottom": bottom,
                    "right": right,
                }
                json.dump(bound_json, outfile)
            OverlayGenerator.start(name, top, left, bottom, right)
            return "success", 201
