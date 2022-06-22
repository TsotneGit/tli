from flask import Blueprint, render_template, send_from_directory

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")
