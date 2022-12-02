from tkinter import *
from PIL import ImageTk, Image
import time
from itertools import count, cycle
w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)

def page1():
    w1 = Tk()
    w1.geometry('925x500')
    w1.title('Login')
    w1.configure(bg='#ff4f5a')
    w1.minsize(925, 500)

    def signin():
        signin_win = Frame(w1, width=925, height=500, bg='white')
        signin_win.place(x=0, y=0)
        f1 = Frame(signin_win, width=350, height=350, bg='white')
        f1.place(x=480, y=100)

        global img1
        image = Image.open("C:\\Users\\Shivakumar\\Downloads\\XYZ.png")
        resize_image = image.resize((500, 500))
        img1 = ImageTk.PhotoImage(resize_image)
        label1 = Label(signin_win, image=img1, border=0, bg='white')
        label1.image = img1
        label1.place(x=0, y=0)

        l2 = Label(signin_win, text="Sign in", fg='#ff4f5a', bg='white')
        l2.config(font=('Microsoft YaHei UI Light', 23, 'bold'))
        l2.place(x=600, y=60)

        def on_enter(e):
            e1.delete(0, 'end')

        def on_leave(e):
            if e1.get() == '':
                e1.insert(0, 'Username')

        e1 = Entry(f1, width=25, fg='black', border=0, bg='white')
        e1.config(font=('Microsoft YaHei UI Light', 11,))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0, 'Username')
        e1.place(x=30, y=60)

        Frame(f1, width=295, height=2, bg='black').place(x=25, y=87)

        def on_enter(e):
            e2.delete(0, 'end')

        def on_leave(e):
            if e2.get() == '':
                e2.insert(0, 'Password')

        e2 = Entry(f1, width=21, fg='black', border=0, bg='white')
        e2.config(font=('Microsoft YaHei UI Light', 11,))
        e2.bind("<FocusIn>", on_enter)
        e2.bind("<FocusOut>", on_leave)
        e2.insert(0, 'Password')
        e2.place(x=30, y=130)

        Frame(f1, width=295, height=2, bg='black').place(x=25, y=157)

        # def signin():

        Button(f1, width=39, pady=7, text='Sign in', bg='#ff4f5a', fg='white', border=0, command=signin).place(x=35,
                                                                                                               y=204)
        l1 = Label(f1, text="Don't have an account?", fg="black", bg='white')
        l1.config(font=('Microsoft YaHei UI Light', 9,))
        l1.place(x=75, y=250)

        b2 = Button(f1, width=6, text='Sign up', border=0, bg='white', fg='#ff4f5a', command=signup)
        b2.place(x=215, y=250)

    def signup():
        signup_win = Frame(w1, width=925, height=500, bg='white')
        signup_win.place(x=0, y=0)
        f1 = Frame(signup_win, width=350, height=350, bg='white')
        f1.place(x=480, y=70)

        global img2
        image = Image.open("C:\\Users\\Shivakumar\\Downloads\\XYZ.png")
        resize_image = image.resize((500, 500))
        img2 = ImageTk.PhotoImage(resize_image)
        label1 = Label(signup_win, image=img2, border=0, bg='white')
        label1.image = img2
        label1.place(x=0, y=0)

        l2 = Label(signup_win, text="Sign up", fg='#ff4f5a', bg='white')
        l2.config(font=('Microsoft YaHei UI Light', 23, 'bold'))
        l2.place(x=600, y=60)

        def on_enter(e):
            e1.delete(0, 'end')

        def on_leave(e):
            if e1.get() == '':
                e1.insert(0, 'Username')

        e1 = Entry(f1, width=25, fg='black', border=0, bg='white')
        e1.config(font=('Microsoft YaHei UI Light', 11,))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0, 'Username')
        e1.place(x=30, y=60)

        Frame(f1, width=295, height=2, bg='black').place(x=25, y=87)

        def on_enter(e):
            e2.delete(0, 'end')

        def on_leave(e):
            if e2.get() == '':
                e2.insert(0, 'Password')

        e2 = Entry(f1, width=21, fg='black', border=0, bg='white')
        e2.config(font=('Microsoft YaHei UI Light', 11,))
        e2.bind("<FocusIn>", on_enter)
        e2.bind("<FocusOut>", on_leave)
        e2.insert(0, 'Password')
        e2.place(x=30, y=130)

        Frame(f1, width=295, height=2, bg='black').place(x=25, y=157)

        def on_enter(e):
            e3.delete(0, 'end')

        def on_leave(e):
            if e3.get() == '':
                e3.insert(0, 'Confirm Password')

        e3 = Entry(f1, width=21, fg='black', border=0, bg='white')
        e3.config(font=('Microsoft YaHei UI Light', 11,))
        e3.bind("<FocusIn>", on_enter)
        e3.bind("<FocusOut>", on_leave)
        e3.insert(0, 'Confirm Password')
        e3.place(x=30, y=130 + 70)

        Frame(f1, width=295, height=2, bg='black').place(x=25, y=157 + 70)

        # def signup_cmd():

        Button(f1, width=39, pady=7, text='Sign up', bg='#ff4f5a', fg='white', border=0, command=signup_cmd).place(x=35,
                                                                                                                   y=204 + 60)
        l1 = Label(f1, text="Already have an account?", fg="black", bg='white')
        l1.config(font=('Microsoft YaHei UI Light', 9,))
        l1.place(x=70, y=250 + 63)

        b2 = Button(f1, width=6, text='Sign in', border=0, bg='white', fg='#ff4f5a', command=signin)
        b2.place(x=210, y=250 + 63)

    signin()
    w1.mainloop()

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text="  Cridators ", fg='white', bg='#272727')
label1.configure(font=("Castellar", 24, "bold"))
label1.place(x=80,y=90)

label2=Label(w, text=' Loading...', fg='white', bg='#272727')
label2.configure(font=("Calibri", 11))
label2.place(x=15,y=215)

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(5):
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()
page1()
w.mainloop()