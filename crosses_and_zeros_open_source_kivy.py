from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import webbrowser
import random
from kivy.config import Config
Config.set('graphics','resizable','0')
players_turn = 0
x_counter = 0
y_counter = 0
seaside_val = 0
lagoon_val = 0
coins = x_counter*2+y_counter*2
Builder.load_file('github.kv')
user_val = 2
class GitBut(Widget):
    def get_link(self):
        webbrowser.open_new("https://github.com/MaximFedarau/My-projects-in-school")
Builder.load_file('close.kv')
class MyLayout(Widget):
    def hello_on(self):
        global coins,seaside_val
        if seaside_val==0:
            self.seaside_bought_lbl = Label(text="Unsold.", color=[1, 0, 0, 1], font_size=30)
        else:
            self.seaside_bought_lbl = Label(text="Sold.", color=[0,1,0,1], font_size=30)
        if lagoon_val == 0:
            self.lagoon_bought_lbl = Label(text="Unsold.", color=[1, 0, 0, 1], font_size=30)
        else:
            self.lagoon_bought_lbl = Label(text="Sold.", color=[0,1,0,1], font_size=30)
        theme_gl = GridLayout(cols=4,rows=5,spacing=10)
        theme_popup = Popup(title="Themes.",size_hint=[.8,.8],content=theme_gl,background = 'atlas://data/images/defaulttheme/tab_btn_disabled')
        self.coins_lbl = Label(text="Coins = "+str(coins),font_size=37,color=[1,1,0,1])
        theme_gl.add_widget(Widget())
        theme_gl.add_widget(Widget())
        theme_gl.add_widget(Widget())
        theme_gl.add_widget(self.coins_lbl)
        self.classic_lbl = Label(text="Classic",font_size=30)
        self.classic_cost_lbl = Label(text=str(0),color=[1,1,0,1],font_size=50)
        self.classic_btn = Button(text="Use it.",background_color=[0,0,0,0],font_size=30,on_press=self.classic_theme)
        self.classic_bought_lbl = Label(text="Sold.",color=[0,1,0,1],font_size=30)
        theme_gl.add_widget(self.classic_lbl)
        theme_gl.add_widget(self.classic_cost_lbl)
        theme_gl.add_widget(self.classic_btn)
        theme_gl.add_widget(self.classic_bought_lbl)
        self.seaside_lbl = Label(text="Seaside",font_size=30)
        self.seaside_cost_lbl = Label(text=str(20),color=[1,1,0,1],font_size=50)
        self.seaside_btn=Button(text="Use it.",background_color=[0,0,0,0],font_size=30,on_press=self.seaside_theme)
        theme_gl.add_widget(self.seaside_lbl)
        theme_gl.add_widget(self.seaside_cost_lbl)
        theme_gl.add_widget(self.seaside_btn)
        theme_gl.add_widget(self.seaside_bought_lbl)
        self.lagoon_lbl = Label(text="Lagoon", font_size=30)
        self.lagoon_cost_lbl = Label(text=str(50), color=[1, 1, 0, 1], font_size=50)
        self.lagoon_btn = Button(text="Use it.", background_color=[0, 0, 0, 0], font_size=30,
                                  on_press=self.lagoon_theme)
        theme_gl.add_widget(self.lagoon_lbl)
        theme_gl.add_widget(self.lagoon_cost_lbl)
        theme_gl.add_widget(self.lagoon_btn)
        theme_gl.add_widget(self.lagoon_bought_lbl)
        theme_popup.open()
    def classic_theme(self,instance):
        global coins
        cost = int(self.classic_cost_lbl.text)
        status = self.classic_bought_lbl.text
        if status=="Unsold.":
            if coins>=cost:
                coins-=cost
                self.coins_lbl.text="Coins = "+str(coins)
                self.classic_bought_lbl.text="Sold."
                self.classic_bought_lbl.color=[0,1,0,1]
                Window.clearcolor = (0,0,0,0)
        if status=="Sold.":
            Window.clearcolor = (0,0,0,0)
    def seaside_theme(self,instance):
        global coins,seaside_val
        cost = int(self.seaside_cost_lbl.text)
        if self.seaside_bought_lbl.text == "Unsold.":
            if coins >= cost:
                coins -= cost
                seaside_val=1
                self.coins_lbl.text = "Coins = " + str(coins)
                self.seaside_bought_lbl.text = "Sold."
                self.seaside_bought_lbl.color = [0,1,0,1]
                Window.clearcolor = (1, .87, .68, 1)
        if self.seaside_bought_lbl.text == "Sold.":
            Window.clearcolor = (1, .87, .68, 1)
    def lagoon_theme(self,instance):
        global coins, lagoon_val
        cost = int(self.lagoon_cost_lbl.text)
        if self.lagoon_bought_lbl.text == "Unsold.":
            if coins >= cost:
                coins -= cost
                lagoon_val = 1
                self.coins_lbl.text = "Coins = " + str(coins)
                self.lagoon_bought_lbl.text = "Sold."
                self.lagoon_bought_lbl.color = [0, 1, 0, 1]
                Window.clearcolor = (.11, .56, 1, 1)
        if self.lagoon_bought_lbl.text == "Sold.":
            Window.clearcolor = (.11, .56, 1, 1)
def check_state(list):
    lst1 = list[0]
    lst2 = list[1]
    lst3 = list[2]
    lst4 = [lst1[0],lst2[0],lst3[0]]
    lst5 =  [lst1[1],lst2[1],lst3[1]]
    lst6 =  [lst1[2],lst2[2],lst3[2]]
    lst7 = [lst1[0],lst2[1],lst3[2]]
    lst8 = [lst3[0],lst2[1],lst1[2]]
    if lst1==["X","X","X"] or lst2==["X","X","X"] or lst3==["X","X","X"] or lst4==["X","X","X"] or lst5==["X","X","X"] or  lst6==["X","X","X"]  or lst7==["X","X","X"] or lst8==["X","X","X"]:
        return "X"
    elif lst1==["O","O","O"] or lst2==["O","O","O"] or lst3==["O","O","O"] or lst4==["O","O","O"] or lst5==["O","O","O"] or  lst6==["O","O","O"]  or lst7==["O","O","O"] or lst8==["O","O","O"]:
        return "O"
    else:
        return "Draw"
class GameApp(App, BoxLayout):
    def build(self):
        self.icon = "close.png"
        menu_bl = BoxLayout()
        user_bl = BoxLayout(spacing=15)
        al = AnchorLayout(anchor_x = "center",anchor_y = "center")
        gl  = GridLayout(cols=3,rows=5,padding=[50],spacing=15)
        self.b1 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b2 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b3 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b4 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b5 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b6 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b7 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b8 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b9 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.menu_b = Button(text="Themes.",font_size=25,size_hint=[.1,.1])
        menu_bl.add_widget(MyLayout())
        menu_bl.add_widget(GitBut())
        user_bl.add_widget(Button(text="1 user.",background_color = [0,0,1,1],font_size=25,on_press=self.downgrade_val))
        user_bl.add_widget(Button(text="2 users.",background_color = [0,0,1,1],font_size=25,on_press=self.increase_val))
        self.lbl = Label(text="X - turn",font_size=40)
        self.x_player_lbl = Label(text=str(x_counter),font_size=40,color=[1,0,0,1])
        self.y_player_lbl = Label(text=str(y_counter),font_size=40,color=[0,1,0,1])
        gl.add_widget(self.x_player_lbl)
        gl.add_widget(self.lbl)
        gl.add_widget(self.y_player_lbl)
        gl.add_widget(self.b1)
        gl.add_widget(self.b2)
        gl.add_widget(self.b3)
        gl.add_widget(self.b4)
        gl.add_widget(self.b5)
        gl.add_widget(self.b6)
        gl.add_widget(self.b7)
        gl.add_widget(self.b8)
        gl.add_widget(self.b9)
        gl.add_widget(menu_bl)
        gl.add_widget(user_bl)
        al.add_widget(gl)
        return al
    def increase_val(self,instance):
        global user_val,players_turn,x_counter,y_counter
        self.x_player_lbl.text=str(0)
        self.y_player_lbl.text = str(0)
        self.lbl.color = [1, 1, 1, 1]
        self.b1.text = "N"
        self.b1.color = [1, 1, 1, 1]
        self.b2.text = "N"
        self.b2.color = [1, 1, 1, 1]
        self.b3.text = "N"
        self.b3.color = [1, 1, 1, 1]
        self.b4.text = "N"
        self.b4.color = [1, 1, 1, 1]
        self.b5.text = "N"
        self.b5.color = [1, 1, 1, 1]
        self.b6.text = "N"
        self.b6.color = [1, 1, 1, 1]
        self.b7.text = "N"
        self.b7.color = [1, 1, 1, 1]
        self.b8.text = "N"
        self.b8.color = [1, 1, 1, 1]
        self.b9.text = "N"
        self.b9.color = [1, 1, 1, 1]
        players_turn = 0
        self.lbl.text = "X - turn"
        x_counter=0
        y_counter=0
        user_val = 2
    def downgrade_val(self,instance):
        global user_val, players_turn, x_counter, y_counter
        self.x_player_lbl.text = str(0)
        self.y_player_lbl.text = str(0)
        self.lbl.color = [1, 1, 1, 1]
        self.b1.text = "N"
        self.b1.color = [1, 1, 1, 1]
        self.b2.text = "N"
        self.b2.color = [1, 1, 1, 1]
        self.b3.text = "N"
        self.b3.color = [1, 1, 1, 1]
        self.b4.text = "N"
        self.b4.color = [1, 1, 1, 1]
        self.b5.text = "N"
        self.b5.color = [1, 1, 1, 1]
        self.b6.text = "N"
        self.b6.color = [1, 1, 1, 1]
        self.b7.text = "N"
        self.b7.color = [1, 1, 1, 1]
        self.b8.text = "N"
        self.b8.color = [1, 1, 1, 1]
        self.b9.text = "N"
        self.b9.color = [1, 1, 1, 1]
        players_turn = 0
        self.lbl.text = "X - turn"
        x_counter = 0
        y_counter = 0
        user_val=1
    def game_func(self,instance):
        global players_turn,x_counter,y_counter,coins,user_val
        if user_val==2:
            name = instance.text
            if name == "N":
                if players_turn % 2 == 0:
                    instance.text = "X"
                    self.lbl.text = "O-turn"
                    instance.color = [1, 0, 0, 1]
                else:
                    instance.text = "O"
                    self.lbl.text = "X-turn"
                    instance.color = [0, 1, 0, 1]
                players_turn += 1
            else:
                instance.text = instance.text
            butn_lst = [[self.b1.text, self.b2.text, self.b3.text], [self.b4.text, self.b5.text, self.b6.text],
                        [self.b7.text, self.b8.text, self.b9.text]]
            if (check_state(butn_lst)) == "X":
                x_counter += 1
                coins += 2
                self.lbl.text = "X - turn"
                self.x_player_lbl.text = str(x_counter)
                players_turn = 0
                self.b1.text = "N"
                self.b1.color = [1, 1, 1, 1]
                self.b2.text = "N"
                self.b2.color = [1, 1, 1, 1]
                self.b3.text = "N"
                self.b3.color = [1, 1, 1, 1]
                self.b4.text = "N"
                self.b4.color = [1, 1, 1, 1]
                self.b5.text = "N"
                self.b5.color = [1, 1, 1, 1]
                self.b6.text = "N"
                self.b6.color = [1, 1, 1, 1]
                self.b7.text = "N"
                self.b7.color = [1, 1, 1, 1]
                self.b8.text = "N"
                self.b8.color = [1, 1, 1, 1]
                self.b9.text = "N"
                self.b9.color = [1, 1, 1, 1]
                box_x = BoxLayout(orientation="vertical")
                popup_x = Popup(title="Congratulations!", content=box_x, size_hint=[.5, .5], auto_dismiss=False)
                lbl_x = Label(text="X won!!!", font_size=100, color=[1, 0, 0, 1])
                but_x = Button(text="Close this popup!", on_press=popup_x.dismiss, size_hint=[1, .2])
                box_x.add_widget(lbl_x)
                box_x.add_widget(but_x)
                popup_x.open()
            elif check_state(butn_lst) == "O":
                y_counter += 1
                coins += 2
                self.lbl.text = "X - turn"
                self.y_player_lbl.text = str(y_counter)
                players_turn = 0
                self.b1.text = "N"
                self.b1.color = [1, 1, 1, 1]
                self.b2.text = "N"
                self.b2.color = [1, 1, 1, 1]
                self.b3.text = "N"
                self.b3.color = [1, 1, 1, 1]
                self.b4.text = "N"
                self.b4.color = [1, 1, 1, 1]
                self.b5.text = "N"
                self.b5.color = [1, 1, 1, 1]
                self.b6.text = "N"
                self.b6.color = [1, 1, 1, 1]
                self.b7.text = "N"
                self.b7.color = [1, 1, 1, 1]
                self.b8.text = "N"
                self.b8.color = [1, 1, 1, 1]
                self.b9.text = "N"
                self.b9.color = [1, 1, 1, 1]
                box_y = BoxLayout(orientation="vertical")
                popup_y = Popup(title="Congratulations!", content=box_y, size_hint=[.5, .5], auto_dismiss=False)
                lbl_y = Label(text="O won!!!", font_size=100, color=[0, 1, 0, 1])
                but_y = Button(text="Close this popup!", on_press=popup_y.dismiss, size_hint=[1, .2])
                box_y.add_widget(lbl_y)
                box_y.add_widget(but_y)
                popup_y.open()
            elif players_turn == 9 and check_state(butn_lst) == "Draw":
                coins += 2
                players_turn = 0
                self.lbl.text = "X - turn"
                self.b1.text = "N"
                self.b1.color = [1, 1, 1, 1]
                self.b2.text = "N"
                self.b2.color = [1, 1, 1, 1]
                self.b3.text = "N"
                self.b3.color = [1, 1, 1, 1]
                self.b4.text = "N"
                self.b4.color = [1, 1, 1, 1]
                self.b5.text = "N"
                self.b5.color = [1, 1, 1, 1]
                self.b6.text = "N"
                self.b6.color = [1, 1, 1, 1]
                self.b7.text = "N"
                self.b7.color = [1, 1, 1, 1]
                self.b8.text = "N"
                self.b8.color = [1, 1, 1, 1]
                self.b9.text = "N"
                self.b9.color = [1, 1, 1, 1]
                box_d = BoxLayout(orientation="vertical")
                popup_d = Popup(title="Hmmmm...", content=box_d, size_hint=[.5, .5], auto_dismiss=False)
                lbl_d = Label(text="Draw.", font_size=100, color=[1, 1, 1, 1])
                but_d = Button(text="Close this popup!", on_press=popup_d.dismiss, size_hint=[1, .2])
                box_d.add_widget(lbl_d)
                box_d.add_widget(but_d)
                popup_d.open()
            if x_counter > y_counter:
                self.lbl.color = [1, 0, 0, 1]
            elif x_counter == y_counter:
                self.lbl.color = [1, 1, 1, 1]
            elif x_counter < y_counter:
                self.lbl.color = [0, 1, 0, 1]
        elif user_val==1:
            if instance.text=="N":
                instance.text="X"
                instance.color = [1, 0, 0, 1]
                n_counter = 0
                btn_lst = [[self.b1.text, self.b2.text, self.b3.text], [self.b4.text, self.b5.text, self.b6.text],
                            [self.b7.text, self.b8.text, self.b9.text]]
                for x in btn_lst:
                    for y in x:
                        if y=="N":
                            n_counter+=1

                if n_counter==0 or check_state(btn_lst)!="Draw":
                    if (check_state(btn_lst)) == "X":
                        x_counter += 1
                        coins += 2
                        self.lbl.text = "X - turn"
                        self.x_player_lbl.text = str(x_counter)
                        players_turn = 0
                        self.b1.text = "N"
                        self.b1.color = [1, 1, 1, 1]
                        self.b2.text = "N"
                        self.b2.color = [1, 1, 1, 1]
                        self.b3.text = "N"
                        self.b3.color = [1, 1, 1, 1]
                        self.b4.text = "N"
                        self.b4.color = [1, 1, 1, 1]
                        self.b5.text = "N"
                        self.b5.color = [1, 1, 1, 1]
                        self.b6.text = "N"
                        self.b6.color = [1, 1, 1, 1]
                        self.b7.text = "N"
                        self.b7.color = [1, 1, 1, 1]
                        self.b8.text = "N"
                        self.b8.color = [1, 1, 1, 1]
                        self.b9.text = "N"
                        self.b9.color = [1, 1, 1, 1]
                        box_x = BoxLayout(orientation="vertical")
                        popup_x = Popup(title="Congratulations!", content=box_x, size_hint=[.5, .5], auto_dismiss=False)
                        lbl_x = Label(text="X won!!!", font_size=100, color=[1, 0, 0, 1])
                        but_x = Button(text="Close this popup!", on_press=popup_x.dismiss, size_hint=[1, .2])
                        box_x.add_widget(lbl_x)
                        box_x.add_widget(but_x)
                        popup_x.open()
                    elif check_state(btn_lst) == "O":
                        y_counter += 1
                        coins += 2
                        self.lbl.text = "X - turn"
                        self.y_player_lbl.text = str(y_counter)
                        players_turn = 0
                        self.b1.text = "N"
                        self.b1.color = [1, 1, 1, 1]
                        self.b2.text = "N"
                        self.b2.color = [1, 1, 1, 1]
                        self.b3.text = "N"
                        self.b3.color = [1, 1, 1, 1]
                        self.b4.text = "N"
                        self.b4.color = [1, 1, 1, 1]
                        self.b5.text = "N"
                        self.b5.color = [1, 1, 1, 1]
                        self.b6.text = "N"
                        self.b6.color = [1, 1, 1, 1]
                        self.b7.text = "N"
                        self.b7.color = [1, 1, 1, 1]
                        self.b8.text = "N"
                        self.b8.color = [1, 1, 1, 1]
                        self.b9.text = "N"
                        self.b9.color = [1, 1, 1, 1]
                        box_y = BoxLayout(orientation="vertical")
                        popup_y = Popup(title="Congratulations!", content=box_y, size_hint=[.5, .5], auto_dismiss=False)
                        lbl_y = Label(text="O won!!!", font_size=100, color=[0, 1, 0, 1])
                        but_y = Button(text="Close this popup!", on_press=popup_y.dismiss, size_hint=[1, .2])
                        box_y.add_widget(lbl_y)
                        box_y.add_widget(but_y)
                        popup_y.open()
                    elif check_state(btn_lst) == "Draw":
                        coins += 2
                        players_turn = 0
                        self.lbl.text = "X - turn"
                        self.b1.text = "N"
                        self.b1.color = [1, 1, 1, 1]
                        self.b2.text = "N"
                        self.b2.color = [1, 1, 1, 1]
                        self.b3.text = "N"
                        self.b3.color = [1, 1, 1, 1]
                        self.b4.text = "N"
                        self.b4.color = [1, 1, 1, 1]
                        self.b5.text = "N"
                        self.b5.color = [1, 1, 1, 1]
                        self.b6.text = "N"
                        self.b6.color = [1, 1, 1, 1]
                        self.b7.text = "N"
                        self.b7.color = [1, 1, 1, 1]
                        self.b8.text = "N"
                        self.b8.color = [1, 1, 1, 1]
                        self.b9.text = "N"
                        self.b9.color = [1, 1, 1, 1]
                        box_d = BoxLayout(orientation="vertical")
                        popup_d = Popup(title="Hmmmm...", content=box_d, size_hint=[.5, .5], auto_dismiss=False)
                        lbl_d = Label(text="Draw.", font_size=100, color=[1, 1, 1, 1])
                        but_d = Button(text="Close this popup!", on_press=popup_d.dismiss, size_hint=[1, .2])
                        box_d.add_widget(lbl_d)
                        box_d.add_widget(but_d)
                        popup_d.open()
                    if x_counter > y_counter:
                        self.lbl.color = [1, 0, 0, 1]
                    elif x_counter == y_counter:
                        self.lbl.color = [1, 1, 1, 1]
                    elif x_counter < y_counter:
                        self.lbl.color = [0, 1, 0, 1]
                else:
                    lst1 = btn_lst[0]
                    lst2 = btn_lst[1]
                    lst3 = btn_lst[2]
                    lst4 = [lst1[0], lst2[0], lst3[0]]
                    lst5 = [lst1[1], lst2[1], lst3[1]]
                    lst6 = [lst1[2], lst2[2], lst3[2]]
                    lst7 = [lst1[0], lst2[1], lst3[2]]
                    lst8 = [lst3[0], lst2[1], lst1[2]]
                    if n_counter==8:
                        if self.b1.text=="X":
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        elif self.b2.text=="X":
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                        elif self.b3.text=="X":
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        elif self.b4.text=="X":
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        elif self.b5.text=="X":
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        elif self.b6.text=="X":
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                        elif self.b7.text=="X":
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        elif self.b8.text=="X":
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                        elif self.b9.text=="X":
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                    elif lst1.count("O")==2 and lst1.count("N")==1:
                        ind = lst1.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b2.text = "O"
                            self.b2.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                    elif lst2.count("O") == 2 and lst2.count("N") == 1:
                        ind = lst2.index("N")
                        if ind == 0:
                            self.b4.text = "O"
                            self.b4.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b6.text = "O"
                            self.b6.color = [0, 1, 0, 1]
                    elif lst3.count("O") == 2 and lst3.count("N") == 1:
                        ind = lst3.index("N")
                        if ind == 0:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b8.text = "O"
                            self.b8.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst4.count("O") == 2 and lst4.count("N") == 1:
                        ind = lst4.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b4.text = "O"
                            self.b4.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                    elif lst5.count("O") == 2 and lst5.count("N") == 1:
                        ind = lst5.index("N")
                        if ind == 0:
                            self.b2.text = "O"
                            self.b2.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b8.text = "O"
                            self.b8.color = [0, 1, 0, 1]
                    elif lst6.count("O") == 2 and lst6.count("N") == 1:
                        ind = lst6.index("N")
                        if ind == 0:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b6.text = "O"
                            self.b6.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst7.count("O") == 2 and lst7.count("N") == 1:
                        ind = lst7.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst8.count("O") == 2 and lst8.count("N") == 1:
                        ind = lst8.index("N")
                        if ind == 0:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                    elif lst1.count("X") == 2 and lst1.count("N") == 1:
                        ind = lst1.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b2.text = "O"
                            self.b2.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                    elif lst2.count("X") == 2 and lst2.count("N") == 1:
                        ind = lst2.index("N")
                        if ind == 0:
                            self.b4.text = "O"
                            self.b4.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b6.text = "O"
                            self.b6.color = [0, 1, 0, 1]
                    elif lst3.count("X") == 2 and lst3.count("N") == 1:
                        ind = lst3.index("N")
                        if ind == 0:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b8.text = "O"
                            self.b8.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst4.count("X") == 2 and lst4.count("N") == 1:
                        ind = lst4.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b4.text = "O"
                            self.b4.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                    elif lst5.count("X") == 2 and lst5.count("N") == 1:
                        ind = lst5.index("N")
                        if ind == 0:
                            self.b2.text = "O"
                            self.b2.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b8.text = "O"
                            self.b8.color = [0, 1, 0, 1]
                    elif lst6.count("X") == 2 and lst6.count("N") == 1:
                        ind = lst6.index("N")
                        if ind == 0:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b6.text = "O"
                            self.b6.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst7.count("X") == 2 and lst7.count("N") == 1:
                        ind = lst7.index("N")
                        if ind == 0:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    elif lst8.count("X") == 2 and lst8.count("N") == 1:
                        ind = lst8.index("N")
                        if ind == 0:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        if ind == 1:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if ind == 2:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                    else:
                        ind_lst = []
                        for i in range(3):
                            for j in range(3):
                                if btn_lst[i][j] == "N":
                                    if i == 0:
                                        ind_lst.append(2 + i + j)
                                    if i == 1:
                                        ind_lst.append(5 + i + j)
                                    if i == 2:
                                        ind_lst.append(8 + i + j)
                        rand_ind = random.randint(0, len(ind_lst) - 1)
                        rand_ind = ind_lst[rand_ind]
                        if rand_ind == 2:
                            self.b1.text = "O"
                            self.b1.color = [0, 1, 0, 1]
                        if rand_ind == 3:
                            self.b2.text = "O"
                            self.b2.color = [0, 1, 0, 1]
                        if rand_ind == 4:
                            self.b3.text = "O"
                            self.b3.color = [0, 1, 0, 1]
                        if rand_ind == 6:
                            self.b4.text = "O"
                            self.b4.color = [0, 1, 0, 1]
                        if rand_ind == 7:
                            self.b5.text = "O"
                            self.b5.color = [0, 1, 0, 1]
                        if rand_ind == 8:
                            self.b6.text = "O"
                            self.b6.color = [0, 1, 0, 1]
                        if rand_ind == 10:
                            self.b7.text = "O"
                            self.b7.color = [0, 1, 0, 1]
                        if rand_ind == 11:
                            self.b8.text = "O"
                            self.b8.color = [0, 1, 0, 1]
                        if rand_ind == 12:
                            self.b9.text = "O"
                            self.b9.color = [0, 1, 0, 1]
                    btn_lst_1 = [[self.b1.text, self.b2.text, self.b3.text],
                                 [self.b4.text, self.b5.text, self.b6.text],
                                 [self.b7.text, self.b8.text, self.b9.text]]
                    if (check_state(btn_lst_1)) == "X":
                        x_counter += 1
                        coins += 2
                        self.lbl.text = "X - turn"
                        self.x_player_lbl.text = str(x_counter)
                        players_turn = 0
                        self.b1.text = "N"
                        self.b1.color = [1, 1, 1, 1]
                        self.b2.text = "N"
                        self.b2.color = [1, 1, 1, 1]
                        self.b3.text = "N"
                        self.b3.color = [1, 1, 1, 1]
                        self.b4.text = "N"
                        self.b4.color = [1, 1, 1, 1]
                        self.b5.text = "N"
                        self.b5.color = [1, 1, 1, 1]
                        self.b6.text = "N"
                        self.b6.color = [1, 1, 1, 1]
                        self.b7.text = "N"
                        self.b7.color = [1, 1, 1, 1]
                        self.b8.text = "N"
                        self.b8.color = [1, 1, 1, 1]
                        self.b9.text = "N"
                        self.b9.color = [1, 1, 1, 1]
                        box_x = BoxLayout(orientation="vertical")
                        popup_x = Popup(title="Congratulations!", content=box_x, size_hint=[.5, .5],
                                        auto_dismiss=False)
                        lbl_x = Label(text="X won!!!", font_size=100, color=[1, 0, 0, 1])
                        but_x = Button(text="Close this popup!", on_press=popup_x.dismiss, size_hint=[1, .2])
                        box_x.add_widget(lbl_x)
                        box_x.add_widget(but_x)
                        popup_x.open()
                    elif check_state(btn_lst_1) == "O":
                        y_counter += 1
                        coins += 2
                        self.lbl.text = "X - turn"
                        self.y_player_lbl.text = str(y_counter)
                        players_turn = 0
                        self.b1.text = "N"
                        self.b1.color = [1, 1, 1, 1]
                        self.b2.text = "N"
                        self.b2.color = [1, 1, 1, 1]
                        self.b3.text = "N"
                        self.b3.color = [1, 1, 1, 1]
                        self.b4.text = "N"
                        self.b4.color = [1, 1, 1, 1]
                        self.b5.text = "N"
                        self.b5.color = [1, 1, 1, 1]
                        self.b6.text = "N"
                        self.b6.color = [1, 1, 1, 1]
                        self.b7.text = "N"
                        self.b7.color = [1, 1, 1, 1]
                        self.b8.text = "N"
                        self.b8.color = [1, 1, 1, 1]
                        self.b9.text = "N"
                        self.b9.color = [1, 1, 1, 1]
                        box_y = BoxLayout(orientation="vertical")
                        popup_y = Popup(title="Congratulations!", content=box_y, size_hint=[.5, .5],
                                        auto_dismiss=False)
                        lbl_y = Label(text="O won!!!", font_size=100, color=[0, 1, 0, 1])
                        but_y = Button(text="Close this popup!", on_press=popup_y.dismiss, size_hint=[1, .2])
                        box_y.add_widget(lbl_y)
                        box_y.add_widget(but_y)
                        popup_y.open()
                    if x_counter > y_counter:
                        self.lbl.color = [1, 0, 0, 1]
                    elif x_counter == y_counter:
                        self.lbl.color = [1, 1, 1, 1]
                    elif x_counter < y_counter:
                        self.lbl.color = [0, 1, 0, 1]
if __name__=="__main__":
    GameApp().run()
