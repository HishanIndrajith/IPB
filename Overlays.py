from flask_restful import Resource, reqparse, Api, request
import json
import os


class Overalays(Resource):
    def get(self):
        battlefield = request.args.get('battlefield')
        path = 'battlefields\\'+battlefield+'\\'

        overlays = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.json' in file:
                    with open(os.path.join(r, file)) as json_file:
                        data = json.load(json_file)
                        overlays.append(data)
        return overlays, {'Access-Control-Allow-Origin': '*'}
