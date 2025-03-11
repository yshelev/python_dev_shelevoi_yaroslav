from source.scripts.databases import logs_db_manager, authors_db_manager

def create_connection_with_two_databases():
	logs_db_manager.create_connection()
	authors_db_manager.create_connection()

def drop_connection_with_two_databases():
	logs_db_manager.drop_connection()
	authors_db_manager.drop_connection()