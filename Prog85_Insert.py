#24
a = eval(input("Enter a list "))
b = input("Enter the element to be inserted ")
c = int(input("Enter the position to be inserted at "))
a = a+[0]
d = a[c-1]
a[c-1]=b
for i in range(c+1,len(a)-1):
    e=a[i+1]
    a[i+1]=d
    d=e
print(a)

L=eval(input("Enter a list"))
print(L)
e=int(input("Enter element to be inserted"))
pos=int(input("Enter position"))
L.append(' ')
for i in range(len(L)-1,pos-1,-1):
    L[i]=L[i-1]
L[pos-1]=e
print(L)

