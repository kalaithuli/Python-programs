print("1.Area of circle ")
print("2.Area of rectangle")
print("3.Area of triangle")
a = int(input("Enter your choice "))
if(a == 1):
    r = float(input("Enter the radius of the circle "))
    ar = 3.14 * r ** 2
elif(a == 2):
    l = float(input("Enter the length "))
    b = float(input("Enter the breadth "))
    ar = l * b
else:
    h = float(input("Enter the height "))
    s = float(input("Enter the base "))
    ar = 0.5 * s * h
print("Area = " , ar)
