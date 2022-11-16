a = int(input("Enter the number of rows and column "))
L = []
for i in range(a):
    row = []
    for j in range(a):
        b = int(input("Enter the element "))
        row.append(b)
    L.append(row)
for i in range(a):
    print(L[i][i] , end=' ')
print()
for j in range(a):
    print(L[a-j-1][a-j-1] , end=' ')