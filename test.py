from flask import Flask
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
from Overlay import Overalay
from Overlays import Overalays
from Battlefield import Battlefield
from Battlefields import Battlefields
from Shape import Shape
from flask_cors import CORS

TGS = Flask(__name__)
api = Api(TGS)
CORS(TGS)

api.add_resource(Overalays, "/overlays")
api.add_resource(Overalay, "/overlays/<string:name>")
api.add_resource(Shape, "/overlays/<string:name>/<int:id>")

api.add_resource(Battlefields, "/battlefields")
api.add_resource(Battlefield, "/battlefields/<string:name>")

TGS.run(debug=True, port=8082)
