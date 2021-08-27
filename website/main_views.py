from flask import Blueprint, render_template

main = Blueprint("main_views", __name__)

@main.route("/")
def home():
    return "<h1>Home</h1>"