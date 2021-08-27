from flask import Flask, Blueprint

def create_app():
    #Initialising
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "bvrjokevwaiubadonaeionjiewonvuabiqw"
    
    #URLs from other files
    from .main_views import main
    from .auth_views import auth

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app