from flask_restful import Resource, reqparse
import json
import os


class Battlefield(Resource):

    def get(self, battlefield):
        filename = 'battlefields\\' + battlefield + '\\bounds.data'
        if os.path.exists(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
            return data, {'Access-Control-Allow-Origin': '*'}
        else:
            return "overlay not found", 404


