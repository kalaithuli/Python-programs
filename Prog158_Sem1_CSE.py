"""n = str(1001)
s = 0
k = 0
for i in range(-1,-len(n)-1,-1):
    s = s + (int(n[i]) * (2 ** k))
    k= k + 1
print(s)
"""
"""negative numbers are stored as 2's complemet 
sign bit = 0 for +ve
sign bit = 1 for - ve
- 13 is represented as 1 1101
steps for 2's complement:
flip the bits(write its complementary)
add 1
Ex : 1 1101 becomes 1 0010 (sign bit remains the same)
add 1 so it becomes 1 0011
"""
"""
n = 125w
while(n!=1):
    if(n%2 != 0):
        print("No")
        break
    n = n // 2
else:
    print("Pw")
"""
"""
n = int(input("Enter a num "))
s = 0
while n>=0:
    n = int(input("Enter a num "))
    if(n<100):
        s = s + n
print(s)
"""
"""k = ord("A")
for i in range(1,10,2):
    for j in range(1,i+1):
        print(chr(k),end ='')
        k = k + 1
    print()"""
n=14
s=0
fo=0
for i in range(1,n+1):
    if n%i==0:
        s=s+1
        if i%2 != 0:
            fo=fo+1
            print(i)
print("factors", s)
