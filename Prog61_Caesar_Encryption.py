a = input("Enter a string ")
b = ''
for i in range(0,len(a)):
    c = a[i]
    b = b + chr(ord(c)-3)
print('Caesar encryption : ' + b)

