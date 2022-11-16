def create():
    fin = open("Report.txt" , 'w')
    ans = 'y'
    while(ans == 'y'):
        inp = input("Enter the data ")
        fin.write(inp)
        ans = input("Do you want to continue? y or n? ")
    fin.close()
    fin = open("Report.txt", 'r')
    line = fin.readline()
    while line:
        print(line)
        print()
        line = fin.readline()
    fin.close()
def caseinversion():
    fin = open("Report.txt", 'r')
    fout = open("Report1.txt" , 'w')
    line = fin.readline()
    line1 = ''
    while line:
        for i in range(len(line)):
            b = line[i]
            if b.isupper():
                line1 = line1 + b.lower()
            elif b.islower():
                line1 = line1 + b.upper()
            else :
                line1 = line1 + b
        fout.write(line1)
        line = fin.readline()
        line1 = ''
    fin.close()
    fout.close()
def printrev():
    fin = open("Report.txt" , 'r')
    line = fin.readline()
    while line:
        for i in range((len(line)-1),-1,-1):
            print(line[i] , end ='')
        line = fin.readline()
        print()
    fin.close()
def removea():
    fin = open("Report.txt", 'r')
    fout = open("Report1.txt" , 'w')
    line = fin.readline()
    while line:
        if('a' not in line):
            fout.write(line)
        line = fin.readline()
    fin.close()
    fout.close()
ans = 'y'
while(ans == 'y'):
    print("1) Create a text file and display it ")
    print("2) Case inversion ")
    print("3) Print lines in reverse order ")
    print("4) Remove lines with 'a' in it ")
    ch = int(input("Enter you choice "))
    if ch == 1:
        create()
    elif ch == 2:
        caseinversion()
    elif ch == 3:
        printrev()
    elif ch == 4:
        removea()
    else :
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")
