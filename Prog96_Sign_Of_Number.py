def sign_num(y):
    if(y>0):
        return 1
    elif(y<0):
        return -1
    else:
        return 0
x = int(input("Enter a number "))
ans = sign_num(x)
print(ans)
