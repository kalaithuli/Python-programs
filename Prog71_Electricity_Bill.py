cn = input("Enter the customer number ")
u = int(input("Enter the number of units consumed "))
if(u<=100):
    amt = u * 3 + 50
elif(u>100 and u<=300):
    amt = 100 * 3 + (u-100)*5 + 50
else :
    amt = 100 * 3 + 200 * 5 + (u-300) * 7 + 50
print("The electricity bill for customer number " , cn , " is " , amt)
