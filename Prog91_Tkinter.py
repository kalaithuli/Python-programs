from tkinter import*
comp= Tk()

def lib():
    Label(comp, text='Price of the book').grid(row=3)
    Label(comp, text='No.of days book is borrowed for').grid(row=4)
    e1 = Entry(comp)
    e1.grid(row=3,column=1)
    e2 = Entry(comp)
    e2.grid(row=4,column=1)
    a1=e1.get()
    b2=e2.get()
    a=int(a1)
    b=int(b2)
    if (b <= 5):
        fee = (1 / 100) * a * 5
    elif (b > 5 and b <= 10):
        fee = (1 / 100) * a * 5 + (1 * (b - 5))
    elif (b > 10 and b <= 15):
        fee = (1 / 100) * a * 5 + (1 * (b - 5)) + (3.5 * (b - 10))
    else:
        fee = (1 / 100) * a * 5 + (1 * (b - 5)) + + (3.5 * (b - 10)) + (5.5 * (b - 15))
    lbl=Label(comp, text="Fee to be paid : "+str(fee))
    lbl.grid(row=5,column=1)
def elec():
    cn = input("Enter the customer number ")
    u = int(input("Enter the number of units consumed "))
    if (u <= 100):
        amt = u * 3 + 50
    elif (u > 100 and u <= 300):
        amt = 100 * 3 + (u - 100) * 5 + 50
    else:
        amt = 100 * 3 + 200 * 5 + (u - 300) * 7 + 50
    print("The electricity bill for customer number ", cn, " is ", amt)

Label(comp, text="Choose the program you wish to execute").grid(row=0)

Button(comp, text="1)Library Record", command=lib).grid(row=1)
Button(comp, text="2)Electricity Bill", command=elec).grid(row=2)
mainloop()
