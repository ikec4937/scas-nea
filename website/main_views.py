from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

main = Blueprint("main_views", __name__)

@main.route("/")
@login_required
def index():
    return render_template("index.html")

@main.route("/search")
def search():
    return "<h1>Search<h1>"

@main.route("/about")
def about():
    return "<h1>About<h1>"

@main.route('/school')
def student_hub():
    return "<h1>School<h1>"