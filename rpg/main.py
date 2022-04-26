from kivy.app import App

from kivyapp.manager import Manager

class RPGApp(App):

    def build(self):
        return Manager()

if __name__=='__main__':
    RPGApp().run()