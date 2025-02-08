from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb+srv://goit_oza:<password>@cluster0.cq44m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["cats_db"]  # Назва бази даних
collection = db["cats"]  # Колекція для збереження документів

# Функція для створення запису
def create_cat(name, age, features):
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)
    print(f"Кіт {name} доданий до бази.")

# Функція для читання всіх записів
def read_all_cats():
    cats = collection.find()
    print("Всі коти наявні в базі:")
    for cat in cats:
        print(cat)

# Функція для пошуку першого кота за ім'ям
def find_cat_by_name(name):
    cat = collection.find_one({"name": name})
    print("Перший знайдений кіт з ім'ям", name)
    if cat:
        print(cat)
    else:
        print(f"Кіт {name} не знайдений.")

# Функція для пошуку всіх котів за ім'ям
def find_cats_by_name(name):
    cats = collection.find({"name": name})
    if cats:
        print("Всі знайдені коти з ім'ям", name)
    found = False
    for cat in cats:
        print(cat)
        found = True
    if not found:
        print(f"Коти {name} не знайдені.")

# Функція для оновлення віку для першого кота за ім'ям
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count:
        print(f"Вік кота {name} оновлено до {new_age} років.")
    else:
        print("Кіт не знайдений.")

# Функція для додавання нової характеристики до списку features
def add_feature(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count:
        print(f"До характеристик кота {name} додано: {new_feature}.")
    else:
        print(f"Кіт {name} не знайдений.")

# Функція для видалення першого запису за ім'ям
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"Кіт {name} видалений з бази.")
    else:
        print(f"Кіт {name} не знайдений.")

# Функція для видалення всіх записів за ім'ям
def delete_cats_by_name(name):
    result = collection.delete_many({"name": name})
    if result.deleted_count:
        print(f"Всі коти з ім'ям {name} видалені з бази.")
    else:
        print(f"Коти {name} не знайдені.")

# Функція для видалення всіх записів
def delete_all_cats():
    collection.delete_many({})
    print("Всі коти видалені з бази.")

# Приклад використання
if __name__ == "__main__":
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("cat", 5, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("tom", 5, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    find_cat_by_name("barsik")
    find_cats_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature("barsik", "любить рибу")
    read_all_cats()
    delete_cat_by_name("barsik")
    delete_cats_by_name("barsik")
    read_all_cats()
    delete_all_cats()
