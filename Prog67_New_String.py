a = input("Enter a string ")
b = len(a)
if(b == 2):
    print(a+a)
elif(b>2):
    print(a[0:2]+a[b-2:b])
else:
    print("Empty String")
