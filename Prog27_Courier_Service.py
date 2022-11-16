#Courier service charges
a = input("Enter the customer's name :")
b = float(input("Enter the weight of the parcel "))
if(b<=10):
    c = b*25
elif(b>10 and b<=30):
    c = 10 * 25 + (b-10)*20
else :
    c = 10 * 25 + 20 * 20 + (b-30)*10
print("Customer name : " + a)
print("Weight of the parcel : " , b)
print("Total bill : " , c)
