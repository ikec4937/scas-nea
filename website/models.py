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