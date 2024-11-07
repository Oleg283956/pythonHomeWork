import sqlite3
connection = sqlite3.connect('bot_db.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEDER NOT NULL
    );
    ''')
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('bot_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT* FROM Users WHERE username=?',(f'{username}',))
    total3 = cursor.fetchmany(size=cursor.arraysize)
    res = False
    if len(total3) > 0:
        res = True
    return res


def add_user(username, email, age):
    connection = sqlite3.connect('bot_db.db')
    cursor = connection.cursor()
    bal = 1000
    cursor.execute('INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)',(f'{username}',f'{email}',f'{age}',f'{bal}'))
    connection.commit()
    connection.close()





def initiate_db_prod():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    connection.commit()


def get_all_users():
    connection = sqlite3.connect('bot_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    userss = cursor.fetchall()
    l_all = []
    for user in userss:
        l_all.append(list(user))
    print(l_all)
    return l_all
    connection.commit()
    connection.close()

def dell_all_users():
    connection = sqlite3.connect('bot_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT* FROM Users')
    userss = cursor.fetchall()
    l_all = []
    for user in userss:
        cursor.execute('DELETE FROM Users')
    connection.commit()
    connection.close()

#dell_all_users()
#get_all_users()


def get_all_products():
    connection = sqlite3.connect('bot_db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    l_all = []
    for product in products:
        l_all.append(list(product))
    return l_all
    connection.commit()
    connection.close()



initiate_db()

cursor.execute('SELECT COUNT(*) FROM Products')
total_products = cursor.fetchone()[0]

if total_products == 0:
    cursor.execute('INSERT INTO Products (title,description,\
    price) VALUES(?,?,?)',('Продукт1',\
    "Снижение риска развития гиповитаминозов и недостатка минеральных веществ, а также в период выздоровления после различных заболеваний, травм, операций и в период всплесков сезонных заболеваний.",'100'))
    cursor.execute('INSERT INTO Products (title,description,\
    price) VALUES(?,?,?)',('Продукт2',\
    "Биоактивные соединения, входящие в состав комплекса «Черника Форте», помогут защитить зрение в условиях повышенной зрительной нагрузки, а также поддержать нормальное состояние глаз.",'200'))
    cursor.execute('INSERT INTO Products (title,description,\
    price) VALUES(?,?,?)',('Продукт3',\
   "Биологически активная добавка «Компливит®» — витаминно - минеральный комплекс, созданный с учетом пищевой физиологическо потребности населения РФ, способствует восполнению дефицит важнейших витаминов и минералов.",'300'))
    cursor.execute('INSERT INTO Products (title,description,\
    price) VALUES(?,?,?)',('Продукт4',\
    "БАД КОМПЛИВИТ® СИЯНИЕ представляет собой комплекс витаминов, минералов, витаминоподобных веществ и экстракта зеленого чая. Использование комплекса помогает улучшить состояние кожи, ногтей и волос, особенно в условиях неблагоприятной городской экологии. Действие комплекса обусловлено свойствами входящих в его состав компонентов.",'400'))
    connection.commit()


connection.commit()
connection.close()