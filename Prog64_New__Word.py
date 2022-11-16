a = input("Enter a string ")
b = len(a)
c = ''
for i in range(0,b):
    if(i%2 == 0):
        c = c + a[i]
print(c)
