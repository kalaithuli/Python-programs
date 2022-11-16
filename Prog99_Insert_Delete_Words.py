def removeword(s1,g1):
    c = s1.count(g1)
    s1 = s1.split()
    n=''
    while (c!=0):
        s1.remove(g1)
        c = c - 1
    n = ' '.join(s1)
    print(n)

def insertword(s1,g1):
    s1 = s1.split()
    n=''
    pos = int(input("Enter the position "))
    s1.append(0)
    l = len(s1)
    for i in range(l - 1, pos - 1, -1):
        s1[i] = s1[i - 1]
    s1[pos - 1] = g1
    n = ' '.join(s1)
    print(n)

def firstlast(s1):
    l = len(s1)
    newstring = s1[l-1]+s1[1:l-1]+s1[0]
    print(newstring)

s = input("Enter a string ")
print("1) Remove a word " )
print("2) Insert a word")
print("3) First and last letters interchanged ")
ch = int(input("Enter your choice "))

if ch == 1:
    g = input ("Enter the word to be deleted ")
    removeword(s,g)
elif ch == 2:
    g = input("Enter the word to be inserted ")
    insertword(s,g)
elif ch == 3:
    firstlast(s)
else:
    print("Wrong choice ")
