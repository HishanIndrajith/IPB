from flask import Flask
from flask_restful import Resource, reqparse, Api
from Features import Features
from Feature import Feature
from Battlefield import Battlefield
from Battlefields import Battlefields
from Overlays import Overlays
from Mobility import Mobility
from flask_cors import CORS

TGS = Flask(__name__)
api = Api(TGS)
CORS(TGS)

api.add_resource(Battlefields, "/battlefields")
api.add_resource(Battlefield, "/battlefields/<string:battlefield>")
api.add_resource(Overlays, "/battlefields/<string:battlefield>/overlays")
api.add_resource(Features, "/battlefields/<string:battlefield>/overlays/<string:overlay>/features")
api.add_resource(Feature, "/battlefields/<string:battlefield>/overlays/<string:overlay>/features/<int:feature_id>")
api.add_resource(Mobility, "/battlefields/<string:battlefield>/least-cost-path")

TGS.run(debug=True, port=8082)
