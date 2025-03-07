from databases import *

# LOGS DATABASE CLASSES
class BaseLogModel(Model):
	class Meta:
		database = logs_db

class SpaceType(BaseLogModel):
	id = PrimaryKeyField()
	name = CharField()


class EventType(BaseLogModel):
	id = PrimaryKeyField()
	name = CharField()


class Log(BaseLogModel):
	id = PrimaryKeyField()
	datetime = DateField()
	user_id = IntegerField()
	space_type_id = ForeignKeyField(SpaceType.id)
	event_type_id = ForeignKeyField(EventType.id)


# AUTHORS DATABASE CLASSES
class BaseAuthorModel(Model):
	class Meta:
		database = authors_db


class User(BaseAuthorModel):
	id = PrimaryKeyField()
	email = CharField(unique=True)
	login = CharField(unique=True)


class Blog(BaseAuthorModel):
	id = PrimaryKeyField()
	owner_id = ForeignKeyField(User.id)
	name = CharField()
	description = CharField()


class Post(BaseAuthorModel):
	id = PrimaryKeyField()
	author_id = ForeignKeyField(User.id)
	header = TextField()
	text = TextField()
	blog_id = ForeignKeyField(Blog.id)