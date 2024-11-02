import sqlite3

sozd = 1
updat = 1
delet = 1

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

if sozd == 0:
    age = 0
    for i in range(10):
        age += 10
        cursor.execute('INSERT INTO Users (username,email,\
        age,balance) VALUES(?,?,?,?)',(f"User{i+1}",\
        f"example{i+1}@gmail.com", age,'1000'))
    sozd = 1

if updat == 0:
    beg = -1
    for i in range(10):
        beg += 2
        cursor.execute('UPDATE Users SET balance=?\
                        WHERE username=?', \
                       (500, f'User{beg}'))
    updat = 1

if delet == 0:
    beg = -2
    for i in range(10):
        beg += 3
        cursor.execute('DELETE FROM Users WHERE username=?',(f'User{beg}',))
    delet = 1

cursor.execute('SELECT username,email,age,balance\
                FROM Users WHERE age!=?',(60,))
users = cursor.fetchall()
for user in users:
  print(f'Имя: {list(user)[0]}|'f'Почта: {list(user)[1]}|'f'Возраст: {list(user)[2]}|'f'Баланс: {list(user)[3]}')

connection.commit()
connection.close()