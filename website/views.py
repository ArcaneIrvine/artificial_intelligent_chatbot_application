from flask import Blueprint
from flask import render_template, request

views = Blueprint('views', __name__)


@views.route('/chat', methods=["POST", "GET"])
def get_bot_response():
    from .ai_chatbot.ChatBot import botchat

    if request.method == "POST":
        msg = request.form['msg']
        return botchat(msg)
    return render_template("chat.html")
