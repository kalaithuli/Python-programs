# recursion
'''def length(x):
    if x == "":
        return 0
    else:
        return (1+length(x[1:]))
a = input()
b = length(a)
print(b)

def sum(x):
    if x!=0:
        return x + sum(x-1)
    else:
        return 0
a = int(input("Enter num: "))
b = sum(a)
print(b)'''

def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
a=int(input("enter num: "))
for i in range(a):
    print(fib(i))





