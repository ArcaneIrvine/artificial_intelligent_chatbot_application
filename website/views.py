from flask import Blueprint
from flask import render_template, request, url_for, redirect
from .ai_chatbot.ChatBot import botchat

views = Blueprint('views', __name__)


@views.route("/chat")
def chat():
    return render_template('chat.html')


@views.route("/get")
def get():
    # import function for botchat
    msg = request.args.get('msg')
    bot_reply = botchat(str(msg))
    print(str(msg))
    return bot_reply
