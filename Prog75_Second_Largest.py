L = eval(input("Enter a list of numbers "))
L1 = sorted(L)
print("The second largest number is " , L1[1])
l = len(L1)
range = L1[l-1] - L1[0]
print("Range= " , range)
