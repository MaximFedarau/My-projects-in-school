from tkinter import *
from math import *
from tkinter.ttk import Radiobutton
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk
def broken():
    window.destroy()
window = Tk()
window.configure(bg='wheat1')
label=Label(window,width=40,text="Welcome, user...",fg='black',font = ("Brush Script MT",40),bg="wheat1")
label.place(x=-90,y=120)
byt_1=Button(window,text="Start calculating...",fg='black',bg='wheat1',font=("Times New Roman",18,'roman'),command=broken,activeforeground="green",activebackground='white')
byt_1.place(x=190,y=200)
window.geometry("600x300")
window.title("Start")
window.mainloop()
root = Tk()
root.title("Calculator")
root.geometry('1400x1080')
root.configure(bg="snow")
def new_window():
    def night():
        root.configure(bg='gray26')
        window_1.configure(bg='gray26')
    def classic():
        root.configure(bg='snow')
        window_1.configure(bg='snow')
    def seaside():
        root.configure(bg='navajo white')
        window_1.configure(bg='navajo white')
    def aquamarine():
        root.configure(bg='aquamarine')
        window_1.configure(bg='aquamarine')
    def year_2007():
        root.configure(bg='maroon2')
        window_1.configure(bg='maroon2')
    def patience():
        root.configure(bg='green')
        window_1.configure(bg='green')
    def desert():
        root.configure(bg='khaki')
        window_1.configure(bg='khaki')
    def wave():
        root.configure(bg='dodger blue')
        window_1.configure(bg='dodger blue')
    def quit():
        window_1.destroy()
    window_1 = Tk()
    window_1.title("Settings")
    var = IntVar()
    var.set(0)
    rad_1 = Radiobutton(window_1,text="classic",value=1,variable=var,command=classic)
    rad_2 = Radiobutton(window_1,text="night",value=2,variable=var,command=night)
    rad_3 = Radiobutton(window_1, text="seaside", value=3, variable=var,command= seaside)
    rad_4 = Radiobutton(window_1, text="aquamarine", value=4, variable=var, command=aquamarine)
    rad_5 = Radiobutton(window_1, text="2007", value=5, variable=var, command=year_2007)
    rad_6 = Radiobutton(window_1, text="patience", value=6, variable=var, command=patience)
    rad_7 = Radiobutton(window_1, text="desert", value=7, variable=var, command=desert)
    rad_8 = Radiobutton(window_1, text="wave", value=8, variable=var, command=wave)
    rad_9 = Radiobutton(window_1, text="Quit", value=9, variable=var, command=quit)
    rad_1.grid(column=0,row=0)
    rad_2.grid(column=0, row=1)
    rad_3.grid(column=0, row=2)
    rad_4.grid(column=0,row=3)
    rad_5.grid(column=0, row=4)
    rad_6.grid(column=0, row=5)
    rad_7.grid(column=0, row=6)
    rad_8.grid(column=0, row=7)
    rad_9.grid(column=1,row=0)
    window_1.mainloop()
def off():
    quit()
def plus():
    s = entr.get()
    s1 = s.split()
    value = 0
    for i in s1:
        if i=="ans":
            value+=lbl.cget("text")
        elif i=="pi":
            value+=pi
        else:
            value+=float(i)
    lbl.configure(text=value)
    entr.delete(0,END)
def minus():
    s = entr.get()
    s1 = s.split()
    if s1[0]=="ans" and s1[1]!="ans" and s1[1]!="pi":
        lbl.configure(text=lbl.cget("text")-float(s1[1]))
        entr.delete(0, END)
    if s1[0] == "ans" and s1[1] != "ans" and s1[1] == "pi":
        lbl.configure(text=lbl.cget("text") - pi)
        entr.delete(0, END)
    elif s1[0]!="ans" and s1[1]=="ans" and s1[0]!="pi":
        lbl.configure(text=float(s1[0])-lbl.cget("text"))
        entr.delete(0, END)
    elif s1[0]!="ans" and s1[1]=="ans" and s1[0]=="pi":
        lbl.configure(text=pi-lbl.cget("text"))
        entr.delete(0, END)
    elif s1[1]==s1[0]=="ans":
        lbl.configure(text=0.0)
        entr.delete(0, END)
    else:
        value = 0
        if s1[0]=="pi" and s1[1]!="pi":
            lbl.configure(text=pi - float(s1[1]))
            entr.delete(0, END)
        elif s1[1]=="pi" and s1[0]!="pi":
            lbl.configure(text=float(s1[0]) - pi)
            entr.delete(0, END)
        elif s1[1]==s1[0]=="pi":
            lbl.configure(text=0.0)
            entr.delete(0, END)
        else:
            value = float(s1[0])-float(s1[1])
            lbl.configure(text=value)
            entr.delete(0, END)
def multiply():
    s = entr.get()
    s1 = s.split()
    value = 1
    for i in s1:
        if i=="ans":
            value*=lbl.cget("text")
        elif i=="pi":
            value*=pi
        else:
            value *= float(i)
    lbl.configure(text=value)
    entr.delete(0, END)
def div():
    s = entr.get()
    s1 = s.split()
    if s1[0]=="ans" and s1[1]!="ans" and s1[1]!="pi":
        try:
            lbl.configure(text=lbl.cget("text")/float(s1[1]))
        except ZeroDivisionError:
            lbl.configure(text="Error")
        entr.delete(0,END)
    elif s1[0] == "ans" and s1[1] != "ans" and s1[1] == "pi":
        lbl.configure(text=lbl.cget("text") / pi)
        entr.delete(0, END)
    elif s1[1]=="ans" and lbl.cget("text")!=0 and s1[0]!="ans" and s1[0]!="pi":
        lbl.configure(text=float(s1[0])/lbl.cget("text"))
        entr.delete(0,END)
    elif s1[1]=="ans" and lbl.cget("text")!=0 and s1[0]!="ans" and s1[0]=="pi":
        lbl.configure(text=pi/lbl.cget("text"))
        entr.delete(0,END)
    elif s1[0]==s1[1]=="ans":
        lbl.configure(text=1.0)
        entr.delete(0, END)
    elif s1[0]==s1[1]=="pi":
        lbl.configure(text=1.0)
        entr.delete(0, END)
    elif s1[1]=="ans" and lbl.cget("text")==0:
        lbl.configure(text="Error")
        entr.delete(0, END)
    else:
        value=1
        if s1[0]!="pi" and s1[1]=="pi":
            value = float(s1[0]) / pi
            lbl.configure(text=value)
        elif s1[1]==s1[0]=="pi":
            lbl.configure(text=value)
        elif s1[0]=="pi" and s1[1]!="pi":
            try:
                value = pi / float(s1[1])
                lbl.configure(text=value)
            except ZeroDivisionError:
                lbl.configure(text="Error")
        else:
            try:
                value = float(s1[0]) / float(s1[1])
                lbl.configure(text=value)
            except ZeroDivisionError:
                lbl.configure(text="Error")
        entr.delete(0, END)
def square_root():
    s = entr.get()
    if s=="ans":
        lbl.configure(text=sqrt(lbl.cget("text")))
        entr.delete(0,END)
    elif s=="pi":
        lbl.configure(text=sqrt(pi))
        entr.delete(0,END)
    else:
        value = sqrt(float(s))
        lbl.configure(text=value)
        entr.delete(0, END)
def factorial_1():
    s = entr.get()
    if s=="ans":
        lbl.configure(text=factorial(lbl.cget("text")))
        entr.delete(0, END)
    elif s=="pi":
        lbl.configure(text="Error")
        entr.delete(0, END)
    else:
        value=factorial(float(s))
        lbl.configure(text=value)
        entr.delete(0, END)
def power():
    s = entr.get()
    s1 = s.split()
    if s1[0]=="ans" and s1[1]!="ans" and s1[1]!="pi":
        lbl.configure(text=lbl.cget("text")**float(s1[1]))
        entr.delete(0, END)
    elif s1[0]=="ans" and s1[1]!="ans" and s1[1]=="pi":
        lbl.configure(text=lbl.cget("text") ** pi)
        entr.delete(0, END)
    elif s1[0]!="ans" and s1[1]=="ans" and s1[0]!="pi":
        lbl.configure(text=float(s1[0])**lbl.cget("text"))
        entr.delete(0, END)
    elif s1[0]!="ans" and s1[1]=="ans" and s1[0]=="pi":
        lbl.configure(text=pi**lbl.cget("text"))
        entr.delete(0, END)
    elif s1[0]==s1[1]=="ans":
        lbl.configure(text=lbl.cget("text")**lbl.cget("text"))
        entr.delete(0, END)
    else:
        if s1[0]=="pi" and s1[1]!="pi" and s1[1]!="ans":
            lbl.configure(text=pi ** float(s1[1]))
            entr.delete(0, END)
        elif s1[0]!="pi" and s1[1]=="pi" and s1[0]!="ans":
            lbl.configure(text=float(s1[0]) ** pi)
            entr.delete(0, END)
        elif s1[0]==s1[1]=="pi":
            lbl.configure(text=pi**pi)
            entr.delete(0, END)
        else:
            lbl.configure(text=float(s1[0])**float(s1[1]))
            entr.delete(0, END)
def sinus():
    s = entr.get()
    if s=="ans":
        if lbl.cget("text")!=pi:
            lbl.configure(text=sin(lbl.cget("text")))
            entr.delete(0, END)
        else:
            lbl.configure(text=0.0)
            entr.delete(0, END)
    elif s=="pi" or s==pi:
        lbl.configure(text=0.0)
        entr.delete(0, END)
    else:
        lbl.configure(text=sin(float(s)))
        entr.delete(0, END)
def cosinus():
    s = entr.get()
    if s == "ans":
        lbl.configure(text=cos(lbl.cget("text")))
        entr.delete(0, END)
    elif s=="pi":
        lbl.configure(text=cos(pi))
        entr.delete(0, END)
    else:
        lbl.configure(text=cos(float(s)))
        entr.delete(0, END)
def deegese_sin():
    s  =entr.get()
    if s=="ans":
        value = radians(float(lbl.cget("text")))
        lbl.configure(text=sin(value))
        entr.delete(0, END)
    elif s=="pi":
        value = radians(float(pi))
        lbl.configure(text=sin(value))
        entr.delete(0, END)
    else:
        value = radians(float(s))
        lbl.configure(text=sin(value))
        entr.delete(0, END)
def deegese_cos():
    s = entr.get()
    if s=="ans":
        if lbl.cget("text")==90:
            lbl.configure(text=0.0)
            entr.delete(0, END)
        else:
            value = radians(float(lbl.cget("text")))
            lbl.configure(text=cos(value))
            entr.delete(0, END)
    elif s=="pi":
        value = radians(pi)
        lbl.configure(text=cos(value))
        entr.delete(0, END)
    else:
        if s=='90':
            lbl.configure(text=0.0)
            entr.delete(0, END)
        else:
            value = radians(float(s))
            lbl.configure(text=cos(value))
            entr.delete(0, END)
def tangens():
    s = entr.get()
    if s=="ans":
        if lbl.cget("text")!=pi:
            lbl.configure(text=tan(lbl.cget("text")))
            entr.delete(0, END)
        else:
            lbl.configure(text=0.0)
            entr.delete(0, END)
    elif s=="pi" or s==pi:
        lbl.configure(text=0.0)
        entr.delete(0, END)
    else:
        lbl.configure(text=tan(float(s)))
        entr.delete(0, END)
def deegese_tan():
    s = entr.get()
    if s == "ans":
        value = radians(float(lbl.cget("text")))
        lbl.configure(text=tan(value))
        entr.delete(0, END)
    elif s == "pi":
        value = radians(pi)
        lbl.configure(text=tan(value))
        entr.delete(0, END)
    else:
        value = radians(float(s))
        lbl.configure(text=tan(value))
        entr.delete(0, END)
def memory_in():
    s = lbl.cget("text")
    entr_1.insert(0,s)
def cleaner():
    entr_1.delete(0,END)
def memory_out():
    s = entr.get()
    value = entr_1.get()
    s1= s.split()
    if len(s1)==0:
        entr.insert(0,value)
    else:
        entr.insert(4,value)
def clean_entr():
    entr.delete(0,END)
def length_converter():
    def off_length_converter_1():
        length_converter_1.destroy()
    length_converter_1 = Tk()
    length_converter_1.title("Length Converter")
    entr_new = Entry(length_converter_1)
    mainmenu_1 = Menu(length_converter_1)
    length_converter_1.config(menu=mainmenu_1)
    firstmenu_1 = Menu(mainmenu_1, tearoff=0)
    firstmenu_1.add_command(label="Exit converter", command=off_length_converter_1)
    mainmenu_1.add_cascade(label="Quit", menu=firstmenu_1)
    def def_1(event):
        s = combobox.get()
        value = entr_new.get()
        if s=='cm-mm':
            lbl_new.configure(text=float(value)*10)
            entr_new.delete(0,END)
        elif s=="mm-cm":
            lbl_new.configure(text=float(value)/10)
            entr_new.delete(0, END)
        elif s=="m-cm":
            lbl_new.configure(text=float(value) * 100)
            entr_new.delete(0, END)
        elif s=="cm-m":
            lbl_new.configure(text=float(value) / 100)
            entr_new.delete(0, END)
        elif s == "km-m":
            lbl_new.configure(text=float(value) * 1000)
            entr_new.delete(0, END)
        elif s == "m-km":
            lbl_new.configure(text=float(value) / 1000)
            entr_new.delete(0, END)
        elif s=="cm-km":
            lbl_new.configure(text=float(value) / 100000)
            entr_new.delete(0, END)
        elif s=="km-cm":
            lbl_new.configure(text=float(value) * 100000)
            entr_new.delete(0, END)
    List = ['cm-mm','mm-cm','m-cm','cm-m','km-m','m-km','cm-km','km-cm']
    combobox = ttk.Combobox(length_converter_1,value = List)
    combobox.current(0)
    combobox.bind("<<ComboboxSelected>>", def_1)
    lbl_new = Label( length_converter_1)
    combobox.grid(column=2,row=0)
    entr_new.grid(column=0,row=0)
    lbl_new.grid(column=1,row=0)
    length_converter_1.mainloop()
but_1=Button(root,bg='white',fg='black',text="+",width=10,height=12,command=plus,font = ("Comic Sans MS",12,"bold"),activeforeground="white",activebackground='gray',relief=RAISED)
but_1.place(x=0,y=60)
but_2 = Button(root,bg='white',fg='black',text="-",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command=minus,activeforeground="white",activebackground='gray',relief=RAISED)
but_2.place(x=100,y=60)
but_3 = Button(root,bg='white',fg='black',text="*",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command=multiply,activeforeground="white",activebackground='gray',relief=RAISED)
but_3.place(x=200,y=60)
but_4 = Button(root,bg='white',fg='black',text="/",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command = div,activeforeground="white",activebackground='gray',relief=RAISED)
but_4.place(x=300,y=60)
but_5=Button(root,bg='white',fg='black',text="√",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command = square_root,activeforeground="white",activebackground='gray',relief=RAISED)
but_5.place(x=400,y=60)
but_6 = Button(root,bg='white',fg='black',text="!",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command = factorial_1,activeforeground="white",activebackground='gray',relief=RAISED)
but_6.place(x=500,y=60)
but_7 = Button(root,bg='white',fg='black',text="power",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command=power,activeforeground="white",activebackground='gray',relief=RAISED)
but_7.place(x=600,y=60)
but_8 = Button(root,bg='white',fg='black',text="sin",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command=sinus,activeforeground="white",activebackground='gray',relief=RAISED)
but_8.place(x=0,y=300)
but_9 = Button(root,bg='white',fg='black',text="cos",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command = cosinus,activeforeground="white",activebackground='gray',relief=RAISED)
but_9.place(x=100,y=300)
but_10 = Button(root,bg='white',fg='black',text="deg",width=7,height=7,font = ("Comic Sans MS",7,"bold"),command = deegese_sin,activeforeground="white",activebackground='gray',relief=RAISED)
but_10.place(x=0,y=500)
but_11 = Button(root,bg='white',fg='black',text="deg",width=7,height=7,font = ("Comic Sans MS",7,"bold"),command = deegese_cos,activeforeground="white",activebackground='gray',relief=RAISED)
but_11.place(x=100,y=500)
but_12 = Button(root,bg='white',fg='black',text="tan",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command = tangens,activeforeground="white",activebackground='gray',relief=RAISED)
but_12.place(x=200,y=300)
but_13 = Button(root,bg='white',fg='black',text="deg",width=7,height=7,font = ("Comic Sans MS",7,"bold"),command = deegese_tan,activeforeground="white",activebackground='gray',relief=RAISED)
but_13.place(x=200,y=500)
but_14 = Button(root,bg='white',fg='black',text="memory_in",width=10,height=12,font = ("Comic Sans MS",12,"bold"),command=memory_in,activeforeground="white",activebackground='gray',relief=RAISED)
but_14.place(x=700,y=60)
but_15 = Button(root,bg='white',fg='black',text="clean",width=7,height=7,font = ("Comic Sans MS",7,"bold"),command=cleaner,activeforeground="white",activebackground='gray',relief=RAISED)
but_15.place(x=783,y=182)
but_16 = Button(root,bg='white',fg='black',text="memory_out",width=12,height=12,font = ("Comic Sans MS",12,"bold"),command=memory_out,activeforeground="white",activebackground='gray',relief=RAISED)
but_16.place(x=821,y=60)
but_17 = Button(root,bg='white',fg='red',text="C",width=9,height=9,font = ("Comic Sans MS",9,"bold"),command=clean_entr,activeforeground="white",activebackground='gray',relief=RAISED)
but_17.place(x=1333,y=0)
text = scrolledtext.ScrolledText(root, undo=True,wrap=WORD)
text.configure(width=40,height=15)
text.place(x=300,y=300)
lbl = Label(root,bg='white',fg='black',width=30,font=("Comic Sans MS",32,"bold"),relief = SOLID)
lbl.place(x=0,y=0)
entr = Entry(root,bg='white',width=30,font=("MS Sans Serif",35,"bold"),relief = SOLID)
entr.place(x=600,y=0)
entr_1 = Entry(root,bg='white',width=15,font=("MS Sans Serif",20,"bold"),relief = SOLID)
entr_1.place(x=698,y=260)
mainmenu = Menu(root)
root.config(menu=mainmenu)
firstmenu = Menu(mainmenu, tearoff=0)
firstmenu.add_command(label="Quit",command=off)
firstmenu.add_separator()
firstmenu.add_command(label='Settings',command=new_window)
secondmenu = Menu(mainmenu,tearoff=0)
secondmenu.add_command(label='Length converter',command=length_converter)
mainmenu.add_cascade(label="Calculator",menu=firstmenu)
mainmenu.add_cascade(label="Converter",menu=secondmenu)
root.mainloop()
