from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #Initialising
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "bvrjokevwaiubadonaeionjiewonvuabiqw"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    #URLs from other files
    from .v_main import main
    from .v_auth import auth
    from .v_postlogin import plog

    #Registering blueprints
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(plog, url_prefix="/")

    #NEEDS TO BE LOADED AND RUN BEFORE DATABASE IS INITIALISED
    from .models import Student, Admin
    
    create_database(app)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database")