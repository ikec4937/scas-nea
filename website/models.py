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

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))

    def serialise(self):
        return {
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))

    def serialise(self):
        return {
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }
    
    """grades = db.relationship("Grade", backref="student")
    tags = db.relationship("Tags", backref="student")
    application_id = db.Column(db.Integer, db.ForeignKey("application.id"))"""

class Grade(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    grade_score = db.Column(db.String(15))
    #student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

class Application(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #student_id = db.relationship("Student", backref="application")
    #school_id = db.Column(db.Integer, db.ForeignKey("school.id"))

class School(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.column(db.String(100))
    description = db.column(db.Text)
    #admins = db.relationship("Application", backref="school")
    #There are other things, I don't know what they are though.