import pickle

def bill_write():
    ans = 'y'
    a ='y'
    tnoi = 0
    tc = 0
    fout = open("Bill.dat", 'wb')
    while ans == 'y':
        while a == 'y':
            itco = int(input("Enter the item code "))
            itdes = input("Enter the item description ")
            cpi = float(input("Enter the cost per item "))
            tnoi = tnoi + 1
            tc = tc + cpi
            data = {"Item code ": itco, "Item description ": itdes, "Cost per Item ": cpi}
            pickle.dump(data,fout)
            a = input("Are there more items? y or n? ")
        dat = {"Total number of items " : tnoi, "Total cost " : tc}
        pickle.dump(dat,fout)
        tnoi = 0
        tc = 0
        a ='y'
        ans = input("Do you want to continue? y or n? ")
    print("Data Written")
    fout.close()

def bill_read():
    fin = open("Bill.dat", 'rb')
    try:
        while True:
            st_rec = pickle.load(fin)
            print(st_rec)

    except EOFError:
        fin.close()

def bill_append():
    fin = open("Bill.dat",'ab')
    ans = 'y'
    while ans == 'y':
        itco = int(input("Enter the item code "))
        itdes = input("Enter the item description ")
        cpi = float(input("Enter the cost per item "))
        data = {"Item code ": itco, "Item description ": itdes, "Cost per Item ": cpi}
        pickle.dump(data,fin)
        ans = input("Do you want to continue - y or n")
    print("Appended ")

def search():
    fin = open("Bill.dat",'rb')
    r = int(input("Enter the item code "))
    found = 0
    try:
        while True:
            bill_rec = pickle.load(fin)
            for record in bill_rec:
                    if bill_rec[record] == r:
                        print(record[1])
                        print("Record found", bill_rec)
                        found = 1
                        break

    except EOFError:
        fin.close()
    if found==0:
        print("not found")

ch1 = 'y'
while ch1 == 'y' or ch1 == 'Y' :
    print(" 1) Write \n 2) Read \n 3) Append \n 4) Search ")
    ch = int(input("Enter your Choice"))
    if ch == 1:
        bill_write()
    elif ch == 2:
        bill_read()
    elif ch == 3:
        bill_append()
    elif ch == 4:
        search()
    else:
        print("Enter a valid choice")
    ch1 = input("Do you want to continue (y/n)")