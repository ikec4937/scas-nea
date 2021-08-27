from flask import Blueprint, render_template

main = Blueprint("main_views", __name__)

@views.route("/")
def home():
    return render_template("home.html")