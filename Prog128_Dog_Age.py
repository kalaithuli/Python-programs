age = int(input("Enter the Chihuahua's age "))
name = input("Enter its name ")
if(age <= 256):
    hage = 2*10 + (age-2)*4
    print(name + " is " , hage , " human years old")
else :
    print("Invalid age ")