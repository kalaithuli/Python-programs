#28
tup1 = eval(input("Enter a nested tuple "))
sum=0
sum1=0
for i in range(len(tup1)):
    a = [tup1[i]]
    for j in range(len(a[0])):
        sum=sum+a[0][j]
    mn=sum/len(a[0])
    print("Mean element",i,":",mn)
    sum1=sum1+mn
    sum = 0
    mn=0
print("Mean of means :",sum1/len(tup1))

