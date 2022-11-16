#25
a = eval(input("Enter a list "))
c = input("Enter the element to be deleted ")
for i in range(len(a)):
    if(a[i]!=c):
        b = i
        for j in range(b,len(a) - 1):
            d = a[j+1]
            a[j] = d
        a[len(a)-1]= ''
print(a)
d={"jan":31,"Feb":28,"March":31,"April":30,"May":31,"June":30}
t=sorted(d.values())
print(t)
for i in range(len(t)):
    if i==len(t)-1:
        break
    elif t[i]==t[i+1]:
        t.remove(t[i])
t.remove(t[len(t)-2])
d1={}
for k in range(len(t)):
    for i,j in d.items():
        if t[k]==j:
            d1[i]=j
print(d1)
