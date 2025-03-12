from peewee import ModelSelect

from source.scripts.models import Log, SpaceType, EventType, Comment, User, Post

def get_sql_logs_from_user(user_id: int) -> ModelSelect:
	"""
	from database select date of log, log id, event type id, space type id, where Log.user_id == user_id
	:param user_id:
	:return:
	"""
	return (
		Log
		.select(
			Log.datetime,
			Log.event_type_id,
			Log.space_type_id,
			Log.id
		)
		.where(Log.user_id == user_id)
	)

def get_sql_comments_from_user(user_id: int) -> ModelSelect:
	"""
	from database select id of comment and id of post related to comment,
	where id author comment equal to user_id
	:param user_id:
	:return:
	"""
	return (
		Comment
		.select(
			Comment.id,
			Comment.post_id
		)
		.where(Comment.author_id == user_id)
	)