from flask import Blueprint, render_template

auth = Blueprint("auth_views", __name__)

@views.route("/")
def home():
    return render_template("home.html")