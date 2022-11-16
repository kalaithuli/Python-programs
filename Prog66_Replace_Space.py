a = input("Enter a string ")
b = len(a)
c = a[0]
for i in range(1,b):
    if(a[i] == a[0]):
        c = c + '$'
    else:
        c = c + a[i]
print(c)
