from . import db
from sqlalchemy.sql import func

"""
Now begs the question: How will the database be modeled?
Application Model can be found on the dbdiagram.io
"""

class Admin(db.Model):
    __tablename__ = "admin"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))

    school = db.relationship("School")

    def serialise(self):
        return {
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

class Student(db.Model):
    __tablename__ = "student"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))

    grades = db.relationship("Grade")
    
    
    def serialise(self):
        return {
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        } 
    
    """tags = db.relationship("Tags", backref="student")
    application_id = db.Column(db.Integer, db.ForeignKey("application.id"))"""

class Grade(db.Model):
    __tablename__ = "grades"
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    boardname = db.Column(db.String(50))
    qualif = db.Column(db.String(50))
    grade_score = db.Column(db.String(15))
    
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    def serialise(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'coursetype': self.qualif,
            'grade_score': self.grade_score,
            'student_id': self.student_id
        }

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #student_id = db.relationship("Student", backref="application")
    #school_id = db.Column(db.Integer, db.ForeignKey("school.id"))

class School(db.Model):
    __tablename__ = "school"
    
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100))
    cont_number = db.Column(db.String(11)) #It'd be weird to enter it as an integer. Don't ask why.
    contact_email = db.Column(db.String(100)) #Could be long
    description = db.Column(db.Text)

    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))

    def serialise(self):
        return {
            "id": self.id, #It's copy-pasted from the json file, so that's why it's in double quotes
            "school_name": self.school_name,
            "cont_number": self.cont_number,
            "contact_email": self.contact_email,
            "description": self.description
        }