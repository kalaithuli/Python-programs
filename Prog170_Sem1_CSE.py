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
