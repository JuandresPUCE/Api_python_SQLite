import sqlite3 as sql
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def createDB():
    conn = sql.connect(DB_PATH)
    print("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS guitars (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, maker TEXT, Type TEXT, price REAL, img TEXT)')
    print("Table created successfully")
    conn.commit()
    conn.close()
    

#

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def addGuitars():
    conn = sql.connect(DB_PATH)
    cur = conn.cursor()

    with open(os.path.join(os.path.dirname(__file__), 'guitars.json')) as file:
        guitars = json.load(file)

    for guitar in guitars:
        cur.execute("INSERT INTO guitars (name, maker, Type, price, img) VALUES (?, ?, ?, ?, ?)",
                    (guitar['name'], guitar['maker'], guitar['Type'], guitar['price'], guitar['img']))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    createDB()
    addGuitars()
    print("Database")
    