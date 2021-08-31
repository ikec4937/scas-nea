from flask import Blueprint, render_template

main = Blueprint("main_views", __name__)

@main.route("/")
def index():
    return "<h1>Home</h1>"