x = int(input("Enter the value of x "))
n = int(input("Enter the value of n "))
k=1
sum = 0
for i in range (1 , 2*n , 2):
    fact = 1
    for j in range (1 , i):
        fact = fact*j
    sum = sum + (x**i/fact)*k
    k = k * (-1)
print(sum)
