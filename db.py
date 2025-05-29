import sqlite3

CONNECTION_DB = sqlite3.connect("agendapet.db")
CLOSE_CONNECTION = CONNECTION_DB.close()
CURSOR = CONNECTION_DB.cursor()


