import pandas
import sqlite3
import os

os.system('rm rpg/kivyapp/databases/magic_itemdb.db')
db=sqlite3.connect('rpg/kivyapp/databases/magic_itemdb.db')
cursor=db.cursor()

cursor.execute(f"""CREATE TABLE if not exists categories(
    name TEXT,
    value INTEGER UNIQUE
)""")

for filename in next(os.walk('db_create/magic_item_db_create/csv/categories'), (None, None, []))[2]:
    cursor.execute(f"""CREATE TABLE if not exists {filename.split('.')[0]}(
        name TEXT,
        value INTEGER UNIQUE
    )""")

for filename in next(os.walk('db_create/magic_item_db_create/csv/characteristics'), (None, None, []))[2]:
    cursor.execute(f"""CREATE TABLE if not exists {filename.split('.')[0]}_characteristics(
        name TEXT,
        value INTEGER UNIQUE,
        description TEXT,
        additional TEXT
    )""")

for filename in next(os.walk('db_create/magic_item_db_create/csv/other'), (None, None, []))[2]:
    cursor.execute(f"""CREATE TABLE if not exists {filename.split('.')[0]}_characteristics(
        name TEXT,
        value INTEGER UNIQUE,
        description TEXT
    )""")

db.commit()
db.close()
