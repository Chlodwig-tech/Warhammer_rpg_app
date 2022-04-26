from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivyapp.screen_ import Screen_
from kivyapp.scripts.magic_item_generator import get_random_magic_item

class MagicItem:

    def __init__(self):
        self.clear()

    def clear(self):
        self.category=None
        self.kind=None
        self.characteristics=None
        self.characteristics_description=None
        self.additional_stats=None

class Generate_magic_item(Screen_):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.m=MagicItem()
        self.start_buttons()

    def clear(self):
        self.m.clear()
        
    def start_buttons(self):
        self.ids.buttons.add_widget(Button(text='Losowy przedmiot',on_press=lambda *args: self.random_item(*args[1:])))
        l=['Broń biała','Broń zasięgowa','Pancerz / Ubranie','Biżuteria','Inne']
        self.ids.buttons.add_widget(Button(text='Broń biała',on_press=lambda *args: self.random_item('Broń biała',*args[1:])))
        self.ids.buttons.add_widget(Button(text='Broń zasięgowa',on_press=lambda *args: self.random_item('Broń zasięgowa',*args[1:])))
        self.ids.buttons.add_widget(Button(text='Pancerz / Ubranie',on_press=lambda *args: self.random_item('Pancerz / Ubranie',*args[1:])))
        self.ids.buttons.add_widget(Button(text='Biżuteria',on_press=lambda *args: self.random_item('Biżuteria',*args[1:])))
        self.ids.buttons.add_widget(Button(text='Inne',on_press=lambda *args: self.random_item('Inne',*args[1:])))
        self.ids.buttons.add_widget(Button(text='Menu',on_press=lambda *args: self.change_screen('welcome',*args[1:])))

    def random_item(self,category=None):
        self.clear()

        if category is not None:
            self.m.category=category

        get_random_magic_item(self.m)


        self.ids.l1.text=f'{self.m.kind} [{self.m.category}]'
        self.ids.l2.text=f'{self.m.characteristics}'
        self.ids.t1.text=f'{self.m.characteristics_description}'

        if self.m.additional_stats:  
            self.ids.t1.text+=f'\n\nDodatkowe informacje:\n{self.m.additional_stats}'