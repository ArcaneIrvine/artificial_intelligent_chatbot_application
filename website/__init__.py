import os
from .views import views
from .auth import auth
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(12).hex()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
