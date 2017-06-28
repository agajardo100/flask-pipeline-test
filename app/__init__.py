from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Local
from config import app_config

flask_bcrypt = Bcrypt()

# db variable initialization
db = SQLAlchemy() 

# Flask-Login
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    Bootstrap(app)          # Init Flask-Bootstrap
    db.init_app(app)        # Init SQLAlchemy
    flask_bcrypt.init_app(app)        # Init BCrypt
    
    # Init Flask-login
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"

    migrate = Migrate(app, db)

    from app import models
    
    # Blueprints
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app