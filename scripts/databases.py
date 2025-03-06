from peewee import *
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = 'databases/'

logs = os.getenv("logs_database")
authors = os.getenv("authors_database")

logs_db = SqliteDatabase(DATABASES + logs)
authors_db = SqliteDatabase(DATABASES + authors)