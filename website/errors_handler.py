from flask import Blueprint, redirect, render_template
errors_handler = Blueprint('errors_handler', __name__)


# 404 (Not Found)
@errors_handler.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')


# 401 (Unauthorized)
@errors_handler.app_errorhandler(401)
def not_found(error):
    return render_template('errors/401.html')


# 500 (Internal Server Error)
@errors_handler.app_errorhandler(500)
def not_found(error):
    return render_template('errors/500.html')
