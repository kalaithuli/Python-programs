n = int(input("Enter a number "))
n1 = n
am = 0
while(n != 0):
    d = n%10
    am = am * 10 + d
    n = n//10
if(am == n1) :
    print("Palindrome number ")
else :
    print("Not a palindrome number ")

