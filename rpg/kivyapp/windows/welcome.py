from kivyapp.screen_ import Screen_
from kivyapp.scripts.character_card import Character_card
from kivy.uix.pagelayout import PageLayout

class Welcome(Screen_):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.pagelayout.page=2
        self.ids.pagelayout.on_touch_down=self.start
        self.ids.pagelayout.on_touch_up=self.stop
        self.start_x=0
        self.start_y=0
        self.number_of_pages=3
        self.ids.charac_card.start_function()

    def start(self,t):
        self.start_x=t.pos[0]
        self.start_y=t.pos[1]


    def stop(self,t):
        if abs(self.start_y-t.pos[1])<200:
            if self.start_x>t.pos[0] and self.ids.pagelayout.page+1<self.number_of_pages:
                self.ids.pagelayout.page+=1
            elif self.start_x<t.pos[0] and self.ids.pagelayout.page>0:
                self.ids.pagelayout.page-=1
            else:
                super(PageLayout,self.ids.pagelayout).on_touch_up(t)
                super(PageLayout,self.ids.pagelayout).on_touch_down(t)
        else:
            super(PageLayout,self.ids.pagelayout).on_touch_up(t)
            super(PageLayout,self.ids.pagelayout).on_touch_down(t)