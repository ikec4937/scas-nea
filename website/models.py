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

class Application:
    id = db.Column(db.Integer, primary_key=True)
    student = db.relationship("Student")
    school = db.relationship("School")

class Grade(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    student = db.relationship("Student") #one-to-one with Student
    grade_name = db.Column(db.String(50))
    grade_score = db.Column(db.String(15)) #In case of large grade names like "Distinction"

class School(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.relationship("Admin") #one-to-one with Admin
    school_name = db.column(db.String(100))
    description = db.column(db.String(25000))
    contact_email = db.Column(db.String(150), unique=True)
    site_link = db.column(db.String(400))
    #There are other things, I don't know what they are though

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
    user = db.relationship("User") #one-to-one relationship with the student's details, if that's how it works.
    application = db.relationship("Application") #one to many relationship with the student's applications to multiple schools
    grade = db.relationship("Grade") #One-to-many relationship with the student's grades

class Admin(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.relationship("User") #one-to-one relationship with the admin, if that's how it works.
    school = db.relationship("School") #one-to-one relationship with the admin's school