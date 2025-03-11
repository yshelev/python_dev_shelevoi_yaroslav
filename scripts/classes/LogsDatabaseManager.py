from dotenv import load_dotenv
import os

from peewee import SqliteDatabase

from scripts.constants.constants import LOGS_PATH

from scripts.classes.DatabaseManager import DatabaseManager



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
