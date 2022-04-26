from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label

from kivyapp.scripts.character import Characters

class Character_card(TabbedPanel):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Builder.load_file('kivyapp/kv/character_card.kv')
        self.stats={}

    def load_character(self):
        pass
    def start_function(self):
        for l in ('WW','US','K','Odp','Zr','Int','SW','Ogd'):
            pass
