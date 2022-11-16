i = ord('A')
for j in range(1,10,2):
    for k in range(1,j+1):
        print(chr(i),end='')
        i+=1
    print()

a=int(input("Enter a no."))
sn=0
sp=0
while(a!=0):
    if (a<0) :
        sn = sn + 1
    else:
        sp = sp + 1
print("Positive num " , sp)
print("Negative num " , sn)