'''
marks = [95,80,99,60,81]
names = ["Rita","Tina","Zara","Timothy","Ana"]
def tup(mark,name):
    a = max(mark)
    b = name[mark.index(a)]
    return a,b
c = tup(marks,names)
print(c)
'''
'''
a = {1:"abc",2:"abc",4:"dfg",3:"dfga"}
b = {}
def dict(a,b):
    for i in a.keys():
        c = a[i]
        if c not in b:
            b[c]=[i]
        else:
            b[c].append(i)
    print(b)
dict(a,b)

a = "abcdz"
b =""
for i in a:
    if i!= "z":
        b = b + chr(ord(i)+1)
    if i == "z":
        b = b + "a"
print(b)
'''
'''

def display(l):
    print("Length of file is" , l)

def fnlen(path,call):
    f = open(path,"r")
    b = f.read()
    call(len(b))

fnlen("Text File.txt",display)'''
'''
def counter(count = 0):
    def inc():
        nonlocal count
        count =count + 5
        return count # returns to a() when invoked - n holds the returned value
    return inc #returns to counter() when invoked - a is now the reference to the
a = counter()
n=int(input("N Number of times:"))
for i in range(n):
    n = a()
    print(n)
    
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def Remember(f):
    memo = {}
    def Recollect(n):
        print(memo)
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return Recollect
fib = Remember(fib)
n=int(input("enter a number:"))
print(fib(n))