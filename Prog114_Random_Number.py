import random
import math
def randomnum(x):
   num = 0
   for i in range (x):
       num = (num*10)+random.randint(1,9)
   print("The required number is ",num)

def polygon(a,b):
    ar = 0.5 * a * math.sin((math.radians(360)) / a) * b ** 2
    print("Area of polygon = ", ar)

print("1) Random number ")
print("2) Area of polygon ")
ch = int(input("Enter your choice "))
if (ch == 1):
    n = int(input("Enter the number of digits "))
    randomnum(n)
else:
    n = int(input("Enter the number of sides "))
    s = int(input("Enter the length from centre to corner "))
    polygon(n,s)
