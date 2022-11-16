from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
import math

# ====================================================================================================================
global m
global p
global c
global t
global a


# functions

def calc():
    m = float(math1.get())
    p = float(physics1.get())
    c = float(chemistry1.get())
    t = (m + p + c)
    a = t / 3
    total1.insert(0, t)
    avg1.insert(0, a)
    if (a >= 95):
        grade1.insert(0, "O")
    elif (a >= 90 and a < 95):
        grade1.insert(0, "A+")
    elif (a >= 80 and a < 90):
        grade1.insert(0, "A")
    elif (a >= 70 and a < 80):
        grade1.insert(0, "B+")
    elif (a >= 60 and a < 70):
        grade1.insert(0, "B")
    elif (a >= 50 and a < 60):
        grade1.insert(0, "C")
    elif (a >= 40 and a < 50):
        grade1.insert(0, "P")
    else:
        grade1.insert(0, "Fail")


def delete():
    math1.delete(0, 'end')
    physics1.delete(0, 'end')
    chemistry1.delete(0, 'end')
    total1.delete(0, 'end')
    avg1.delete(0, 'end')
    grade1.delete(0, 'end')
    t1.delete(0, 'end')
    t2.delete(0, 'end')
    t3.delete(0, 'end')


win = Tk()
win.title("Marksheet Generater")
win.geometry("800x500")
win.maxsize(800, 500)
win.minsize(800, 500)
win['bg'] = "dark orange"

# labels and texts

l1 = Label(win, text="Student Name", font=("verdana", 12, "bold"), borderwidth=5).grid(row=0, column=0, padx=20,
                                                                                       pady=25)
t1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
t1.grid(row=0, column=1, padx=20, pady=25)

l2 = Label(win, text="Student Class", font=("verdana", 12, "bold"), borderwidth=5).grid(row=1, column=0, padx=20,
                                                                                        pady=25)
t2 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
t2.grid(row=1, column=1, padx=20, pady=25)


# marks space

heading = Label(win, text="Marks", font=("verdana", 18, "bold"), fg="gold", bg="dark orange", borderwidth=5).place(
    x=575, y=0)

math = Label(win, text="Math", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=60)
math1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
math1.place(x=590, y=60)

physics = Label(win, text="Physics", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=120)
physics1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
physics1.place(x=590, y=120)

chemistry = Label(win, text="Chemistry", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=180)
chemistry1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
chemistry1.place(x=590, y=180)

# result space


total = Label(win, text="Total", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=300)
total1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
total1.place(x=200, y=300)

avg = Label(win, text="Avarage", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=360)
avg1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
avg1.place(x=200, y=360)

grade = Label(win, text="Grade", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=420)
grade1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
grade1.place(x=200, y=420)

# buttons

calculate = Button(win, text="Calculate", width=12, borderwidth=5, font=("verdana 8 bold"), command=calc).place(x=600,
                                                                                                                y=260)

clear = Button(win, text="Clear", width=12, borderwidth=5, font=("verdana 8 bold"), command=delete).place(x=600, y=300)

win.mainloop()

eng1 = IntVar()
phy1 = IntVar()
hind1 = IntVar()
chemistry1 = IntVar()
math1 = IntVar()
comp1 = IntVar()
if eng1.get() != 0:
    en = float(eng1.get())
    t = t + en
if phy1.get() != 0:
    ph = float(phy1.get())
    t = t + ph
if hind1.get() != 0:
    hi = float(hind1.get())
    t = t + hi
if chemistry1.get() != 0:
    ch = float(chemistry1.get())
    t = t + ch
if math1.get() != 0:
    ma = float(math1.get())
    t = t + ma
if comp1.get() != 0:
    co = float(comp1.get())
    t = t + co


    if eng1 != '':
        en = float(eng1)
        t = t + en
    if phy1 != '':
        ph = float(phy1)
        t = t + ph
    if hind1 != '':
        hi = float(hind1)
        t = t + hi
    if chemistry1 != '':
        ch = float(chemistry1)
        t = t + ch
    if math1 != '':
        ma = float(math1)
        t = t + ma
    if comp1 != '':
        co = float(comp1)
        t = t + co


    eng1 = 0
    phy1 = 0
    hind1 = 0
    chemistry1 = 0
    math1 = 0
    comp1 = 0

    eng1 = ''
    phy1 = ''
    hind1 = ''
    chemistry1 = ''
    math1 = ''
    comp1 = ''

