import psycopg2
from faker import Faker
import random

# Параметри підключення до бази даних PostgreSQL
# Логічно що для цього треба заводити окрему функціональність!
# і спільно використовувати create_connection і параметри
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "aMLrG1AJIxIPJ1ON"
DB_HOST = "localhost"
DB_PORT = "5432"

fake = Faker()

def create_connection():
    # Створення підключення до PostgreSQL
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def seed_database():
    # Заповнення таблиць випадковими значеннями
    conn = create_connection()
    cursor = conn.cursor()
    
    # Додавання користувачів
    user_ids = []
    for _ in range(10):
        fullname = fake.name()
        email = fake.unique.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id", (fullname, email))
        user_ids.append(cursor.fetchone()[0])
    
    # Отримання статусів
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]
    
    # Додавання завдань
    for _ in range(20):
        title = fake.sentence(nb_words=4)
        description = fake.text() if random.choice([True, False]) else None
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            (title, description, status_id, user_id)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("База даних успішно заповнена випадковими даними.")

if __name__ == "__main__":
    seed_database()
