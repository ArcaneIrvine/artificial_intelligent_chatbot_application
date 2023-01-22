from flask import Flask, render_template, request, url_for, flash
from website import create_app
app = create_app()


@app.route("/", methods=["POST", "GET"])
def welcome():
    return render_template("signup.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


if __name__ == "__main__":
    app.run(debug=True)
