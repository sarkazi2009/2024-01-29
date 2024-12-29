import sqlite3

# Создание базы данных и подключение к ней
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создание таблицы, если её ещё нет
create_table_query = """
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
"""

cursor.execute(create_table_query)

conn.commit()
insert_data_query = """
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
"""

data_list = [
     ("User1", "example1@gmail.com", 10, 1000),
     ("User2", "example2@gmail.com", 20, 1000),
     ("User3", "example3@gmail.com", 30, 1000),
     ("User4", "example4@gmail.com", 40, 1000),
     ("User5", "example5@gmail.com", 50, 1000),
     ("User6", "example6@gmail.com", 60, 1000),
     ("User7", "example7@gmail.com", 70, 1000),
     ("User8", "example8@gmail.com", 80, 1000),
     ("User9", "example9@gmail.com", 90, 1000),
     ("User10", "example10@gmail.com", 100, 1000)
 ]

cursor.executemany(insert_data_query, data_list)

conn.commit()
update_balance_query = """
UPDATE Users
SET balance = 500
WHERE id IN (SELECT id FROM Users WHERE id % 2 = 1)
"""

cursor.execute(update_balance_query)

conn.commit()
delete_record_query = """
DELETE FROM Users
WHERE id IN (SELECT id FROM Users WHERE id % 3 = 0)
"""

cursor.execute(delete_record_query)

conn.commit()


cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(user)
