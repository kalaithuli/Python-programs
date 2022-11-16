"""n=13
s=""
while n>=1:
    k = n%2
    n = n//2
    s=s + str(k)

print(s)"""
import datetime as f
"""# input 4 char str n convert the char to its next alphabet
a = input("Enter a 4 character string ")
b=''
if len(a)==4:
    for i in a:
        b = b + chr(ord(i)+1)
    print(b)
else:
    print("Enter a 4 character string only")

#convert to upper case n print unicode
a = input("Enter a 4 character string ")
if len(a)==4:
    for i in a:
        print(i , ord(i))
    b = a.upper()
    print(b)
else:
    print("Enter a 4 character string only")
"""

by=int(input("Enter the year"))
bm=int(input("Enter the month"))
bd=int(input("Enter the date"))
bday = f.date(by,bm,bd)
tdy = f.date.today()
print((tdy-bday).days)
print((tdy-bday).days * 24 * 3600)
#wap to read dob as input n find age in days n seconds
#find on which weekday india became independant
#count no. of days until today from beginning of this year
#area of triangle given 2 sides n included angle
#to select a random value from list


# *********** random.shuffle() ************ random.sample(a,n)"""