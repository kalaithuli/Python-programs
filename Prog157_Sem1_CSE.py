'''
n = list(input("Enter the binary number: "))
n.reverse()
s = 0
for i in range(0,len(n)):
    s = s + (int(n[i]) * (2**i))
print(s)
'''

for i in range(1,6):
    n = 0
    for j in range(1,i+1):
        print(j,end="")
    print()
