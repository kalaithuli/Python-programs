#Parking charges of a vehicle
a = input("Enter vehicle number ")
b = float(input("Enter the number of hours the vehicle is parked "))
if(b <= 1) :
    fee = 3
else :
    fee = 3 + ((b-1) * 1.50)
print("Parking charge for vehicle number " + a + " is " , fee)

