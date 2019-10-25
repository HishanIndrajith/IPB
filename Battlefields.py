from flask_restful import Resource, reqparse, Api
import json
import os


class Battlefields(Resource):
    def get(self):
        path = 'battlefields\\'
        battlefields = []
        # r=root, d=directories, f = files
        for x in os.listdir(path):
            dir = path + x
            if os.path.isdir(dir):
                battlefields.append(x)
        return battlefields, {'Access-Control-Allow-Origin': '*'}

