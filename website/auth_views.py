from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth_views", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return "<h1>Login</h1>"

@auth.route("/register", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        s_school = request.form.get("sschool") #What secondary school the user is registering for/from
        stat_check = request.form.get("statcheck") #If the student is an admin
        password = request.form.get("pword")
        password2 = request.form.get("pword2")
    
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstname) < 2: 
            flash("You must have a name to enter the site", category="error")
        elif len(lastname) < 2: 
            flash("You must have a FULL name to enter the site", category="error")
        elif len(s_school) < 2: 
            flash("You must go to a school to enter the site", category="error")
        elif password != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = User(email=email, firstname=firstname, lastname=lastname, secondary_school=s_school, if_admin=statcheck,  password=generate_password_hash(password2, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("You're in!", category="success")
            redirect(url_for("main_views.index"))
    
    return render_template("registration.html")