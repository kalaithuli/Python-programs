import pickle
import os

def emp_write():
    ans = 'y'
    fout = open("Emp.dat", 'wb')
    while ans == 'y':
        eno = int(input("Enter the Employee No. "))
        name = input("Enter Employee name ")
        sal = float(input("Enter the salary "))
        data = {"Emp No": eno, "Employee name": name, "Salary": sal}
        pickle.dump(data, fout)
        ans = input("Do you want to continue - y or n ")

    print("Data Written")
    fout.close()


def emp_read():
    fin = open("Emp.dat", 'rb')
    try:
        while True:
            emp_rec = pickle.load(fin)
            print(emp_rec)

    except EOFError:
        fin.close()


def modify():
    fin = open("Emp.dat", 'rb')
    fout = open("Emp2.dat", 'ab')
    eno = int(input("Enter Employee no. to be modified "))
    found = False
    try:
        while True:
            emp_rec = pickle.load(fin)
            if emp_rec["Emp No"] == eno:
                print(emp_rec)
                emp_rec["Emp No"] = int(input("Enter the Employee No. "))
                emp_rec["Employee name"] = input("Enter name to be modified ")
                emp_rec["Salary"] = float(input("Enter salary to be modified "))
                print(emp_rec)
                found = True
                pickle.dump(emp_rec, fout)
            else:
                pickle.dump(emp_rec, fout)

    except EOFError:
        if found == False:
            print("Record not Found")
        else:
            print("Record updated")

        fin.close()
        fout.close()
    os.remove("Emp.dat")
    os.rename("Emp2.dat", "Emp.dat")

ch1 = 'y'
while ch1 == 'y' or ch1 == 'Y' :
    print(" 1) Write \n 2) Read \n 3) Modify ")
    ch = int(input("Enter your Choice "))
    if ch == 1:
        emp_write()
    elif ch == 2:
        emp_read()
    elif ch == 3:
        modify()
    else:
        print("Enter a valid choice")
    ch1 = input("Do you want to continue (y/n)")
