#To find the factorial of any number
n = int(input("Enter the number "))
prod = 1
while(n>=1) :
    prod = prod * n
    if(n != 1):
        print(n , "*" , end=' ')
    else:
        print(n)
    n = n-1
print("Factorial= " , prod)
