# orm layer over sqlite3

import re
import sqlite3


class DB:
    _uri = 'temp.db'
    _conn = None
    _cursor = None

    def __init__(self):
        self._conn = sqlite3.connect(self._uri)
        self._cursor = self._conn.cursor()
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER,
                username TEXT,
                password TEXT
            )
        ''')
        self._conn.commit()
        self._cursor.execute('INSERT INTO users VALUES(123, "admin", "password")')
        self._conn.commit()

    def __del__(self):
        self._conn.close()

    def query(self, query, session):
        # check for attacks
        if 'DROP' in query or 'DELETE' in query or 'INSERT' in query or 'UPDATE' in query or 'SELECT' not in query and session['role'] != 'admin':
            return 'Invalid query'
        # match regex to check for attacks
        elif re.match(r'[\w\s]+', query):
            return 'Invalid query'
        self._cursor.execute(query)
        return self._cursor.fetchall()


import shutil
import datetime

def backup_database():
    source_path = "/path/to/database.db"
    backup_folder = "/path/to/backup/"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"database_backup_{timestamp}.db"

    destination_path = backup_folder + backup_filename
    shutil.copyfile(source_path, destination_path)
    print("Database backup created:", destination_path)

# Example usage
# backup_database()