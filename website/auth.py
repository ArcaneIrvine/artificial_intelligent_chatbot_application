from random import randint
from website import db, mail
from website.models import User
from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect, session
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        usrn = request.form["username"]
        psw1 = request.form["password1"]
        psw2 = request.form["password2"]

        # create user and check if there is another user with the same email
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User with that email already exists', category='error')

        elif len(email) < 6:
            flash('Email must be at least 6 characters', category='error')
        # check if passwords match
        elif psw1 != psw2:
            flash('Passwords do not match', category='error')
        elif len(psw1) < 6:
            flash('Password must be at least 6 characters', category='error')
        elif len(usrn) < 2:
            flash('Nickname must be longer than 2 characters', category='error')
        # otherwise add user to the database
        else:
            # generate otp and send to users email
            otp = randint(000000, 999999)
            session['otp_'] = otp
            session['email_'] = email
            session['usrn_'] = usrn
            session['psw_'] = psw1
            msg = Message('OTP', sender='arcaneirvinetest@gmail.com', recipients=[str(email)])
            msg.body = str(otp)
            mail.send(msg)
            return redirect(url_for('auth.verify'))
    return render_template("signup.html")


@auth.route("/verify", methods=["POST", "GET"])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if int(user_otp) == session.get('otp_', None):
            # create new user, store password with a hash for security reasons
            new_user = User(email=session.get('email_', None), username=session.get('usrn_', None), password=generate_password_hash(session.get('psw_', None), method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Signed up successfully!', category='success')
            # log in user module, remember user
            login_user(new_user, remember=True)
            return redirect(url_for('views.chat'))
        else:
            flash('the code you entered was not right', category='error')

    return render_template('verify.html')


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        psw = request.form["password"]
        # check if user exists in the database
        user = User.query.filter_by(email=email).first()
        if user:
            # check if the password matches with that users saved password in the database
            if check_password_hash(user.password, psw):
                flash('Logged in successfully!', category='success')
                # log in user module, remember user
                login_user(user, remember=True)
                return redirect(url_for('views.chat'))
            # if it doesn't ask to enter  password again
            else:
                flash('Incorrect password, try again', category='error')
        # if user doesn't exist with than nickname ask user to signup first
        else:
            flash('User does not exist. Please sign up first', category='error')
    return render_template("login.html")


@auth.route("/logout", methods=["POST", "GET"])
def logout():
    # log out user
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for("auth.login"))
