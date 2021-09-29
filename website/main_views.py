from flask import Blueprint, render_template

main = Blueprint("main_views", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/search")
def search():
    return "<h1>Search<h1>"

@main.route("/about")
def about():
    return "<h1>About<h1>"

@app.route('/school')
def student_hub():
    pass