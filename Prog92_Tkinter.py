from tkinter import *
window =Tk()
window.geometry('800x400')

lbl =Label(window ,text="Enter first number")
lbl.grid(column=2 ,row=2)
entry =Entry(window)
entry.grid(column=10 ,row=2 ,pady=10)
lbl1 =Label(window ,text="Enter Second number")
lbl1.grid(column=2 ,row=8)
entry1 =Entry(window)
entry1.grid(column=10 ,row=8 ,pady=10)


def sum1():
    a1 =entry.get()
    b1 =entry1.get()
    s=int( a1) + int(b1)
    s1=str ( s)
    lbl2=Label(window, text="Sum =" + s1)
    lbl2.grid(column=2,row= 12)

def sub():
    a1=entry.get()
    b1=entry1.get()
    s=int(a1) - int(b1)
    s1=str(s)
    lbl3=Label(window, text="Difference =" + s1)
    lbl3.grid(column=2,row =12)


def mul():
    a1=entry.get()
    b1=entry1.get()
    s=int(a1) * int(b1)
    s1=str(s)
    lbl4=Label(window, text="Product =" + s1)
    lbl4.grid(column=2,row =12)

def divi():
    a1=entry.get()
    b1=entry1.get()
    s=int(a1) /int (b1)
    s1=str (s)
    lbl5=Label(window, text="Quotient =" + s1)
    lbl5.grid(column=2,row =12)


button = Button(window, text='+', command=sum1)
button.grid(column=5, row=10, padx=10)
button1 = Button(window, text='-', command=sub)
button1.grid(column=10, row=10, padx=10)
button2 = Button(window, text='*', command=mul)
button2.grid(column=15, row=10, padx=10)
button3 = Button(window, text='/', command=divi)
button3.grid(column=20, row=10, padx=10)
window.mainloop()