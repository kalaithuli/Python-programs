def create():
    fin = open("Text File.txt" , 'w')
    ans = 'y'
    while(ans == 'y'):
        inp = input("Enter the data ")
        fin.write(inp)
        ans = input("Do you want to continue? y or n? ")
    fin.close()
def vow_dig_word():
    fin = open("Text File.txt" , 'r')
    vow = 0
    dig = 0
    wor = 0
    vowels = ['a','e','i','o','u']
    digits = ['1','2','3','4','5','6','7','8','9','0']
    line = fin.readline()
    while line:
        for i in range(len(line)):
            b = line[i]
            if b in vowels:
                vow = vow + 1
            elif b in digits:
                dig = dig + 1
            else:
                continue
        list = line.split()
        wor = wor + len(list)
        line = fin.readline()
    print("No. of vowels = ", vow)
    print("No. of digits = " , dig)
    print("No. of words = " , wor)
    fin.close()
def replacewithhash():
    fin = open("Text File.txt" , 'r')
    fout = open("New Text File.txt" , 'w')
    line = fin.readline()
    line1 =''
    while line:
        for i in range(len(line)):
            if (line[i] != ' '):
                line1 = line1 + line[i]
            else :
                line1 = line1 + '#'
        fout.write(line1)
        line = fin.readline()
        line1 = ''
    fin.close()
    fout.close()
ans = 'y'
while(ans == 'y'):
    print("1) Create a text file ")
    print("2) Frequency of Vowels, Digits and Words")
    print("3) Replace spaces with # ")
    ch = int(input("Enter you choice "))
    if ch == 1:
        create()
    elif ch == 2:
        vow_dig_word()
    elif ch == 3:
        replacewithhash()
    else :
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")




