import sqlite3

from config import DATABASE_DIR, create_DATA_DIR

def create_connection():

    create_DATA_DIR()

    return sqlite3.connect(DATABASE_DIR)


def create_table():

    connection = create_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS code_index(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL,
            content TEXT NOT NULL
            )
            '''
        )

        connection.commit()

    finally:

        connection.close()


def clear_index():

    connection = create_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''DELETE FROM code_index'''
        )

        connection.commit()

    finally:

        connection.close()


def insert_file(path, content):

    connection = create_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            '''
            INSERT INTO code_index(path, content)
            VALUES ( ? , ?)
            ''', (str(path), content)
        )

        connection.commit()

    finally:

        connection.close()

def search_code(keyword):

    connection = create_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            '''
            SELECT path, content FROM code_index
            WHERE content LIKE ?
            ''', (f"%{keyword}%")
        )

        return cursor.fetchall()

    finally:

        connection.close()
