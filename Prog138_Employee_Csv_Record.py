import csv
def create():
    ans = 'y'
    data = []
    while (ans == 'y'):
        empno = input("Enter employee number :")
        name = input("Enter employee name :")
        salary = input("Enter the salary :")
        data += [[empno, name, salary]]
        ans = input("Do you want to enter more data?y or n? ")

    with open("Employee.csv", "w", newline="") as f:
        csv_w = csv.writer(f, delimiter=',')
        csv_w.writerows(data)

def read():
    with open("Employee.csv" ,'r') as fh:
        a = csv.reader(fh)
        for rec in a:
            print(rec)

def search():
    with open("Employee.csv" ,'r') as fh:
        a = csv.reader(fh)
        eno = input("Enter the employee number ")
        flag = 0
        for rec in a:
            if rec[0] == eno:
                print("Employee number found ")
                flag = 1
        if flag == 0:
            print("Not found ")
ans = 'y'
while(ans == 'y'):
    print("1) Create ")
    print("2) Display ")
    print("3) Search ")
    ch = int(input("Enter your choice "))
    if ch == 1:
        create()
    elif ch == 2:
        read()
    elif ch == 3:
        search()
    else:
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")