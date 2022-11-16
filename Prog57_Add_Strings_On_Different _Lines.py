e = int(input("Enter the number of lines "))
a=''
for j in range(0,e):
    a= a + input()+'\n'
b = len(a)
c = ''
for i in range(0,b):
    if(a[i] != '\n'):
        c = c + a[i]
print(c)


