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
users = [
    ("ravi", "pass"),
    ("teja", "pusha"),
    ("prasanth", "punitha"),
    ("kumar", "devakanai"),
    ("koki kumar", "kaviya"),
    ("lakshmi", "majapasanga"),
    ("sofiya", "U$trong_password"),
    ("santhi", "ramya"),
    ("latha", "panimalar"),
    ("sharan", "patti")
]
cursor.executemany("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", users)
connection.commit()
cursor.execute("SELECT username, password FROM users")
for row in cursor.fetchall():
    print(f"Username: {row[0]}, Password: {row[1]}")

connection.close()