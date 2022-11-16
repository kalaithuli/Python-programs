#23
a = eval(input("Enter a list "))
c = input("Enter the element to be searched for: ")
b=len(a)
flag = False
for i in range(b):
    if(a[i] == c):
        print("Search element,",c,"is found at ",i)
        flag = True
if(flag == False):
    print("Search element,",c,"is not found")

