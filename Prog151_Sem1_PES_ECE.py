import math
a = int(input("Enter the number "))
b = 0
print(a%10 , (a%100)//10 ,a//100)
print ("Sum of digits = " , a%10 + (a//100)%10 + a//100)

# basic sal 25000 , 200 fr every cam , comm 12%

bas = int(input("Enter the price of the camera: "))
no = int(input("Enter the number of cameras sold: "))
tot = 25000 + (200 * no) + (0.12 * bas * no)
print("Total salary = ",tot)

#

r = int(input("Enter the radius "))
ar = 3.14 * r * r
print("Area of the circle is " , ar)
print("Perimeter: " , 2 * 3.14 * r)
a = int(input("Enter the side 1: "))
b = int(input("Enter the side 2: "))
c = int(input("Enter the side 3: "))
s = (a+b+c)/2
area = math.sqrt (s * (s-a) * (s-b) * (s-c))
print("Area = " , area)

#

f =int(input("Enter the length in feet: "))
print("Length in centimetre is " , f*30.48 , "cm")

#

m1 = int(input("Enter the mark 1: "))
m2 = int(input("Enter the mark 2: "))
m3 = int(input("Enter the mark 3: "))
m4 = int(input("Enter the mark 4: "))
m5 = int(input("Enter the mark 5: "))
p = ((m1 + m2 + m3 + m4 + m5)/5) * 100
if(p>=90.0) :
    print("O")
elif(p>=80.0 and p<90.0) :
    print("A")
elif(p>=70.0 and p<=80.0) :
    print("B")
elif(p>=60.0 and p<=70.0) :
    print("C")
else :
    print("D")