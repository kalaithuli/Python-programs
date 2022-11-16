def insert(a):
    b = eval(input("Enter the element to be inserted "))
    c = int(input("Enter the position to be inserted at "))
    if b not in a:
        a = a + [0]
        d = a[c - 1]
        a[c - 1] = b
        for i in range(c + 1, len(a) - 1):
            e = a[i + 1]
            a[i + 1] = d
            d = e
        print(a)
    else:
        print("It already exists ")


def delete(a):
    c = eval(input("Enter the element to be deleted "))
    nl = []
    cnt = a.count(c)
    if(cnt > 1):
        for i in range(len(a)):
            if (a[i] != c):
                nl.append(a[i])
    print(nl)
ans ='y'
while ans == 'y':
    a = eval(input("Enter a list "))
    print("1) Insertion ")
    print("2) Deletion ")
    ch = int(input("Enter your choice "))
    if ch == 1:
        insert(a)
    elif ch == 2:
        delete(a)
    else:
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")








