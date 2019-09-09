from flask import Flask
from flask_restful import Resource, reqparse, Api
from Overlay import Overalay
from Overlays import Overalays
from Shape import Shape
from flask_cors import CORS

TGS = Flask(__name__)
api = Api(TGS)
CORS(TGS)

api.add_resource(Overalays, "/overlays")
api.add_resource(Overalay, "/overlays/<string:name>")
api.add_resource(Shape, "/overlays/<string:name>/<int:id>")

TGS.run(debug=True, port=8082)
