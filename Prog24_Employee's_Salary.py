#Employee salary
 a = input("Enter the name of the employee ")
b = int(input("Enter the basic pay "))
if(b>= 45000) :
    da = (40/100)*b
    hra = (30/100)*b
elif(b>=30000 and b<45000) :
    da = (40 / 100) * b
    hra = (25 / 100) * b
elif(b>=15000 and b<=30000):
    da = (30 / 100) * b
    hra = (20 / 100) * b
else :
    da = (30 / 100) * b
    hra = (15 / 100) * b
total = b + da + hra
if(total > 100000):
    total = total - ((30/100)*b)
print("Employee name " + a)
print("Basic pay " , b)
print("Dearance allowance " , da)
print("House Rent Allowance " , hra)
print("Total salary " , total)