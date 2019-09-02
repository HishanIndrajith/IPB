from flask_restful import Resource, reqparse, Api
import json
import os


class Overalays(Resource):
    def get(self):
        path = 'overlays\\'

        overlays = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.json' in file:
                    with open(os.path.join(r, file)) as json_file:
                        data = json.load(json_file)
                        overlays.append(data)
        return overlays, 200

    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("name")
    #     parser.add_argument("properties")
    #     parser.add_argument("type")
    #     parser.add_argument("features")
    #     args = parser.parse_args()
    #
    #     name = args["name"]
    #     filename = 'overlays\\' + name + '.json'
    #     if not os.path.exists(filename):
    #         overlay = {
    #             "name": name,
    #             "properties": args["properties"],
    #             "type": args["type"],
    #             "features": args["features"]
    #         }
    #         with open('overlays\\'+name+'.json', 'w') as outfile:
    #             json.dump(overlay, outfile)
    #         return overlay, 201
    #     else:
    #         return "overlay already exists", 409
