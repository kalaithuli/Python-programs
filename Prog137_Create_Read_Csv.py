import csv
def create():
    ans = 'y'
    data = []
    while (ans == 'y'):
        item_code = input("Enter item code :-")
        name = input("Enter name :-")
        price = input("Enter price :-")
        qty = input("Enter Quantity :-")
        data += [[item_code, name, price, qty]]
        ans = input("Do you want to enter more data?y or n? ")

    with open("Groceries.csv", "w", newline="") as f:
        csv_w = csv.writer(f, delimiter=',')
        csv_w.writerows(data)

def read():
    with open("Groceries.csv" ,'r') as fh:
        a = csv.reader(fh)
        for rec in a:
            print(rec)

ans = 'y'
while(ans == 'y'):
    print("1) Create ")
    print("2) Display ")
    ch = int(input("Enter your choice "))
    if ch == 1:
        create()
    elif ch == 2:
        read()
    else:
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")

