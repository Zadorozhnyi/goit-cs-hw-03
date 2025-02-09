import psycopg2
from contextlib import contextmanager

# Параметри підключення до бази даних PostgreSQL
# Логічно що для цього треба заводити окрему функціональність!
# і спільно використовувати create_connection і параметри
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "aMLrG1AJIxIPJ1ON"
DB_HOST = "localhost"
DB_PORT = "5432"

@contextmanager
def create_connection():
    # create a database connection to a PostgreSQL database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    yield conn
    conn.commit()
    conn.close()

def create_tables():
    with create_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER,
            user_id INTEGER,
            FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        ''')
        
        # Додавання початкових статусів, якщо вони ще не існують
        cursor.execute('''
        INSERT INTO status (name) VALUES ('new') ON CONFLICT (name) DO NOTHING;
        INSERT INTO status (name) VALUES ('in progress') ON CONFLICT (name) DO NOTHING;
        INSERT INTO status (name) VALUES ('completed') ON CONFLICT (name) DO NOTHING;
        ''')
        
        print("Таблиці успішно створені.")

if __name__ == "__main__":
    create_tables()
