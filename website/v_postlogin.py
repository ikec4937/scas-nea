from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

plog = Blueprint("v_postlogin", __name__)

@plog.route("/student-hub")
@login_required
def student_hub():
    return render_template("student_hub.html", user=current_user)

@plog.route("/admin-hub")
@login_required
def admin_hub():
    pass