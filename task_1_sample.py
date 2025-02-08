import sqlite3

database = './test.sqlite'

def get_tasks_by_user(user_id):
    # Отримати всі завдання певного користувача
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

def get_tasks_by_status(status_name):
    # Вибрати завдання за певним статусом
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?)", (status_name,))
        return cursor.fetchall()

def update_task_status(task_id, new_status):
    # Оновити статус конкретного завдання
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = ?) WHERE id = ?", (new_status, task_id))
        conn.commit()

def get_users_without_tasks():
    # Отримати список користувачів, які не мають жодного завдання
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
        return cursor.fetchall()

def add_new_task(title, description, status_name, user_id):
    # Додати нове завдання для конкретного користувача
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, (SELECT id FROM status WHERE name = ?), ?)", (title, description, status_name, user_id))
        conn.commit()

def get_unfinished_tasks():
    # Отримати всі завдання, які ще не завершено
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')")
        return cursor.fetchall()

def delete_task(task_id):
    # Видалити конкретне завдання
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def find_users_by_email(email_pattern):
    # Знайти користувачів з певною електронною поштою
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email LIKE ?", (email_pattern,))
        return cursor.fetchall()

def update_user_name(user_id, new_name):
    # Оновити ім'я користувача
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET fullname = ? WHERE id = ?", (new_name, user_id))
        conn.commit()

def count_tasks_by_status():
    # Отримати кількість завдань для кожного статусу
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT status.name, COUNT(tasks.id) FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name")
        return cursor.fetchall()

def get_tasks_by_email_domain(domain):
    # Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE ?", (f'%{domain}',))
        return cursor.fetchall()

def get_tasks_without_description():
    # Отримати список завдань, що не мають опису
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE description IS NULL")
        return cursor.fetchall()

def get_users_with_in_progress_tasks():
    # Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT users.*, tasks.* FROM users JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress')")
        return cursor.fetchall()

def get_users_with_task_count():
    # Отримати користувачів та кількість їхніх завдань
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname")
        return cursor.fetchall()

# Приклад використання
if __name__ == "__main__":
    print("Отримати всі завдання певного користувача:", get_tasks_by_user(1))
    print("\nВибрати завдання за певним статусом:", get_tasks_by_status('new'))
    update_task_status(2, 'in progress')
    print("\nОтримати список користувачів, які не мають жодного завдання:", get_users_without_tasks())
    add_new_task("Нове завдання", "Опис завдання", "new", 1)
    print("\nОтримати всі завдання, які ще не завершено:", get_unfinished_tasks())
    delete_task(3)
    print("\nЗнайти користувачів з певною електронною поштою:", find_users_by_email('%@example.com'))
    update_user_name(1, "Новий Ім'я")
    print("\nОтримати кількість завдань для кожного статусу:", count_tasks_by_status())
    print("\nОтримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:", get_tasks_by_email_domain('gmail.com'))
    print("\nОтримати список завдань, що не мають опису:", get_tasks_without_description())
    print("\nВибрати користувачів та їхні завдання, які є у статусі 'in progress':", get_users_with_in_progress_tasks())
    print("\nОтримати користувачів та кількість їхніх завдань:", get_users_with_task_count())
