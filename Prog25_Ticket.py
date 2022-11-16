#Travel agency and ticket fares
a = input("Enter you name ")
b = int(input("Enter the ticket amount "))
if(b>=70000) :
    netamt = b - ((18/100)*b)
elif(b>=55001 and b<70000):
    netamt = b - ((16 / 100) * b)
elif(b>=35001 and b<55001):
    netamt = b - ((12 / 100) * b)
elif(b>=25001 and b<35001):
    netamt = b - ((10 / 100) * b)
else :
    netamt = b - ((2 / 100) * b)
print("Name : " + a)
print("Discount : " , (b-netamt))
print("Net Amount : " , netamt)
