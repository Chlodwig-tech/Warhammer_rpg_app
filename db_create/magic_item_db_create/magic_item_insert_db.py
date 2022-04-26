import pandas
import sqlite3
import os

db=sqlite3.connect('rpg/kivyapp/databases/magic_itemdb.db')
cursor=db.cursor()

categories=pandas.read_csv('db_create/magic_item_db_create/csv/categories.csv',delimiter=';')
for c,chance in zip(categories['category'],categories['chance']):
    cursor.execute(f"""INSERT OR IGNORE INTO categories VALUES
        ('{c}',{chance})
    """)

for filename in next(os.walk('db_create/magic_item_db_create/csv/categories'), (None, None, []))[2]:
    data=pandas.read_csv(f'db_create/magic_item_db_create/csv/categories/{filename}',delimiter=';')
    for c,chance in zip(data[filename.split('.')[0]],data['chance']):
        cursor.execute(f"""INSERT OR IGNORE INTO {filename.split('.')[0]} VALUES
            ('{c}',{chance})
        """)

for filename in next(os.walk('db_create/magic_item_db_create/csv/characteristics'), (None, None, []))[2]:
    data=pandas.read_csv(f'db_create/magic_item_db_create/csv/characteristics/{filename}',delimiter=';')
    for c,chance,description,a in zip(data[filename.split('.')[0]],data['chance'],data['description'],data['additional']):
        if pandas.notna(a):
            with open(a,'r') as f:
                a=f.read()
        else:
            a='null'
        cursor.execute(f"""INSERT OR IGNORE INTO {filename.split('.')[0]}_characteristics VALUES
            ('{c}',{chance},'{description}','{a}')
        """)

for filename in next(os.walk('db_create/magic_item_db_create/csv/other'), (None, None, []))[2]:
    data=pandas.read_csv(f'db_create/magic_item_db_create/csv/other/{filename}',delimiter=';')
    for c,chance,description in zip(data[filename.split('.')[0]],data['chance'],data['description']):
        cursor.execute(f"""INSERT OR IGNORE INTO {filename.split('.')[0]}_characteristics VALUES
            ('{c}',{chance},'{description}')
        """)


db.commit()
db.close()
