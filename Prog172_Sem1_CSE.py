'''
def strin(s):
    global cu
    global cl
    cu,cl=0,0
    for i in s:
        if i == i.upper():
            cu+=1
        if i == i.lower():
            cl+=1
    return cu,cl

a = strin("PgfdhS")
print("Lower = ",cl)
print("upper = ",cu)
print(a)
'''
'''
def stri(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print(a,b)
    else:
        print(b)
a=input("Enter a string: ")
b=input("Enter a string: ")
stri(a,b)
'''
'''
def li(l):
    a=set(l)
    b=list(a)
    print(b)
l=eval(input("Enter a list: "))
li(l)
'''
'''
def dict(a,b):
    c = {}
    for i in range(len(a)):
        if a[i] not in c:
            c[a[i]]=[b[i]]
            print(c)
        else :
            c[a[i]].append(b[i])
            print(c)
    print(c)

a=['Karnataka','Tamil Nadu','Kerala','Karnataka','Tamil Nadu','Kerala']
b=['mysore','chennai',"trivandrum","hassan",'pondy',"kochi"]
dict(a,b)
'''
'''
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("800x500")
imgTemp = Image.open("C:\\Users\\Shivakumar\\Desktop\\cricket.png")
img2 = imgTemp.resize((height,1800))
img = ImageTk.PhotoImage(img2)

label = Label(root,image=img)
label.pack(side='top',fill=Y,expand=True)
bg = PhotoImage(file="")
mc=Canvas(root,width=800,height=500)
mc.pack(fill="both",expand=True)
mc.create_image(0,0,image=bg,anchor="nw")
root.mainloop()'''
