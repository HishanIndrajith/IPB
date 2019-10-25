from flask_restful import Resource, reqparse, Api
import json
import os
import ast
import shutil
from ElevationRoadsOverlayGenerator import ElevationRoadsOverlayGenerator


class Battlefield(Resource):

    def get(self, name):
        filename = 'battlefields\\' + name+'\\bounds.data'
        if os.path.exists(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
            return data, {'Access-Control-Allow-Origin': '*'}
        else:
            return "overlay not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("top")
        parser.add_argument("left")
        parser.add_argument("bottom")
        parser.add_argument("right")
        args = parser.parse_args()
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
            shutil.copy('battlefields\\buildings.json', filename+'\\buildings.json')
            shutil.copy('battlefields\\vegetation.json', filename+'\\vegetation.json')
            shutil.copy('battlefields\\water.json', filename+'\\water.json')
            ElevationRoadsOverlayGenerator.createElevationAndRoadOverlay(name, top, left, bottom, right)
            return "success", 201
