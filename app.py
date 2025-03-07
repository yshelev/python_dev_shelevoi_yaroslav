from scripts.models import *
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/comments/<username>", methods=['GET'])
def comments_of_user():

    return 123

@app.route("/api/general/<username>", methods=['GET'])
def general_info_about_user():
    username = request.args.get("username")

    user = User.get(User.login == username)

    request_ = Log.select().where(Log.user_id == user.id)

    print([i for i in request_])
    return 'smth'