from flask import Flask

app = Flask(__name__)

@app.route("/api/comments/<username>")
def comments_of_user():
    return 123

@app.route("/api/general/<username>")
def general():
    return 123