'''
a = [["pes54uti7",54,53,5,2342],["pes54ufghfgi7",54,53,5,2342],["pes54bdfbbti7",54,53,5,2342],["pesgrdf54uti7",54,53,5,2342]]
d={}
for i in a:
    k=i.pop(0)
    d[k]=sum(i)
print(d)

d=set()
for i in range(1,21):
    if i%4!=0:
        d.add(i)
print(d)

d=""" Sanksrit kalidasa YHK
English murder mystery A.Christie
Kannada Kuvempu TRH
Kannada hrjdbg rghh"""
a=d.split('\n')
result={}
for i in a:
    lang=i.split()[0]
    if lang not in result:
        result[lang]=0
    result[lang]+=1
print(result)

l = [5,4566,4664,467,456,46]
l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(l)

d={}
n=int(input("Enter number: "))
for i in range(1,n+1):
    d[i]=i*i
print(d)
'''
n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
