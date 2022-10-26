from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics','resizable','0')
players_turn = 0
x_counter = 0
y_counter = 0
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
class GameApp(App):
    def build(self):
        al = AnchorLayout(anchor_x = "center",anchor_y = "center")
        gl  = GridLayout(cols=3,rows=4,padding=[50],spacing=15)
        self.b1 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b2 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b3 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b4 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b5 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b6 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b7 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b8 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
        self.b9 = Button(text="N",font_size=50,on_press=self.game_func,background_color=[0,0,0,0])
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
        al.add_widget(gl)
        return al
    def game_func(self,instance):
        global players_turn,x_counter,y_counter
        name = instance.text
        if name=="N":
            if players_turn%2==0:
                instance.text="X"
                self.lbl.text="O-turn"
                instance.color=[1,0,0,1]
            else:
                instance.text="O"
                self.lbl.text = "X-turn"
                instance.color = [0, 1, 0, 1]
            players_turn += 1
        else:
            instance.text=instance.text
        butn_lst = [[self.b1.text,self.b2.text,self.b3.text],[self.b4.text,self.b5.text,self.b6.text],[self.b7.text,self.b8.text,self.b9.text]]
        if (check_state(butn_lst))=="X":
            x_counter += 1
            self.lbl.text="X - turn"
            self.x_player_lbl.text=str(x_counter)
            players_turn = 0
            self.b1.text = "N"
            self.b1.color = [1, 1, 1, 1]
            self.b2.text = "N"
            self.b2.color =[1, 1, 1, 1]
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
            popup_x = Popup(title="Congratulations!",content=box_x,size_hint=[.5,.5],auto_dismiss=False)
            lbl_x = Label(text="X won!!!",font_size=100,color=[1,0,0,1])
            but_x = Button(text="Close this popup!", on_press=popup_x.dismiss,size_hint=[1,.2])
            box_x.add_widget(lbl_x)
            box_x.add_widget(but_x)
            popup_x.open()
        elif check_state(butn_lst)=="O":
            y_counter += 1
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
            popup_y = Popup(title="Congratulations!", content=box_y,size_hint=[.5,.5],auto_dismiss=False)
            lbl_y = Label(text="Y won!!!", font_size=100, color=[0,1,0,1])
            but_y = Button(text="Close this popup!", on_press=popup_y.dismiss, size_hint=[1, .2])
            box_y.add_widget(lbl_y)
            box_y.add_widget(but_y)
            popup_y.open()
        elif players_turn == 9 and check_state(butn_lst)=="Draw":
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
            popup_d = Popup(title="Hmmmm...", content=box_d,size_hint=[.5,.5],auto_dismiss=False)
            lbl_d = Label(text="Draw.", font_size=100, color=[1,1,1,1])
            but_d = Button(text="Close this popup!", on_press=popup_d.dismiss, size_hint=[1, .2])
            box_d.add_widget(lbl_d)
            box_d.add_widget(but_d)
            popup_d.open()
        if x_counter>y_counter:
            self.lbl.color=[1,0,0,1]
        elif x_counter==y_counter:
            self.lbl.color=[1,1,1,1]
        elif x_counter<y_counter:
            self.lbl.color=[0,1,0,1]
if __name__=="__main__":
    GameApp().run()
