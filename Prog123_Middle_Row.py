import math
a = int(input("Enter the no. of rows and coloumns "))
arr = []
for i in range (a):
    row = []
    for j in range (a):
        e = int(input("Enter the element"))
        row.append(e)
    arr.append(row)

mid = int(math.floor(a/2))
sum = 0
for j in range(a):
    sum = sum + arr[mid][j]
print("Sum of middle row " , mid , ":" , sum)
