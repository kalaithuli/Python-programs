a = int(input("Enter the no. of rows and coloumns "))
arr = []
for i in range (a):
    row = []
    for j in range (a):
        e = int(input("Enter the element"))
        row.append(e)
    arr.append(row)
#Diagonal1
for i in range(a):
    print(arr[i][i] , end=' ')
print()
#Diagonal2
for j in range(a):
    print(arr[a-j-1][a-j-1] , end=' ')
