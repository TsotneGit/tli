from flask import Flask
from flask_restful import Api, Resource
from hardware_api import ArduinoUno


app = Flask(__name__)
api = Api(app)
board = ArduinoUno("COM5")


class LightOn(Resource):
    def get(self):
        board.digital_write(2, True)

        return {"Response": "200Ok"}


class LightOff(Resource):
    def get(self):
        board.digital_write(2, False)

        return {"Response": "200Ok"}


api.add_resource(LightOn, "/lighton")
api.add_resource(LightOff, "/lightoff")
