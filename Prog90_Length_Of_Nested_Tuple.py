#27
t=eval(input("Enter a nested tuple "))
b=['']*len(t)
for i in range(len(t)):
    a=t[i]
    b[i]=len(a)
b=tuple(b)
print(b)
