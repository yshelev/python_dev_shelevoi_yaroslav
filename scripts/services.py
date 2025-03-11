from .constants import CASES
from peewee import fn, SqliteDatabase

from scripts.models import Log, SpaceType, EventType, Comment, User, Post


def create_connection(table: SqliteDatabase) -> bool:
	try:
		table.connect()
		return True
	except Exception as e:
		return False

def discard_connection(table: SqliteDatabase) -> bool:
	try:
		table.close()
		return True
	except Exception as e:
		return False

def get_dict_count_of_logins_logouts_and_blog_activities_by_date(user_id: int):
	check_on_event_type_equal_login = CASES["EVENT_TYPE"]["EQUAL_LOGIN"]
	check_on_event_type_equal_logout = CASES["EVENT_TYPE"]["EQUAL_LOGOUT"]
	check_on_space_type_equal_blog = CASES["SPACE_TYPE"]["EQUAL_BLOG"]
	return (
        Log
        .select(
            Log.datetime.alias("date"),
            fn.SUM(check_on_event_type_equal_login).alias("login_count"),
            fn.SUM(check_on_event_type_equal_logout).alias("logout_count"),
            fn.SUM(check_on_space_type_equal_blog).alias("blog_activities_count"),
        )
        .join(SpaceType)
        .switch(Log)
        .join(EventType)
        .where(Log.user_id == user_id)
        .group_by(Log.datetime)
        .order_by(Log.datetime)
		.dicts()
    )


def get_dict_quantity_of_comments_in_post(user_id: int):
	return (
		Comment
		.select(
			User.login.alias("post_author_login"),
			Post.header.alias("header"),
			fn.COUNT(Comment.id).alias("number_of_comments"),
		)
		.join(Post)
		.join(User)
		.switch(Post)
		.where(Comment.author_id == user_id)
		.group_by(Post.id)
		.dicts()
	)