import math
n = int(input("Enter the number of sides "))
S = int(input("Enter the length from centre to corner "))
ar = 0.5 * n * math.sin((2*math.pi)/n) * S**2
ar1 = 0.5 * n * math.sin((math.radians(360))/n) * S**2
print("Area of polygon = ",ar)
print("Area of polygon = ",ar1)
