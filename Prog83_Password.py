#22
a = input("Enter your password ")
if(a[0]>'0' and a[0]<'9' and len(a)>=6):
    print("Your password is valid and is accepted")
else:
    print("Your password is not valid")
