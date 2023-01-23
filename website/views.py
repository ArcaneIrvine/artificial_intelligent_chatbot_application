from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)


@views.route('/chat', methods=["POST", "GET"])
def chat():
    return render_template("chat.html")