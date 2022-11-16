a = eval(input("Enter a list of numbers "))
b = []
i = 0
for a[i] in a:
    if a[i] not in b:
         b.append(a[i])
    i = i+1
print(b)