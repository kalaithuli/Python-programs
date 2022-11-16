from tkinter import *

# opening window
window1 = Tk()
window1.title("Welcome")
window1.geometry('550x300')


# main window with the menu
def Main_Window():
    top1 = Toplevel(window1)
    top1.title("Welcome")
    top1.geometry('550x300')
    btn1 = Button(top1, text="To-Do Lists", command=Open_window2)
    btn3 = Button(top1, text="Progress Report", command=Open_window3)

    btn2 = Button(top1, text='Exit', command=top1.destroy)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    top1.mainloop()


# first window which teaches about alphabets
def Open_window2():
    top2 = Toplevel()
    top2.title("Tutorials")
    top2.geometry('550x300')
    lbl = Label(top2, text="Learning alphabets")

    bg = PhotoImage(file='pract.png')
    lb2 = Label(top2, image=bg, height=800, width=800)

    btn1 = Button(top2, text="Back", command=top2.destroy)
    lbl.place(x=10, y=30)
    lb2.place(x=10, y=80)
    btn1.place(x=0, y=0)
    top2.mainloop()

def Open_window3():
    top3 = Toplevel()
    top3.title("Tutorials")
    top3.geometry('550x300')
    lbl = Label(top3, text="Learning Numbers")

    bg = PhotoImage(file='capture.png')
    lb2 = Label(top3, image=bg, height=800, width=800)

    btn1 = Button(top3, text="Back", command=top3.destroy)
    lbl.place(x=10, y=30)
    lb2.place(x=10, y=80)
    btn1.place(x=0, y=0)
    top3.mainloop()



btn = Button(window1, text="TUTEESIO", command=Main_Window)
btn.pack()
window1.mainloop()

