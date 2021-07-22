from tkinter import *
root = Tk()
ent1 = Entry(root,width = 20,bd = 3)
ent2 = Entry(root,width = 20,bd = 3)
ent3 = Entry(root,width = 20,bd = 3)
ent4 = Entry(root,width = 20,bd = 3)
ent1.grid(row = 0, column = 1)
ent2.grid(row = 0, column = 2)
ent3.grid(row = 0, column = 3)
ent4.grid(row = 0, column = 4)
canv = Canvas(root,width=1000,height=1000,bg = "white",cursor = "pencil")
canv.create_line(500,0,500,1000,width=5,fill="black",arrow=FIRST)
canv.create_line(0,500,1000,500,width=5,fill="black",arrow=LAST)
a = 480
while a > 0:
    canv.create_line(a,490,a,510,width=5,fill="black")
    a -= 20
b = 520
while b != 1000:
    canv.create_line(b,490,b,510,width=5,fill="black")
    b += 20
с = 480
while с > 0:
    canv.create_line(490,с,510,с,width=5,fill="black")
    с -= 20
d = 520
while d < 1000:
    canv.create_line(490,d,510,d,width=5,fill="black")
    d += 20
g = 20
v  = 480
while g != 480:
    canv.create_text(v,520,text=g,font="Verdana 12")
    g += 20
    v -= 24
canv.create_text(180,20,text="Расстояние от точки О до черточки -- 20 пикселей",font = "Verdana 12",fill = "red")
canv.create_text(510,490,text="O",font="Verdana 12")
canv.pack()
k = int(input("Введите коэффициент k: "))
b = int(input("Введиет перменную b: "))
x = int(input("Введите аргумент x: "))
x1 = int(input("Введите аргумент x1: "))
canv.create_line(x,k*x+b,x1,k*x1+b,width = 2,fill = "green")    
