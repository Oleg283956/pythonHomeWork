import sqlite3

# Просмотр Users в консоли
prosmort = 0

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


# DB Browser (SQLite) ОЧЕНЬ ДОЛГО ЗАГРУЖАЕТСЯ! Поэтому сделана:
def prosmotr_base():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    print()
    for user in users:
        print(user)


cursor.execute('SELECT COUNT(*) FROM Users')

total1 = cursor.fetchone()[0]

if total1 == 0:
    age = 0
    for i in range(10):
        age += 10
        cursor.execute('INSERT INTO Users (username,email,\
        age,balance) VALUES(?,?,?,?)',(f"User{i+1}",\
        f"example{i+1}@gmail.com", age,'1000'))

if prosmort == 1:
    prosmotr_base()


cursor.execute('SELECT balance FROM Users WHERE username=?',\
               ('User1',))


total3 = cursor.fetchmany(size=cursor.arraysize)
if len(total3) > 0:
    cursor.execute('SELECT balance FROM Users WHERE username=?', \
                   ('User1',))
    total2 = cursor.fetchone()[0]


if len(total3) > 0:
    if total2 == 1000:
        beg = -1
        for i in range(10):
            beg += 2
            cursor.execute('UPDATE Users SET balance=?\
                        WHERE username=?', \
                       (500, f'User{beg}'))

if prosmort == 1:
    prosmotr_base()


cursor.execute('SELECT username FROM Users WHERE username=?',\
               ('User1',))
total3 = cursor.fetchmany(size=cursor.arraysize)

if  len(total3) > 0:
    beg = -2
    for i in range(10):
        beg += 3
        cursor.execute('DELETE FROM Users WHERE username=?',(f'User{beg}',))

if prosmort == 1:
    prosmotr_base()


'''
cursor.execute('SELECT username,email,age,balance\
                FROM Users WHERE age!=?',(60,))
users = cursor.fetchall()
for user in users:
  print(f'Имя: {list(user)[0]}|'f'Почта: {list(user)[1]}|'f'Возраст: {list(user)[2]}|'f'Баланс: {list(user)[3]}')
'''




cursor.execute('SELECT* FROM Users WHERE id=?', \
               (6,))
total3 = cursor.fetchmany(size=cursor.arraysize)
if len(total3) > 0:
    cursor.execute('DELETE FROM Users WHERE id=?',\
               (6,))


if prosmort == 1:
    prosmotr_base()

cursor.execute('SELECT COUNT(*) FROM Users')
# общее количество записей в Users
total_users = cursor.fetchone()[0]
#print('total_users = '+str(total_users))


cursor.execute('SELECT SUM(balance) FROM Users')
#сумма всех балансов
all_balances = cursor.fetchone()[0]
#print('all_balances = '+str(all_balances))


cursor.execute('SELECT AVG(balance) FROM Users')
# средний баланс всех пользователей
total3 = cursor.fetchone()[0]

print(all_balances / total_users)


connection.commit()
connection.close()