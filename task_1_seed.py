import sqlite3
from faker import Faker
import random

# Підключення до бази даних
database = './test.sqlite'
fake = Faker()

def seed_database():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        # Додавання користувачів
        users = []
        for _ in range(10):
            fullname = fake.name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))
            users.append(cursor.lastrowid)
        
        # Отримання статусів
        cursor.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cursor.fetchall()]
        
        # Додавання завдань
        for _ in range(20):
            title = fake.sentence(nb_words=4)
            description = fake.text() if random.choice([True, False]) else None
            status_id = random.choice(status_ids)
            user_id = random.choice(users)
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
                           (title, description, status_id, user_id))
        
        print("База даних успішно заповнена випадковими даними.")

if __name__ == "__main__":
    seed_database()
