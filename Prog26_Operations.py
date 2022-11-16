#Operations using desired operands and operators
a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = input("Enter the operator ")
if(c == '+'):
    d = a+b
elif(c == '-'):
    d = a-b
elif(c == '*'):
    d = a*b
elif(c == '/'):
    d = a/b
print("The operator is " + c)
print("Computed result " , d)