import sqlite3

def get_letter_value(letter):
    alfabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    return alfabet.index(letter[0])

def get_all_profesions_names():
    db=sqlite3.connect('kivyapp/databases/professiondb.db')
    cursor=db.cursor()

    cursor.execute(f"SELECT name FROM professions_stats")

    l=[a[0] for a in cursor.fetchall()]
    db.commit()
    db.close()
    l=sorted(l,key=get_letter_value)
    return l

def get_profession(p,name):
    db=sqlite3.connect('kivyapp/databases/professiondb.db')
    cursor=db.cursor()

    cursor.execute(f"SELECT * FROM professions_stats WHERE name='{name}'")
    l=cursor.fetchone()
    p.name=l[0]
    p.type=l[1]
    p.stats['WW']=l[2]
    p.stats['US']=l[3]
    p.stats['K']=l[4]
    p.stats['Odp']=l[5]
    p.stats['Zr']=l[6]
    p.stats['Int']=l[7]
    p.stats['SW']=l[8]
    p.stats['Ogd']=l[9]
    p.stats['A']=l[10]
    p.stats['Żyw']=l[11]
    p.stats['Sz']=l[12]
    p.stats['Mag']=l[13]
    p.book=l[14]

    cursor.execute(f"SELECT * FROM '{name.replace(' ','_').lower()}'")
    for row in cursor.fetchall():
        if row[0]!='nan':
            p.skills.append(row[0])
        if row[1]!='nan':
            p.talents.append(row[1])
        if row[2]!='nan':
            p.trappings.append(row[2])
        if row[3]!='nan':
            p.c_entries.append(row[3])
        if row[4]!='nan':
            p.c_exits.append(row[4])

    db.commit()
    db.close()