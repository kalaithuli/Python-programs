# Determining the roots based on the discriminant
import math
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
d = b**2 - 4*a*c
if (d==0) :
    root = (-b + (d**0.5))/2*a
    print(root)
elif (d>0) :
    root1 = (-b + math.sqrt(d))/2*a
    root2 = (-b - math.sqrt(d))/2*a
    print(root1)
    print(root2)
else :
    x = -b/(2*a)
    y = math.sqrt(math.fabs(d)) / (2*a)
    print(x , ' + i' , y)
