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
        #grade = Grade.query.filter_by(student_id=session["user"].id).first()
        #session["grade"] = grade.serialise()
        
        if request.method == "POST":
            coursetype = request.form.get("coursetype")
            boardname = request.form.get("boardname")
            subject = request.form.get("subject")
            grade_score = request.form.get("grade_score")
            
            if len(subject) < 2:
                flash("Enter the FULL name of your subject", category="error")
            elif coursetype == "none_selected": 
                flash("Enter the type of course you have studied", category="error")
            elif boardname == "none_selected": 
                flash("Enter your course's board", category="error")
            elif grade_score == "none":
                flash("Enter your grade", category="error")
            else:
                new_user = Grade(student_id=session["user"]["id"], coursetype=coursetype, subject=subject, boardname=boardname, grade_score=grade_score)
                db.session.add(new_user)
                db.session.commit()
                
                flash("Grade Successfully added", category="success")
        
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

            new_grade = Grade(session["user"].uID, subject=subject, coursetype=coursetype, gradescore=gradescore)
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
