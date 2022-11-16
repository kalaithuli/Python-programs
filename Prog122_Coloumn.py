a = int(input("Enter the no. of rows and coloumns "))
arr = []
for i in range (a):
    row = []
    for j in range (a):
        e = int(input("Enter the element"))
        row.append(e)
    arr.append(row)
sum = 0
for i in range(a):
    for j in range(a):
        sum = sum + arr[j][i]
    print("Sum of coloumn " , i , ":" , sum)
    sum = 0