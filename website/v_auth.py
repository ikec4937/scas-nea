from flask import ( #Didn't know you could do this. Cool.
    Blueprint, 
    render_template, 
    request, 
    flash, 
    redirect, url_for,
    session, g
)
from werkzeug.security import (generate_password_hash, check_password_hash)
from .models import Student, Admin
from . import db

import json

auth = Blueprint("v_auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("uID", None)

        email = request.form.get("email")
        password = request.form.get("pword")
        stat_check = request.form.get("loginas")

        if stat_check == "student":
            student = Student.query.filter_by(email=email).first() #search through all emails
            if student:
                if check_password_hash(student.password, password): #If the student is found, look through the passwords of the users.
                    session["logged_in"] = True #The user is logged in
                    session["is_student"] = True #...as a student
                    session["uID"] = student.serialise() #Their first name, last name and email is saved.
                    flash("You're in as a student!", category="success")
                    return redirect(url_for("v_postlogin.student_hub"))
                else:
                    flash("Your password is incorrect", category="error")
            else:
                flash("Your student email does not exist with us", category="error")
        
        elif stat_check == "admin":
            admin = Admin.query.filter_by(email=email).first()
            if admin:
                if check_password_hash(admin.password, password):
                    flash("You're in as an admin!", category="success")
                    session["logged_in"] = True
                    session["is_student"] = False
                    session["uID"] = admin.serialise()
                    return redirect(url_for("v_postlogin.admin_hub"))
                else:
                    flash("Your password is incorrect", category="error")
            else:
                flash("Your admin email does not exist with us", category="error")
        
        else:
            flash("Are you a student or an admin?", category="error")
    
    return render_template("login.html")

@auth.route("/logout-user")
def logout():
    session.pop("uID", None)
    session.pop("is_student", None)
    session["logged_in"] = False
    return redirect(url_for("v_main.index"))

@auth.route("/register-student", methods=["GET", "POST"])
def reg_student():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        password = request.form.get("pword")
        password2 = request.form.get("pword2")
    
        user = Student.query.filter_by(email=email).first()
        if user: #If the user's email has been found in the database,
            flash("Your email already exists with us", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstname) < 2: 
            flash("You must have a name to enter the site", category="error")
        elif len(lastname) < 2: 
            flash("You must have a FULL name to enter the site", category="error")
        elif password != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = Student(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password2, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            session["logged_in"] = True
            session["is_student"] = False
            session["uID"] = [new_user.id, firstname, lastname, email]
            flash("You're in!", category="success")
            return redirect(url_for("v_postlogin.student_hub"))
    
    return render_template("reg_student.html")

@auth.route("/register-admin", methods=["GET", "POST"])
def reg_admin():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        password = request.form.get("pword")
        password2 = request.form.get("pword2")
    
        user = Admin.query.filter_by(email=email).first()
        if user: #If the user's email has been found in the database,
            flash("Your email already exists with us", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstname) < 2: 
            flash("You must have a name to enter the site", category="error")
        elif len(lastname) < 2: 
            flash("You must have a FULL name to enter the site", category="error")
        elif password != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = Admin(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password2, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            session["logged_in"] = True
            session["is_student"] = False
            session["uID"] = [new_user.id, firstname, lastname, email]
            flash("You're in!", category="success")
            return redirect(url_for("v_postlogin.admin_hub"))
    
    return render_template("reg_admin.html")