from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from random import randint

class Screen_(Screen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='roll',size_hint=(0.2,0.1),pos_hint={'right':1,'bottom':1},background_color='red',on_press=self.roll))

    def change_screen(self,screen_name):
        self.manager.current=screen_name

    def update_l(self,b):
        self.l.text=f'{randint(1,int(b.text[1:]))}'

    def roll(self,e):
        b=BoxLayout(orientation='vertical')
        g=GridLayout(rows=1,size_hint=(1,0.5))
        for k in [4,6,10,12,20,100]:
            g.add_widget(Button(text=f'k{k}',on_press=self.update_l))

        self.l=Label(text='roll dice')
        closeButton=Button(text='wyjdź',size_hint=(1,0.3))
        b.add_widget(self.l)
        b.add_widget(g)
        b.add_widget(closeButton)

        popup=Popup(title='roll',content=b)
        popup.open()
        closeButton.bind(on_press=popup.dismiss)