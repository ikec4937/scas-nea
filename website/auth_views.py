from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth_views", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pword")

        user = User.query.filter_by(email=email).first() #search through all emails
        if user:
            if check_password_hash(user.password, password):
                flash("You're in!", category="success")
                login_user(user, remember=True) #Remembers the user, till the server shuts down or the web server restarts
                return redirect(url_for("views.home"))
            else:
                flash("Your password is incorrect", category="error")
        else:
            flash("Your email does not exist with us", category="error")
    
    return render_template("login.html", user=current_user)

@app.route("/logout-user")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_views.index"))

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
        elif stat_check == "":
            flash("Are you a student or a teacher?", category="error")
        else:
            new_user = User(email=email, firstname=firstname, lastname=lastname, secondary_school=s_school, if_admin=stat_check,  password=generate_password_hash(password2, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("You're in!", category="success")
            return redirect(url_for("main_views.index"))
    
    return render_template("registration.html")