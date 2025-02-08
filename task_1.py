import sqlite3
from contextlib import contextmanager

database = './test.sqlite'

@contextmanager
def create_connection(db_file):
    # create a database connection to a SQLite database
    conn = sqlite3.connect(db_file)
    yield conn
    conn.commit()
    conn.close()

def create_tables():
    with create_connection(database) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status_id INTEGER,
            user_id INTEGER,
            FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        ''')
        
        # Додавання початкових статусів, якщо вони ще не існують
        cursor.execute('''
        INSERT OR IGNORE INTO status (name) VALUES ('new'), ('in progress'), ('completed')
        ''')
        
        print("Таблиці успішно створені.")

if __name__ == "__main__":
    create_tables()
