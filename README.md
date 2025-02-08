# goit-cs-hw-03

## Завдання 1

Створіть базу даних для системи управління завданнями, використовуючи PostgreSQL. База даних має містити таблиці для користувачів, статусів завдань і самих завдань. Виконайте необхідні запити в базі даних системи управління завданнями.

### Покрокова інструкція

1. Створіть таблиці у вашій PostgreSQL базі даних відповідно до вимог. Використовуйте належні типи даних та обмеження.

### Вимоги до структури бази даних:

#### Таблиця **users**:

**id**: Первинний ключ, автоінкремент (тип SERIAL),

**fullname**: Повне ім'я користувача (тип VARCHAR(100)),

**email**: Електронна адреса користувача, яка повинна бути унікальною (тип VARCHAR(100)).

#### Таблиця **status**:

**id**: Первинний ключ, автоінкремент (тип SERIAL),

**name**: Назва статусу (тип VARCHAR(50)), повинна бути унікальною. Пропонуємо наступні типи [('new',), ('in progress',), ('completed',)].

#### Таблиця **tasks**:

**id**: Первинний ключ, автоінкремент (тип SERIAL),

**title**: Назва завдання (тип VARCHAR(100)),

**description**: Опис завдання (тип TEXT),

**status_id**: Зовнішній ключ, що вказує на id у таблиці status (тип INTEGER),

**user_id**: Зовнішній ключ, що вказує на id у таблиці users (тип INTEGER).

2. Переконайтеся, що поля email у таблиці users та name у таблиці status є унікальними.

3. Налаштуйте зв'язки між таблицями таким чином, щоб при видаленні користувача автоматично видалялися всі його завдання (каскадне видалення).

4. Напишіть скрипт створення цих таблиць.

5. Напишіть скрипт seed.py на Python, який буде заповнювати ці таблиці випадковими значеннями. Використовуйте бібліотеку Faker.

6. Використовуючи SQL, виконайте наступні запити в базі даних системи управління завданнями.

### Запити для виконання:

Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.

Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.

Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.

Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.

Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.

Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.

Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.

Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.

Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.

Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.

Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. 

Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').

Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.

Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.

Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.

**Для запуску скрипту у терміналі:**
#### Для створення таблиць
```
python task_1.py
Таблиці успішно створені.
```
#### Для заповнення таблиць випадковими значеннями
```
python task_1_seed.py
База даних успішно заповнена випадковими даними.
```

#### Запити для виконання
```
python task_1_sample.py
Отримати всі завдання певного користувача: [(13, 'Act thought claim.', 'Room live friend test. Professional business office their. Power exactly avoid speech their.\nCourse lawyer nature lot feel. Course less seek by interesting.\nForward how sing rest. Together job mouth.', 3, 1), (15, 'Organization morning news.', None, 1, 1), (21, 'Нове завдання', 'Опис завдання', 1, 1), (22, 'Нове завдання', 'Опис завдання', 1, 1), (23, 'Нове завдання', 'Опис завдання', 1, 1), (24, 'Нове завдання', 'Опис завдання', 1, 1)]

Вибрати завдання за певним статусом: [(4, 'Production couple financial take room.', 'Grow population ahead. Stock reflect dark tough.\nThemselves discussion blood political must our customer. Spring run evening short study.\nWife senior off Mrs worker coach month. Interesting each too.', 1, 2), (5, 'Mission question heart fine.', None, 1, 6), (8, 'Behind after speech.', None, 1, 4), (9, 'Behavior summer the they interview.', 'Less spend artist member minute.\nActivity board open ago rock. Explain happen travel call guess behind. Car former appear floor forward continue send company.', 1, 2), (12, 'Television pressure daughter.', None, 1, 7), (15, 'Organization morning news.', None, 1, 1), (17, 'Heart here.', None, 1, 4), (19, 'Seek stand image.', 'Camera record raise board laugh office event. Structure machine phone goal.\nCandidate my against fact course. Leader across show.\nOil direction list our yet bring. Room space should reach.', 1, 5), (21, 'Нове завдання', 'Опис завдання', 1, 1), (22, 'Нове завдання', 'Опис завдання', 1, 1), (23, 'Нове завдання', 'Опис завдання', 1, 1), (24, 'Нове завдання', 'Опис завдання', 1, 1)]

Отримати список користувачів, які не мають жодного завдання: [(10, 'Ashlee Kelly', 'natalieperez@example.com')]

Отримати всі завдання, які ще не завершено: [(2, 'Her she.', 'Behavior strong stay chair do. Set story value station life sea.\nOperation as perhaps article. Road inside able oil rate water rate. Worker gas skill seek.', 2, 9), (4, 'Production couple financial take room.', 'Grow population ahead. Stock reflect dark tough.\nThemselves discussion blood political must our customer. Spring run evening short study.\nWife senior off Mrs worker coach month. Interesting each too.', 1, 2), (5, 'Mission question heart fine.', None, 1, 6), (6, 'Like direction notice wear.', None, 2, 8), (7, 'Pretty contain message.', 'Management bar subject off. Project single once interview Mrs before so important.\nPer despite leave of middle and include. Become street level. Create build staff rest color.', 2, 3), (8, 'Behind after speech.', None, 1, 4), (9, 'Behavior summer the they interview.', 'Less spend artist member minute.\nActivity board open ago rock. Explain happen travel call guess behind. Car former appear floor forward continue send company.', 1, 2), (12, 'Television pressure daughter.', None, 1, 7), (15, 'Organization morning news.', None, 1, 1), (17, 'Heart here.', None, 1, 4), (19, 'Seek stand image.', 'Camera record raise board laugh office event. Structure machine phone goal.\nCandidate my against fact course. Leader across show.\nOil direction list our yet bring. Room space should reach.', 1, 5), (20, 'Network property ball.', None, 2, 6), (21, 'Нове завдання', 'Опис завдання', 1, 1), (22, 'Нове завдання', 'Опис завдання', 1, 1), (23, 'Нове завдання', 'Опис завдання', 1, 1), (24, 'Нове завдання', 'Опис завдання', 1, 1), (25, 'Нове завдання', 'Опис завдання', 1, 1)]

Знайти користувачів з певною електронною поштою: [(1, "Новий Ім'я", 'fgrant@example.com'), (7, 'Whitney Pierce', 'tsanchez@example.com'), (10, 'Ashlee Kelly', 'natalieperez@example.com')]

Отримати кількість завдань для кожного статусу: [('completed', 7), ('in progress', 4), ('new', 13)]

Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти: []

Отримати список завдань, що не мають опису: [(1, 'Coach concern forget thus.', None, 3, 6), (5, 'Mission question heart fine.', None, 1, 6), (6, 'Like direction notice wear.', None, 2, 8), (8, 'Behind after speech.', None, 1, 4), (10, 'Court sea right send street.', None, 3, 5), (12, 'Television pressure daughter.', None, 1, 7), (15, 'Organization morning news.', None, 1, 1), (16, 'Material popular.', None, 3, 7), (17, 'Heart here.', None, 1, 4), (20, 'Network property ball.', None, 2, 6)]

Вибрати користувачів та їхні завдання, які є у статусі 'in progress': [(9, 'Kyle Olson', 'kdiaz@example.net', 2, 'Her she.', 'Behavior strong stay chair do. Set story value station life sea.\nOperation as perhaps article. Road inside able oil rate water rate. Worker gas skill seek.', 2, 9), (8, 'Hannah Harrell', 'graywilliam@example.net', 6, 'Like direction notice wear.', None, 2, 8), (3, 'Kristina Williams', 'smithjonathan@example.org', 7, 'Pretty contain message.', 'Management bar subject off. Project single once interview Mrs before so important.\nPer despite leave of middle and include. Become street level. Create build staff rest color.', 2, 3), (6, 'Ethan Johnson', 'gregorygomez@example.net', 20, 'Network property ball.', None, 2, 6)]

Отримати користувачів та кількість їхніх завдань: [('Ashlee Kelly', 0), ('Ethan Johnson', 3), ('Hannah Harrell', 1), ('Justin Thompson', 3), ('Kathryn Moses', 2), ('Kristina Williams', 2), ('Kyle Olson', 2), ('Laura Riddle', 2), ('Whitney Pierce', 2), ("Новий Ім'я", 7)]
```

## Завдання 2

Розробіть Python скрипт, який використовує бібліотеку PyMongo для реалізації основних CRUD (Create, Read, Update, Delete) операцій у MongoDB.

### Покрокова інструкція

1. Створіть базу даних відповідно до вимог.

Вимоги до структури документа

Кожен документ у вашій базі даних повинен мати наступну структуру:
```
{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"]
}
```

Документ представляє інформацію про кота, його ім'я name, вік age та характеристики features.

2. Розробіть Python скрипт main.py для виконання наступних завдань.

### Завдання для виконання:

**Читання (Read)**
Реалізуйте функцію для виведення всіх записів із колекції.
Реалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.

**Оновлення (Update)**
Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.
Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.

**Видалення (Delete)**
Реалізуйте функцію для видалення запису з колекції за ім'ям тварини.
Реалізуйте функцію для видалення всіх записів із колекції.

**Для запуску скрипту у терміналі:**
```
python task_2.py
Кіт barsik доданий до бази.
Кіт cat доданий до бази.
Кіт tom доданий до бази.
Всі коти наявні в базі:
{'_id': ObjectId('67a7809c32916786506e5cc9'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('67a7809d32916786506e5cca'), 'name': 'cat', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('67a7809d32916786506e5ccb'), 'name': 'tom', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
Перший знайдений кіт з ім'ям barsik
{'_id': ObjectId('67a7809c32916786506e5cc9'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
Всі знайдені коти з ім'ям barsik
{'_id': ObjectId('67a7809c32916786506e5cc9'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
Вік кота barsik оновлено до 4 років.
До характеристик кота barsik додано: любить рибу.
Всі коти наявні в базі:
{'_id': ObjectId('67a7809c32916786506e5cc9'), 'name': 'barsik', 'age': 4, 'features': ['ходить в капці', 'дає себе гладити', 'рудий', 'любить рибу']}
{'_id': ObjectId('67a7809d32916786506e5cca'), 'name': 'cat', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('67a7809d32916786506e5ccb'), 'name': 'tom', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
Кіт barsik видалений з бази.
Коти barsik не знайдені.
Всі коти наявні в базі:
{'_id': ObjectId('67a7809d32916786506e5cca'), 'name': 'cat', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('67a7809d32916786506e5ccb'), 'name': 'tom', 'age': 5, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
Всі коти видалені з бази.
```

### Перед видаленням всіх котів, база даних виглядає так:
![image info](cats_db.png)