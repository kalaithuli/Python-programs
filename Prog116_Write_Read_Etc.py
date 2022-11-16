import pickle
import os

def stud_write():
    ans = 'y'
    fout = open("stud2.dat", 'wb')
    while ans == 'y':
        rno = int(input("Enter the Roll No. "))
        name = input("Enter a name ")
        marks = float(input("Enter the Marks "))
        data = {"Roll No": rno, "Sname": name, "Marks": marks}
        pickle.dump(data, fout)
        ans = input("Do you want to continue - y or n ")

    print("Data Written")
    fout.close()


def stud_read():
    fin = open("stud2.dat", 'rb')
    try:
        while True:
            st_rec = pickle.load(fin)
            print(st_rec)

    except EOFError:
        fin.close()


def modify():
    fin = open("stud2.dat", 'rb')
    fout = open("temp2.dat", 'ab')
    rno = int(input("Enter roll no. to be modified "))
    found = False
    try:
        while True:
            st_rec = pickle.load(fin)
            if st_rec["Roll No"] == rno:
                print(st_rec)
                st_rec["Roll No"] = int(input("Enter the Roll No. "))
                st_rec["Sname"] = input("Enter name to be modified ")
                st_rec["Marks"] = float(input("Enter marks to be modified "))
                print(st_rec)
                found = True
                pickle.dump(st_rec, fout)
            else:
                pickle.dump(st_rec, fout)

    except EOFError:
        if found == False:
            print("Record not Found")
        else:
            print("Record updated")

        fin.close()
        fout.close()
    os.remove("stud2.dat")
    os.rename("temp2.dat", "stud2.dat")


def delete():
    fin = open("stud2.dat", 'rb')
    fout = open("temp2.dat", 'ab')
    rno = int(input("Enter roll no. to be deleted "))
    found = False
    try:
        while True:
            st_rec = pickle.load(fin)
            if st_rec["Roll No"] == rno:
                print(st_rec)
                found = True
                ans = input("Are you sure you want to delete(Y/n) ")
                if ans == 'y' or ans == 'Y':
                    continue

            else:
                pickle.dump(st_rec, fout)

    except EOFError:
        if found == False:
            print("Record not Found")
        else:
            print("Record Deleted")

        fin.close()
        fout.close()
    os.remove("stud2.dat")
    os.rename("temp2.dat", "stud2.dat")

def stud_append():
    fin = open("stud2.dat",'ab')
    ans = 'y'
    while ans == 'y':
        rno= int(input("Enter the Roll No. to be added "))
        name = input("Enter a name to be added ")
        marks = float(input("Enter the Marks to be added "))
        data = {"Roll No" : rno , "Sname" : name , "Marks" : marks}
        pickle.dump(data,fin)
        ans = input("Do you want to continue - y or n")
    print("Appended ")

def search():
    fin=open("stud2.dat",'rb')
    r=int(input("enter rno"))
    found=0
    try:
        while True:
            st_rec=pickle.load(fin)
            if st_rec["Roll No"]==r:
                print("record found",st_rec)
                found=1
                a=input("press any key")
                break
    except EOFError:
        fin.close()

    if found==0:
        print("not found")

ch1 = 'y'
while ch1 == 'y' or ch1 == 'Y' :
    print(" 1) Write \n 2) Read \n 3) Modify \n 4) Append \n 5) Delete \n 6) Search ")
    ch = int(input("Enter your Choice"))
    if ch == 1:
        stud_write()
    elif ch == 2:
        stud_read()
    elif ch == 3:
        modify()
    elif ch == 4:
        stud_append()
    elif ch == 5:
        delete()
    elif ch == 6:
        search()
    else:
        print("Enter a valid choice")
    ch1 = input("Do you want to continue (y/n)")


