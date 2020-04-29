from flask_restful import Resource, reqparse, request
import json
import os
from mobility import main
from flask import send_file
sep = os.path.sep


class Mobility(Resource):

    def get(self, battlefield):
        file_path = 'battlefields' + sep + battlefield + sep + 'mobility' + sep + 'path.tif'
        start_str = request.args.get('start')
        destination_str = request.args.get('destination')
        start = start_str.split(", ")
        destination = destination_str.split(", ")
        print(start)
        main.init(battlefield, start, destination)
        filename = file_path
        return send_file(filename, mimetype='image/tiff')


