L = eval(input("Enter a list of numbers "))
s = 0
L2= []
for i in range(0,len(L)):
    s = s+L[i]
    L2.append(s)
for j in range(0, len(L2)):
    print(L2[j], end=' ')


