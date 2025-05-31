import sqlite3

def connect_db():
    return sqlite3.connect(":memory:")

def create_table(conn):
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()

def create_user(conn, username, email):
    conn.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    conn.commit()

def get_user(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cur.fetchone()

def update_user_email(conn, username, new_email):
    conn.execute("UPDATE users SET email = ? WHERE username = ?", (new_email, username))
    conn.commit()

def delete_user(conn, username):
    conn.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
