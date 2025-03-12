from source.constants.cases import CASES
from peewee import fn

from source.scripts.services.optimize_services import (
	get_logs_from_user,
	get_comments_from_user,
)

from source.scripts.models import (
	Log,
	SpaceType,
	EventType,
	Comment,
	User,
	Post
)

def get_general_data(user_id: int) -> list[dict]:
	"""
	get list of dicts with structure: {\n
		"date": string\n
		"login_count": int,\n
		"logout_count": int,\n
		"blog_activities_count": int
	}
	:param user_id:
	:return:
	"""
	check_on_event_type_equal_login = CASES["EVENT_TYPE"]["EQUAL_LOGIN"]
	check_on_event_type_equal_logout = CASES["EVENT_TYPE"]["EQUAL_LOGOUT"]
	check_on_space_type_equal_blog = CASES["SPACE_TYPE"]["EQUAL_BLOG"]

	optimized_logs = get_logs_from_user(user_id)

	return (
        optimized_logs
        .select(
            Log.datetime.alias("date"),
            fn.SUM(check_on_event_type_equal_login).alias("login_count"),
            fn.SUM(check_on_event_type_equal_logout).alias("logout_count"),
            fn.SUM(check_on_space_type_equal_blog).alias("blog_activities_count"),
        )
        .join(SpaceType)
        .switch(Log)
        .join(EventType)
        .group_by(Log.datetime)
        .order_by(Log.datetime)
		.dicts()
    )


def get_comments_data(user_id: int) -> list[dict]:
	"""
	get list of dicts with structure: {\n
		"post_author_login": string\n
		"header": string,\n
		"number_of_comments": int,
	}
	:param user_id:
	:return:
	"""
	optimized_comments = get_comments_from_user(user_id)

	return (
		optimized_comments
		.select(
			User.login.alias("post_author_login"),
			Post.header.alias("header"),
			fn.COUNT(Comment.id).alias("number_of_comments"),
		)
		.join(Post)
		.join(User)
		.group_by(Post.id)
		.dicts()
	)