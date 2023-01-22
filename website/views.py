from flask import Blueprint
from flask import Flask, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("/signup.html")