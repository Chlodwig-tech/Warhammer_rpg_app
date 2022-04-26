from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from os import walk

from kivyapp.screen_windows import *

class Manager(ScreenManager):
    
    def __init__(self):
        super().__init__()
        for filename in next(walk('kivyapp/kv/'),(None,None,[]))[2]:
            Builder.load_file(f'kivyapp/kv/{filename}')
            self.add(filename.split('.kv')[0])

        self.current='welcome'

    def add(self,name):
        if name=='welcome':
            self.add_widget(Welcome(name='welcome'))
        elif name=='generate_magic_item':
            self.add_widget(Generate_magic_item(name='generate_magic_item'))
        elif name=='show_profession':
            self.add_widget(Show_profession(name='show_profession'))