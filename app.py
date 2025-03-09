from scripts.models import *
from flask import Flask, request

from scripts.services import (
    get_count_of_logins_logouts_and_blog_activities_by_date,
    create_connection,
    discard_connection
)

app = Flask(__name__)

@app.route("/api/comments", methods=['GET'])
def comments_of_user():
    username = request.args.get("username")

    return 123

@app.route("/api/general", methods=['GET'])
def general_info_about_user():
    username = request.args.get("username")

    create_connection(authors_db)
    user = User.get(User.login == username)
    discard_connection(authors_db)

    create_connection(logs_db)
    sql_output = get_count_of_logins_logouts_and_blog_activities_by_date(user.id)
    discard_connection(logs_db)

    final_output = [{
        "date": log.date,
        "login_count": log.login_count,
        "logout_count": log.logout_count,
        "blog_activities_count": log.blog_activities_count,
    } for log in sql_output]
    return final_output