from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

main = Blueprint("v_main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/search")
def search():
    return "<h1>Search<h1>"

@main.errorhandler(404)
def not_found(e):
    return render_template("404_page.html")

@main.route("/main")
def registration():
    return render_template("registration.html")