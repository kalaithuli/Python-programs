n = int(input("Enter the value of n "))
a = int(input("Enter the value of a "))
r = int(input("Enter the value of r "))
sum=0
for i in range(0,n+1):
    sum = sum +(a*r**i)
print(sum)

x = int(input("Enter the value of x "))
sum = 0
c=1
for i in range(1,n+1):
    c = c*2
    if(i%2==0):
        sum = sum + (x**c)
    else:
        sum = sum - (x**c)
print(sum)
c=1
sum=1
for i in range(2,2*n+1,2):
    c=c+1
    fact=1
    for j in range(1,i):
        fact = fact*j
    if(c%2==0):
        sum = sum - (x**i)/fact
    else:
        sum = sum + (x**i)/fact
print(sum)

