from flask import Flask
from flask_restful import Api


def create_api_app():
    app = Flask(__name__)
    api = Api(app)
    return app
