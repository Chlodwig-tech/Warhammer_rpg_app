import sqlite3
import os

os.system('rm rpg/kivyapp/databases/professiondb.db')
db=sqlite3.connect('rpg/kivyapp/databases/professiondb.db')
cursor=db.cursor()

cursor.execute(f"""CREATE TABLE if not exists professions_stats(
    name TEXT UNIQUE,
    type TEXT,
    WW INTEGER,
    US INTEGER,
    K INTEGER,
    Odp INTEGER,
    Zr INTEGER,
    Int INTEGER,
    SW INTEGER,
    Ogd INTEGER,
    A INTEGER,
    Żyw INTEGER,
    Sz INTEGER,
    Mag INTEGER,
    book TEXT
)""")

for filename in next(os.walk('db_create/professions_db_create/csv/profession'), (None, None, []))[2]:
    cursor.execute(f"""CREATE TABLE if not exists {filename.split('.')[0]}(
        skill TEXT,
        talent TEXT,
        trapping TEXT,
        c_entry TEXT,
        c_exit TEXT
    )""")




db.commit()
db.close()
