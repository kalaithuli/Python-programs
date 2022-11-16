n = int(input("Enter a number "))
num = 0
while(n != 0) :
    d = n%10
    num = num * 10 +d
    n = n//10
print(num)