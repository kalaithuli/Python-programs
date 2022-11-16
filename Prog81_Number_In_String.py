#19
a=input("Enter a string ")
b=len(a)
d=0
sum=0
print("The original string is ",a)
while(b!=0):
    c=a[b-1]
    if(c>='0' and c<='9'):
        d = d+1
        sum = sum+int(c)
        print(c,end=' ')
    b=b-1
if(d!=0):
    print(" are the digits")
    print("The sum is ",sum)
else:
    print("There are no digits")



