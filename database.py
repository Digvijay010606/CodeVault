import sqlite3
from config import database_path

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(database_path())
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS index (
                    path TEXT PRIMARY KEY,
                    tokenized content TEXT,
                    line_no INTEGER
                    )
                    ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

def insert_data(path, tokenized_content, line_no):
    create_table()
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO index (path, tokenized content, line_no)
                VALUES (?, ?, ?)
            ''', (path, tokenized_content, line_no))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

def fetch_data(target_word):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT path, tokenized content, line_no
                FROM index
                WHERE tokenized content LIKE ?
            ''', (f'%{target_word}%',))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
    return []


