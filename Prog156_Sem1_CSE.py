#Chck whether given no. is
# perfect square
# fibonacci number
# perfect power of 2
import math

a = int(input("Enter a number: "))
if (int(math.sqrt(a))** 2) == a:
    print("Perfect square ")
else:
    print("Not perfect square")

n = int(input("Enter "))
s = int(math.sqrt((5*n*n)-4)) ** 2
d = int(math.sqrt((5*n*n)+4)) ** 2
if s == (5*n*n)-4 or d == (5*n*n)+4:
    print("Fibonacci num ")
else:
    print("Not a fib num")

n = int(input("Enter a number "))
c = 0
for i in range(1,n):
    if(n%i==0):
        print(i,end=" ")
        c+=1
print()
if c>1:
    print("Not a prime num: ")
else:
    print("Prime number")

s=4
for i in range(1,4):
    print(i,end="+")
    s= s + i
print(4 ," = " ,s)


p=4
for i in range(1,4):
    print(i,end="*")
    p=p * i
print(4 ," = " ,p)
for i in range(1,5):
    print(i,end = " ")
print()
for i in range(8,4,-1):
    print(i,end = " ")

