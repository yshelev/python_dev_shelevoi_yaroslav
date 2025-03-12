from peewee import SqliteDatabase


class DatabaseManager:
	__database_instance = None
	__path_to_database = None

	def __init__(self, database_instance):
		self.__database_instance = database_instance

	def __create_database_instance(self):
		pass

	def create_connection(self):
		self.__database_instance.connect()

	def drop_connection(self):
		self.__database_instance.close()

	def get_database_instance(self) -> SqliteDatabase:
		return self.__database_instance