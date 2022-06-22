from flask import Flask


def create_web_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Yzf3V6qbAt"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
