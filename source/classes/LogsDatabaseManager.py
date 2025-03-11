from peewee import SqliteDatabase

from source.constants.constants import LOGS_PATH

from source.classes.DatabaseManager import DatabaseManager



class LogsDatabaseManager(DatabaseManager):
	def __init__(self):
		self.__path_to_database = LOGS_PATH
		self.__create_database_instance()

		super().__init__(self.__database_instance)

	def __create_database_instance(self):
		self.__database_instance = SqliteDatabase(
			self.__path_to_database,
			pragmas={
				'foreign_keys': 1
			}
		)
