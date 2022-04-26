import pandas
import sqlite3
import os

db=sqlite3.connect('rpg/kivyapp/databases/professiondb.db')
cursor=db.cursor()

data=pandas.read_csv('db_create/professions_db_create/csv/professions.csv',delimiter=';')

for _,p,b,ww,us,k,odp,zr,Int,sw,ogd,a,zyw,sz,mag,book in data.itertuples():
    cursor.execute(f"""INSERT OR IGNORE INTO professions_stats VALUES
        ('{p}','{b}',{ww},{us},{k},{odp},{zr},{Int},{sw},{ogd},{a},{zyw},{sz},{mag},'{book}')
    """)

for filename in next(os.walk('db_create/professions_db_create/csv/profession'), (None, None, []))[2]:
    data=pandas.read_csv(f'db_create/professions_db_create/csv/profession/{filename}',delimiter=';')
    for _,s,t,tr,cen,cex in data.itertuples():
        cursor.execute(f"""INSERT OR IGNORE INTO {filename.split('.')[0]} VALUES
            ('{s}','{t}','{tr}','{cen}','{cex}')        
        """)




db.commit()
db.close()
