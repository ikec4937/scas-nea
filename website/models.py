from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""
Now begs the question: How will the database be modeled?

Application:
- Application ID
- User ID
- School ID
- User Grades
"""

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    secondary_school = db.Column(db.String(250))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    if_admin = db.Column(db.String(20))

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.relationship("User", db.ForeignKey("user.id"))
    grade_id = db.relationship("Grade")

class Grade(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    grade_score = db.Column(db.String(15))

class Application(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.relationship("Student")

class School(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.column(db.String(100))
    description = db.column(db.Text)
    contact_email = db.Column(db.String(150), unique=True)
    admin_ids = db.relationship("Application")
    #There are other things, I don't know what they are though.