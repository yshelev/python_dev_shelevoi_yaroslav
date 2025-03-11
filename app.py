from scripts.scripts.models import *
from flask import Flask, request

from scripts.scripts.services import (
    get_dict_count_of_logins_logouts_and_blog_activities_by_date,
    get_dict_quantity_of_comments_in_post
)

app = Flask(__name__)

@app.route("/api/comments", methods=['GET'])
def comments_of_user():
    username = request.args.get("username")

    authors_db_manager.create_connection()
    user = User.get(User.login == username)

    sql_output = get_dict_quantity_of_comments_in_post(user.id)
    authors_db_manager.drop_connection()

    print(sql_output)

    final_output = [{
        "login": user.login,
        "header": row['header'],
        "post_author_login": row['post_author_login'],
        "number_of_comments": row['number_of_comments'],
    } for row in sql_output]
    return final_output

@app.route("/api/general", methods=['GET'])
def general_info_about_user():
    username = request.args.get("username")

    authors_db_manager.create_connection()
    user = User.get(User.login == username)
    authors_db_manager.drop_connection()

    logs_db_manager.create_connection()
    sql_output = get_dict_count_of_logins_logouts_and_blog_activities_by_date(user.id)
    logs_db_manager.drop_connection()

    final_output = [{
        "date": log['date'],
        "login_count": log['login_count'],
        "logout_count": log['logout_count'],
        "blog_activities_count": log['blog_activities_count'],
    } for log in sql_output]
    return final_output

if __name__ == '__main__':
    app.run(debug=True)