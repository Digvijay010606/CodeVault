import sqlite3

from config import DATABASE_PATH, create_data_directory


def create_connection():
    """Create and return a SQLite database connection."""

    create_data_directory()

    try:
        return sqlite3.connect(DATABASE_PATH)

    except sqlite3.Error as error:
        print(f"Database connection error: {error}")
        return None


def create_table():
    """Create the code index table if it does not exist."""

    connection = create_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS code_index (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )

        connection.commit()

    except sqlite3.Error as error:
        print(f"Error creating table: {error}")

    finally:
        connection.close()


def clear_index():
    """Remove all indexed files from the database."""

    connection = create_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM code_index")

        connection.commit()

    except sqlite3.Error as error:
        print(f"Error clearing index: {error}")

    finally:
        connection.close()


def insert_file(path, content):
    """Insert a file into the code index."""

    connection = create_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO code_index (path, content)
            VALUES (?, ?)
            """,
            (str(path), content),
        )

        connection.commit()

    except sqlite3.Error as error:
        print(f"Error inserting file: {error}")

    finally:
        connection.close()


def search_code(keyword):
    """
    Search indexed source code for a keyword.
    """

    connection = create_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT path, content
            FROM code_index
            WHERE content LIKE ?
            """,
            (f"%{keyword}%",),
        )

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Error searching database: {error}")
        return []

    finally:
        connection.close()