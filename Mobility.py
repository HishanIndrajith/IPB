from flask_restful import Resource, reqparse, request
import json
import os
from mobility import main

sep = os.path.sep


class Mobility(Resource):

    def get(self, battlefield):
        start_str = request.args.get('start')
        destination_str = request.args.get('destination')
        building = request.args.get('building')
        elevation = request.args.get('elevation')
        roads = request.args.get('roads')
        vegetation = request.args.get('vegetation')
        water = request.args.get('water')
        start = start_str.split(", ")
        destination = destination_str.split(", ")
        path = main.init(battlefield, start, destination, int(building), int(elevation), int(roads), int(vegetation),
                         int(water))
        if path is None:
            return "points out of border", 400
        return json.loads(path), {'Access-Control-Allow-Origin': '*'}
