import flask
from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, logout_user, current_user
from website import db
from .ai_chatbot.ChatBot import botchat
from .models import History, Bot, User

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

    # save what the users question was if the bot didn't know how to reply
    if bot_reply == 'Sorry, i did not understand, please try again.':
        new_question = Bot(question=msg)
        db.session.add(new_question)
        db.session.commit()

    # save users chat history in database
    new_note = History(data=msg+", "+bot_reply, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()

    # return bot reply to chat page
    return bot_reply


@views.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    if request.method == "POST":
        # delete user and his chat history
        User.query.filter_by(id=current_user.id).delete()
        History.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()

        flash('User succesfully deleted!', category='success')
        return redirect(url_for('auth.signup'))
    return render_template('profile.html')

