a = int(input("Enter the lower limit "))
b = int(input("Enter the upper limit "))
flag = False
for i in range(a,b,1):
    for j in range(2 , i ):
        if(i%j==0):
            flag = False
    if(flag == True):
        print(i , end =" ")
    flag = True

