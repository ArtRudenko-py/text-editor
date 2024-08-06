import random
import os
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

d=0
f=0
k=0

def save_file():
    d = text1.get("1.0","end")
    filepath=filedialog.asksaveasfile()


    f=open(filepath.name,"w")
    f.write(d)
    f.close()

def open_file():
    text1.delete("1.0","end")
    fileopn=filedialog.askopenfilename()
    f=open(fileopn,"r")
    d=f.read()
    f.close()
    text1.insert("1.0",d)
def new_file():
    text1.delete("1.0","end")

def exit_file():
    root.quit()
def size_f(event):
    print(size.get())

def type_f(event):
    print(type.get())
def set_italic():
    global f
    if f == True:
        f = False
        text1.tag_remove("italic", "1.0", "end")

    else:
        f = True
        text1.tag_add("italic", "1.0", "end")
        text1.tag_configure("italic", font=(type.get() , size.get(),"italic"))
    print(f)


def set_bold():
    global k
    if k == True:
        k = False
        text1.tag_remove("bold", "1.0", "end")

    else:
        k= True
        text1.tag_add("bold", "1.0", "end")
        text1.tag_configure("bold", font=(type.get() , size.get(), "bold"))
    print(k)


def set_underline():


    global d
    if d == True:
        d=False
        text1.tag_remove("underline","1.0","end")

    else:
        d=True
        text1.tag_add("underline", "1.0", "end")
        text1.tag_configure("underline", underline=True)
    print(d)

def font_f(event):
    d = type.get() + " " + size.get()
    text1.tag_add("sz", "1.0", "end")
    text1.tag_configure("sz", font=d)

def save_file_as():
    g = text1.get("1.0", "end")
    file = input("Введите путь к файлу: ")
    try:

        d = open(file, 'w')
        d.write(g)
        d.close()

    except FileNotFoundError:
        print("Такого файла нет")


root=Tk()
root.title("ryry")
root.geometry("600x600")
root.resizable(width=False,height=False)

menu1file=Menu(tearoff=0)
menu1file.add_command(label="Новый", command=new_file)
menu1file.add_command(label="Открыть",command=open_file)
menu1file.add_command(label="Сохранить", command=save_file)
menu1file.add_command(label="Сохранить как", command=save_file_as)
menu1file.add_separator()
menu1file.add_command(label="Выход",command=exit_file)
menu1=Menu()
menu1.add_cascade(label="Text",menu=menu1file)



text1=Text(width=400)
text1.pack()



sizes=["8","10", "12","14","16","18","20","22","24"]
size=ttk.Combobox(values=sizes, state="readonly")
size.current(1)
size.bind("<<ComboboxSelected>>",font_f)
size.place(x=150,y=450,height=20,width=100)


types=["Arial","Times_New_Roman","Helvetica","Verdana"]
type=ttk.Combobox(values=types,state="readonly")
type.current(1)
type.bind("<<ComboboxSelected>>",font_f)
type.place(x=400,y=450,height=20,width=100)



lab1=Label(text="Выберите размер")
lab1.place(x=50,y=450,height=20,width=100)
lab2=Label(text="Выберите шрифт")
lab2.place(x=300,y=450,height=20,width=100)
root.config(menu=menu1)


but1=Button(text="полужирный",command=set_bold)
but1.place(x=50,y=520,height=20,width=100)
but2=Button(text="подчеркнуть",command=set_underline)
but2.place(x=250,y=520,height=20,width=100)
but3=Button(text="курсив",command=set_italic)
but3.place(x=450,y=520,height=20,width=100)

root.mainloop()
