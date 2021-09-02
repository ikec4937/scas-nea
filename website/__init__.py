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
    from .main_views import main
    from .auth_views import auth

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    
    create_database(app)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database")