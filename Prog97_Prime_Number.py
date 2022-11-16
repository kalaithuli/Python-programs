def prime(b):
    c=0
    for i in range (2,b):
        if(b%i == 0):
            c=c+1
    if(c==0):
        return 1
    else :
        return 0
a = int(input("Enter a number "))
ans = prime(a)
print(ans)
if(ans==1):
    print("Prime number")
else:
    print("Not a prime number")
