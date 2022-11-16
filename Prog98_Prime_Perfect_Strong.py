def prime(n1):
    c = 0
    for i in range(2, n1):
        if (n1 % i == 0):
            c = c + 1
    if (c == 0):
        return 1
    else:
        return 0

def strong(n1):
    n2 = n1
    prod = 1
    sum = 0
    while (n1 != 0):
        d = n1%10
        while(d!=1):
            prod = prod * d
            d = d - 1
        sum = sum + prod
        prod = 1
        n1 = n1//10
    if(n2 == sum):
         return 1
    else:
        return 0

def perfect(n1):
    sum=0
    for i in range(1,n1):
        if(n1 % i == 0):
            sum = sum + i
    if (sum == n1):
        return 1
    else:
        return 0

n = int(input("Enter the number "))
print("1) Prime number ")
print("2) Strong number ")
print("3) Perfect number ")
ch = int(input("Enter your choice "))

if ch == 1:
    ans = prime(n)
    if (ans == 1):
        print("Prime number")
    else:
        print("Not a prime number")

elif ch == 2:
    ans = strong(n)
    if (ans == 1):
        print("Strong number")
    else:
        print("Not a strong number")

elif ch == 3:
    ans = perfect(n)
    if (ans == 1):
        print("Perfect number")
    else:
        print("Not a perfect number")

else:
    print("Sorry, wrong choice ")

