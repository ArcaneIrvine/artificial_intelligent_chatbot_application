import os
from os import path
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# define new database
db = SQLAlchemy()
DB_NAME = "database.db"

# define mail
mail = Mail()


# app create function
def create_app():
    app = Flask(__name__)

    app.secret_key = os.urandom(12).hex()
    # store database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize database
    db.init_app(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    # on a production environment store credentials on environment variables for safety reasons
    app.config['MAIL_USERNAME'] = 'arcaneirvinetest@gmail.com'
    app.config['MAIL_PASSWORD'] = 'lpajewxwifnhclex'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # initialize mail
    mail.init_app(app)

    # register blueprints
    from .views import views
    from .auth import auth
    from .errors_handler import errors_handler
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(errors_handler)

    # create database
    from .models import User, History
    create_database(app)

    # create login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# database create function
def create_database(app):
    if not path.exists('instance/'+DB_NAME):
        with app.app_context():
            db.create_all()
            print('database created')


