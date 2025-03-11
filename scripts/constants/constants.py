import os

from dotenv import load_dotenv

load_dotenv()

DATABASES_PATH = 'databases/'
LOGS_PATH = DATABASES_PATH + os.getenv("logs_database")
AUTHORS_PATH = DATABASES_PATH + os.getenv("authors_database")