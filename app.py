from flask import Flask, render_template, request, url_for
from ChatBot import chat

# application
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def welcome():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usrn = request.form["username"]
        psw = request.form["password"]
        return render_template("index.html")
    else:
        return render_template("login.html")


@app.route("/chat")
def chat():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()