from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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
    from .postlogin_views import plog

    #Registering blueprints
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(plog, url_prefix="/")

    #NEEDS TO BE LOADED AND RUN BEFORE DATABASE IS INITIALISED
    from .models import Student, Admin
    
    create_database(app)

    #Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth_views.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_student(id):
        return Student.query.get(int(id))
    
    @login_manager.user_loader
    def load_admin(id):
        return Admin.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database")