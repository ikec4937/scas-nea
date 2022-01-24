from flask import (
    Blueprint, 
    render_template, 
    redirect, url_for,
    request, flash, 
    jsonify, 
    session
)
from .models import Grade
from . import db

plog = Blueprint("v_postlogin", __name__)

@plog.route("/student/hub")
def student_hub():
    if session["logged_in"]: 
        if session["is_student"]:
            return render_template("hub_student.html") #alphabetical order will look nice, this way
        else:
            return redirect(url_for("v_postlogin.admin_hub"))
    else:
        flash("You need to log in or register to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/student/manage-grades")
def manage_grades():
    if session["logged_in"] and session["is_student"]:
        return render_template("mang_grades.html")
    else:
        flash("You are not logged in as a student to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/student/edit-schools")
def student_edit_school():
    if session["logged_in"] and session["is_student"]:
        return render_template("edit_school_s.html")
    else:
        flash("You are not logged in as a student to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/student/manage-application")
def student_manage_application():
    if session["logged_in"] and session["is_student"]:
        if request.method == "POST":
            subject = request.form.get("subject")
            coursetype = request.form.get("coursetype")
            gradescore = request.form.get("gradescore")
            
            #And then I need to add some variables here and there to ensure that I'm pushing in data that exists.

            new_grade = Grade(session["uID"].uID, subject=subject, coursetype=coursetype, gradescore=gradescore)
            db.session.add(new_grade)
            db.session.commit()
        
        return render_template("mang_application.html")
    else:
        flash("You are not logged in as a student to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/admin/hub")
def admin_hub():
    if session["logged_in"]: 
        if session["is_student"]:
            return redirect(url_for("v_postlogin.student_hub"))
        else:
            return render_template("hub_admin.html")
    else:
        flash("You need to log in or register to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/admin/edit-school")
def admin_edit_school():
    return render_template("edit_school_a.html")

"""
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
"""
