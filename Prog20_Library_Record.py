#Library record with the rental charges of the book and late fee

a = int(input("Enter the cost price of the book "))
b = int(input("Enter the number of days book is borrowed for "))
if(b <= 5) :
    fee = (1/100) * a * 5
elif(b>5 and b<=10) :
    fee = (1/100) * a * 5 + (1*(b-5))
elif(b>10 and b<=15) :
    fee = (1 / 100) * a * 5 + (1 * (b - 5)) + (3.5 * (b-10))
else :
    fee = (1/100) * a * 5 + (1*(b-5)) + + (3.5 * (b-10)) + (5.5 * (b-15))
print("Fee to be paid " , fee)
