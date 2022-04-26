import sqlite3
import os

os.system('rm rpg/kivyapp/databases/characterdb.db')
db=sqlite3.connect('rpg/kivyapp/databases/characterdb.db')
cursor=db.cursor()

cursor.execute(f"""CREATE TABLE if not exists character(
    name TEXT UNIQUE,
    race TEXT,
    current_profession TEXT,    
    age INTEGER
)""")

cursor.execute(f"""CREATE TABLE if not exists character_skills(
    name TEXT,
    skill_name TEXT,
    level INTEGER,
    bonuses INTEGER,
    type TEXT
)""")

cursor.execute(f"""CREATE TABLE if not exists character_talents(
    name TEXT,
    talent_name TEXT,
    description TEXT,
    bonuses TEXT
)""")

cursor.execute(f"""CREATE TABLE if not exists character_weapons(
    name TEXT,
    weapon_name TEXT,
    description TEXT
)""")

cursor.execute(f"""CREATE TABLE if not exists character_armor(
    name TEXT,
    armor_name TEXT,
    description TEXT
)""")

db.commit()
db.close()
