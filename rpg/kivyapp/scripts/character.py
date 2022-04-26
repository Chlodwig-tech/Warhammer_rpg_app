import sqlite3

class Characters:

    def insert(self,column,data):
        db=sqlite3.connect('kivyapp/databases/characterdb.db')
        cursor=db.cursor()
        cursor.execute(f"INSERT OR IGNORE INTO {column} VALUES ({data})")
        name=cursor.fetchone()
        db.commit()
        db.close()