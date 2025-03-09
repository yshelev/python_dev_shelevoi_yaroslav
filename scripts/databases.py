from peewee import SqliteDatabase
import os
from dotenv import load_dotenv

load_dotenv()
DATABASES = 'databases/'

logs = os.getenv("logs_database")
authors = os.getenv("authors_database")

logs_db = SqliteDatabase(DATABASES + logs, pragmas= {
	'foreign_keys': 1
})
authors_db = SqliteDatabase(DATABASES + authors, pragmas= {
	'foreign_keys': 1
})