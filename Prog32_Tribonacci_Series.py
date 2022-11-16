#To print the tribonacci series
n = int(input("Enter the values of n "))
a = 0
b = 1
c = 1
print(a , b , c , end =' ' )
for i in range(4,n+1) :
    d = a+b+c
    print(d,end = ' ')
    a = b
    b = c
    c = d