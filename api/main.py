from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello world!"}

    def post(self, data):
        print(data)


api.add_resource(HelloWorld, "/")