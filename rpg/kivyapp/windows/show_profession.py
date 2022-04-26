from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from kivyapp.screen_ import Screen_
from kivyapp.scripts.profession import get_profession,get_all_profesions_names

class Profesion:

    def __init__(self):
        self.name='name'
        self.type='podstawowa'
        self.stats={}
        self.skills=[]
        self.talents=[]
        self.trappings=[]
        self.c_entries=[]
        self.c_exits=[]
        self.book='podstawowy'

class Show_profession(Screen_):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.stats={}
        self.dropdown=DropDown()
        for name in get_all_profesions_names():
            btn=Button(text=f'{name}',size_hint_y=None,height=100)
            btn.bind(on_release=lambda *args:self.change_profession(*args))
            self.dropdown.add_widget(btn)

        mainbutton = Button(text ='Profesja')
        mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))

        self.ids.profession.add_widget(mainbutton)
        self.ids.c_entries.on_ref_press=self.cp
        self.ids.c_exits.on_ref_press=self.cp

        for l in ('WW','US','K','Odp','Zr','Int','SW','Ogd'):
            self.stats[l]=Label(text=f'{l}\n-',color='black')
            self.ids.stats1.add_widget(self.stats[l])
        for l in ('A','Żyw','S','Wt','Sz','Mag','PO','PP'):
            self.stats[l]=Label(text=f'{l}\n-',color='black')
            self.ids.stats2.add_widget(self.stats[l])

    def change_profession(self,*args,name=None):
        p=Profesion()
        if name is None:
            self.dropdown.select(args[0].text)
            get_profession(p,args[0].text)
        else:
            self.dropdown.select(name)
            get_profession(p,name)
        for key in p.stats:
            self.stats[key].text=f'{key}\n{"+"+str(p.stats[key]) if p.stats[key]>0 else "-"}'

        print(p.book)
        print(p.type)

        skills='Umiejętności: '
        for skill in p.skills:
            skills+=f'{skill}, '
        
        talents='Zdolności: '
        for talent in p.talents:
            talents+=talent+', '

        trappings='Wyposażenie: '
        for trapping in p.trappings:
            trappings+=trapping+', '

        c_entries='Profesje wejściowe: '
        if not p.c_entries:
            c_entries+='brakxd'
        for c_entry in p.c_entries:
            c_entries+=f'[ref={c_entry}]{c_entry}[/ref], '

        c_exits='Profesje wyjściowe: '
        for c_exit in p.c_exits:
            c_exits+=f'[ref={c_exit}]{c_exit}[/ref], '

        self.ids.version.text=f'profesja {p.type}  -  {p.book}'
        self.ids.skills.text=skills[:-2]
        self.ids.talents.text=talents[:-2]
        self.ids.trappings.text=trappings[:-2]
        self.ids.c_entries.text=c_entries[:-2]
        self.ids.c_exits.text=c_exits[:-2]

    def cp(self,x,arg):
        print(arg,x)
        self.change_profession(arg,name=arg)