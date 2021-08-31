from flask import Blueprint, render_template

auth = Blueprint("auth_views", __name__)

@auth.route("/login")
def login():
    return "<h1>Login</h1>"

@auth.route("/register")
def registration():
    return render_template("registration.html")