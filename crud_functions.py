import sqlite3

def initiate_db():
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS Prod')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Prod
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 price INTEGER NOT NULL)
                 ''')

    cursor.execute('DROP TABLE IF EXISTS Users')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                     (id INTEGER PRIMARY KEY,
                     username TEXT NOT NULL,
                     email TEXT NOT NULL,
                     age INTEGER NOT NULL,
                     balance INTEGER NOT NULL)''')

    products = [
        {"name": "Яблоки", "description": "Яблоко как яблоко", "price": 100, },
        {"name": "Груши", "description": "Груша как груша", "price": 200},
        {"name": "Апельсины", "description": "Апельсин как апельсин", "price": 300},
        {"name": "Бананы", "description": "Банан как банан", "price": 400}]

    for product in products:
        cursor.execute('INSERT INTO Prod (title, description, price)VALUES(?, ?, ?)',
                       (f"{product['name']}",f"{product['description']}", f"{product['price']}"))

    connection.commit()
    connection.close()

def add_user(username ,email ,age):
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()

    # Баланс по умолчанию 1000
    balance = 1000
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()
    info = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if info.fetchone() is None:
        result = None
    else:
        result = not None
    return result

def get_all_products():
    connection = sqlite3.connect('Prod.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Prod")
    products = cursor.fetchall()
    connection.close()
    return products