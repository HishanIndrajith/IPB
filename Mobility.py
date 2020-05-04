from flask_restful import Resource, reqparse, request
import json
import os
from mobility import main
sep = os.path.sep


class Mobility(Resource):

    def get(self, battlefield):
        start_str = request.args.get('start')
        destination_str = request.args.get('destination')
        start = start_str.split(", ")
        destination = destination_str.split(", ")
        path = main.init(battlefield, start, destination)
        return json.loads(path), {'Access-Control-Allow-Origin': '*'}


