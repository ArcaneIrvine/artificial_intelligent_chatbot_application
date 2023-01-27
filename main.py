from flask import render_template, request, url_for, flash, redirect
from website import create_app
app = create_app()


@app.route("/", methods=["POST", "GET"])
def welcome():
    return redirect(url_for('auth.signup'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
