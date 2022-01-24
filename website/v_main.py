from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for

main = Blueprint("v_main", __name__)


@main.route("/")
def startup():
    session["logged_in"] = False
    return redirect(url_for("v_main.index"))

@main.route("/home")
def index():
    return render_template("index.html")

@main.route("/search")
def search():
    return "<h1>Search<h1>"

@main.errorhandler(404)
def not_found(e):
    return render_template("404_page.html")

@main.route("/register")
def registration():
    if session["logged_in"]:
        return redirect(url_for("v_postlogin.student_hub"))
    else:
        return render_template("registration.html")