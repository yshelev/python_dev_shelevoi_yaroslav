from databases import *

# LOGS DATABASE CLASSES
class Space_type(Model):
	id = PrimaryKeyField()
	name = CharField()

	class Meta:
		database = logs_db


class Event_type(Model):
	id = PrimaryKeyField()
	name = CharField()

	class Meta:
		database = logs_db


class Logs(Model):
	id = PrimaryKeyField()
	datetime = DateField()
	user_id = IntegerField()
	space_type_id = ForeignKeyField(Space_type.id)
	event_type_id = ForeignKeyField(Event_type.id)

	class Meta:
		database = logs_db

# AUTHORS DATABASE CLASSES
pass