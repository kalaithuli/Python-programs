a = eval(input("Enter a list of numbers "))
se = 0
so = 0
for i in range(0,len(a)):
    if(i%2 == 0):
        se = se + a[i]
    else:
        so = so + a[i]
print(se-so)
