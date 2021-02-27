from flask_restful import Resource, reqparse, Api, request
import json
import os

sep = os.path.sep


class Overlays(Resource):
    def get(self, battlefield):
        path = 'battlefields' + sep + battlefield + sep
        overlays = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.json' in file:
                    with open(os.path.join(r, file)) as json_file:
                        data = json.load(json_file)
                        overlays.append(data)
        return overlays, {'Access-Control-Allow-Origin': '*'}
