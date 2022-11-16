#Sum of even and odd numbers seperately
a = int(input("Enter the value of n "))
evesum=0
odsum=0
for i in range(1 , a+1 ):
    if(i%2==0):
        evesum = evesum+i
    else:
        odsum=odsum+i
print("Even sum " , evesum)
print("Odd sum " , odsum)