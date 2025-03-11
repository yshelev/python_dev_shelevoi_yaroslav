from peewee import SqliteDatabase

from scripts.constants.constants import AUTHORS_PATH

from scripts.classes.DatabaseManager import DatabaseManager



class AuthorDatabaseManager(DatabaseManager):
	def __init__(self):
		self.__path_to_database = AUTHORS_PATH
		self.__create_database_instance()

		super().__init__(self.__database_instance)

	def __create_database_instance(self):
		self.__database_instance = SqliteDatabase(
			self.__path_to_database,
			pragmas={
				'foreign_keys': 1
			}
		)