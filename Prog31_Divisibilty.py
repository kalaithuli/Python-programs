#Checking the divisibility of a number and checking if its even or odd
n = int(input("Enter the value of n"))
m = int(input("Enter the value of m"))
for i in range(1 , n+1):
    if(i%m == 0):
        if(i%2 == 0):
            print(i , " is even")
        else:
            print(i, " is odd")




