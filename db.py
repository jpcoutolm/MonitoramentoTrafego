import sqlite3
import os

os.makedirs('database', exist_ok=True)
conn = sqlite3.connect('database/devices.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        name TEXT NOT NULL,
        traffic REAL NOT NULL
    )
''')
conn.commit()
conn.close()