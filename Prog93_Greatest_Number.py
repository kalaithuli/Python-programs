def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
x = int(input("Enter a number "))
y = int(input("Enter a number "))
z = int(input("Enter a number "))
ans = great(x,y,z)
print("Greatest number =" , ans)
