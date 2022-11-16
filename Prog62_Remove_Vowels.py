a = input("Enter a string ")
b = len(a)
c = ''
for i in range(0,b):
    if(a[i] not in 'aAeEiIoOuU'):
        c = c + a[i]
print(c)