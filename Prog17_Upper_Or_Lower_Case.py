#Capital letters or small letters
a = input("Enter the alphabet ")
if(a>='A' and a<='Z'):
    print("Capital letter_Upper case")
elif(a>='a' and a<='z'):
    print("Small letter_Lower case")
else:
    print("Sorry, it is not an alphabet")

a = input("Enter the character ")
if(a>='A' and a<='Z'):
    print("Upper case")
elif(a>='a' and a<='z'):
    print("Lower case")
elif(a>='0'):
    print("Digit")

sum = 0
for i in range(2,41,2):
    sum = sum + i
    print(i , end = ' ')
print()
print("Sum = " , sum)