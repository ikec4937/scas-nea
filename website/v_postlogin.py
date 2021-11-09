from flask import (
    Blueprint, 
    render_template, 
    redirect, url_for,
    request, flash, 
    jsonify, 
    session
)
#from flask_login import login_required, current_user

plog = Blueprint("v_postlogin", __name__)

@plog.route("/student-hub")
def student_hub():
    if session["logged_in"] and session["is_student"]:
        return render_template("student_hub.html")
    else:
        return redirect(url_for("v_main.index"))


@plog.route("/admin-hub")
def admin_hub():
    pass