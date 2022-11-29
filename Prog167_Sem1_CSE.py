import random
a = open("File.txt","r")
b = a.read().split()
print(len(b))
a.close()
n = input("Enter a word ")
a = open("File.txt","r")
b = a.read().split()
print(b.count(n))
a.close()
a = open("File.txt","r")
b = a.readlines()
print(random.choice(b))
a.close()
a = open("File.txt","r")
b = a.read().split()
max = b[0]
for i in b:
    if(len(i)>len(max)):
        max = i
print("Longest word is ",max)
a.close()
a = open("File.txt","r")
b = a.read().split()
b.reverse()
print(b)
