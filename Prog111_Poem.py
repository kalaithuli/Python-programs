# Reading an entire text from file
f1 = open("Poem.txt","r")
str1 = f1.read()
print(str1)
f1.close()

f1 = open("Poem.txt","r")
str1 = f1.readline()
print (str1)
str2 = f1.readline()
print(str2)
str3 = f1.readline()
print(str3)
f1.close()

f1 = open("Poem.txt" , "r")
str1 = ' '
while str1:
    str1 = f1.readline()
    print(str1)
f1.close()

fout = open("Poem2.txt",'w')
str1 = input("Enter a string ")
fout.write(str1)
fout.close()

