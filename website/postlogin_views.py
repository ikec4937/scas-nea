from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

plog = Blueprint("postlogin_views", __name__)

@plog.route("/student-hub")
@login_required
def student_hub():
    return render_template("student_hub.html", student=current_user.firstname)

@plog.route("/admin-hub")
@login_required
def admin_hub():
    pass