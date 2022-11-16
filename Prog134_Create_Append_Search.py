def create():
    f1 = open("Marks.dat",'w')
    n = int(input("No. of records: "))
    for i in range(n):
        rno = int(input("Enter the roll no.: "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        rec = str(rno)+" "+name+" "+str(marks)
        f1.write(rec + "\n")
    f1.close()
    f2 = open("Marks.dat",'r')
    a=f2.read()
    print(a)
def append():
    f1 = open("Marks.dat","a")
    n = int(input("no: of records:"))
    for i in range(n):
        rno = int(input("enter roll no:"))
        name = input("enter names")
        marks = int(input("enter marks:"))
        rec = str(rno) + " "+ name +" "+str(marks)
        f1.write(rec +"\n")
    f1.close()
    f2 = open("Marks.dat","r")
    a = f2.read()
    print(a)
def search():
        f2=open("Marks.dat","r")
        a=f2.readlines()
        u = int(input("enter roll number:"))
        for i in a:
            if i[0]==str(u):
                print(i)
while True:
    print("1.create:")
    print("2.append")
    print("3.search:")
    ch = int(input("enter your choice:"))
    if ch == 1:
        print(create())
    elif ch == 2:
        print(append())
    elif ch == 3:
        print(search())
    else:
        break


