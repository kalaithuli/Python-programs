n = 4
j = n-1
print(' '*n + '  * ')
for i in range(1,2*n):
    if(i>n):
        print(' '*(i-n) + ' * ' + ' '*(2*j-1)+' * ')
        j=j-1
    else:
        print(' '*(n-i) + ' * ' + ' '*(2*i-1)+' * ')
if(n>1):
    print(' '*n + '  * ')

n=7
k=(n//2)*2
for i in range(0,n,2):
    for j in range(0,k+1):
        print(end=' ')
    for j in range(0,i+1):
        print('* ' , end ='')
    k=k-2
    print()
k=1
for i in range(n-1,0,-2):
    for j in range(0,k+2):
        print(end=' ')
    for j in range(0,i-1):
        print('* ' , end ='')
    k=k+2
    print()

n=4
s = n*2 -1
for i in range(1,n+1):
    for j in range(0,s):
        print(end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    for j in range(2,i+1):
        print(j,end=' ')
    s=s-2
    print()

n=5
s=0
for i in range(n,0,-1):
    for j in range(1,s+1):
        print(end=' ')
    for j in range(1,i+1):
        print('$' , end=' ')
    s=s+2
    print()

for i in range(1,6):
    for j in range(1,i+1):
        if(j%2==0):
            print('#' , end=' ')
        else:
            print('*', end=' ')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        if j == 1:
            print(((5 - i) * ' '),'#',end='')
        else:
            print('#',end='')
    print()
