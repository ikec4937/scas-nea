from flask import (
    Blueprint, 
    render_template, 
    redirect, url_for,
    request, flash, 
    jsonify, 
    session
)

plog = Blueprint("v_postlogin", __name__)

@plog.route("/student-hub")
def student_hub():
    if session["logged_in"]: 
        if session["is_student"]:
            return render_template("hub_student.html") #alphabetical order will look nice, this way
        else:
            return redirect(url_for("v_postlogin.admin_hub"))
    else:
        flash("You need to log in or register to access this page", category="error")
        return redirect(url_for("v_auth.login"))

@plog.route("/admin-hub")
def admin_hub():
    if session["logged_in"]: 
        if session["is_student"]:
            return redirect(url_for("v_postlogin.student_hub"))
        else:
            return render_template("hub_admin.html")
    else:
        flash("You need to log in or register to access this page", category="error")
        return redirect(url_for("v_auth.login"))