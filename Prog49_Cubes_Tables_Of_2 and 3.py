n = int(input("Enter the number of terms "))
for i in range(1,n+1):
    print(i**3 , end=' ')
print()
j=0
for i in range(1,n+1):
    j=j+3
    print(j , end=' ')
print()
j=0
for i in range(1,n):
    j=j-2
    print(j , end =' ')

