import sqlite3
connection = sqlite3.connect(r"external use:\ ravi.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")
users = []
cursor.executemany("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", users)
connection.commit()
connection.close()