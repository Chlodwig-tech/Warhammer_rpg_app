import sqlite3
from random import randint

dictionary={'Broń biała':'melee_weapon','Broń zasięgowa':'range_weapon','Pancerz / Ubranie':'armor_or_clothing','Biżuteria':'jewelry','Inne':'other'}
dictionary2={'Tajemna księga':'secret_book','Klejnot mocy':'mighty_jewel','Różdżka':'wand','Mikstura':'potion','Magiczne buty':'magic_boots','Magiczna peleryna / płaszcz':'magic_clape','Magiczna lina':'magic_line','Magiczne lustro':'magic_mirror'}

class MagicItem:

    def __init__(self):
        self.category=None
        self.kind=None
        self.characteristics=None
        self.characteristics_description=None
        self.additional_stats=None

    def __str__(self):
        s=''

        if self.category:
            s+='['+str(self.category)+'] '
        
        if self.kind:
            s+=str(self.kind)+' - '

        if self.characteristics:
            s+=str(self.characteristics)+' ('
        
        if self.characteristics_description:
            s+=str(self.characteristics_description)+')'

        if self.additional_stats:
            s+='\nadditional info:\n'+str(self.additional_stats)

        if s=='':
            return 'no item'
        return s

def get_magic_item_by_category(kind):
    db=sqlite3.connect('kivyapp/databases/magic_itemdb.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT name,MIN(value) FROM {kind} WHERE value>={randint(1,100)}")
    name=cursor.fetchone()
    db.commit()
    db.close()
    return name[0]

def get_characteristics(kind,m):
    db=sqlite3.connect('kivyapp/databases/magic_itemdb.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT name,MIN(value),description,additional FROM {kind}_characteristics WHERE value>={randint(1,100)}")
    ch=cursor.fetchone()
    m.characteristics=ch[0]
    m.characteristics_description=ch[2]
    if ch[3]!='null':
        m.additional_stats=ch[3]
    db.commit()
    db.close()

def get_other_characteristics(kind,m):
    db=sqlite3.connect('kivyapp/databases/magic_itemdb.db')
    cursor=db.cursor()
    cursor.execute(f"SELECT name,MIN(value),description FROM {kind}_characteristics WHERE value>={randint(1,100)}")
    ch=cursor.fetchone()
    m.characteristics=ch[0]
    m.characteristics_description=ch[2]

    db.commit()
    db.close()

def get_random_magic_item():
    m=MagicItem()
    m.category=get_magic_item_by_category('categories')
    m.kind=get_magic_item_by_category(dictionary[m.category])

    if dictionary[m.category]=='melee_weapon' or dictionary[m.category]=='range_weapon':
        get_characteristics('weapon',m)
    elif dictionary[m.category]=='other':
        get_other_characteristics(dictionary2[m.kind],m)
    else:
        get_characteristics(dictionary[m.category],m)

    return m

if __name__=='__main__':
    m=get_random_magic_item()
    print(m)