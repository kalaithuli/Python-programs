n = int(input("Enter a number "))
n1=n
num = 0
while(n != 0) :
    d = n%10
    num = num + d ** 3
    n = n//10
print(num)
if(num == n1):
    print("Armstrong no. ")
else:
    print("Not armstrong no. ")
1