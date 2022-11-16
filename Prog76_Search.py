a = eval(input("Enter a list of numbers "))
b =int(input("Enter the number to be searched for "))
c= 0
for i in range(0,len(a)):
    if(a[i] == b):
        print ('Index value = ' , i)
        c = c+1
print("Number of times the number occurred = " , c)

