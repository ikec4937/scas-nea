from flask import Flask

@app.route("/student-hub")
@login_required
def student_hub():
    pass

@app.route("/admin-hub")
@login_required
def admin_hub():
    pass