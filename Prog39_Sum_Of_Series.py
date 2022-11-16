x = int(input("Enter the value of x "))
n = int(input("Enter the value of n "))
fact = 1
sumser = 0
for i in range (1 , n+1):
    for j in range(1 , i+1):
        fact = fact * j
    sumser = sumser +  (x/fact)
    fact = 1
print("Sum of series = " , sumser)