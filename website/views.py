from flask import Blueprint
from flask import render_template, request, url_for, redirect
from flask_login import login_required, logout_user, current_user
from website import db
from .ai_chatbot.ChatBot import botchat
from .models import History

views = Blueprint('views', __name__)


@views.route("/chat")
@login_required
def chat():
    return render_template('chat.html')


@views.route("/get")
@login_required
def get():
    # import function for botchat
    msg = request.args.get('msg')
    bot_reply = botchat(str(msg))

    # save users chat history in database
    new_note = History(data=msg+", "+bot_reply, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()

    # return bot reply to chat page
    return bot_reply
