m = int(input("Enter the start value "))
n = int(input("Enter the stop value "))
primadam = []
freq = 0
if (m<n):
    for i in range(m,n+1):
        flag1 = False
        for j in range(2, i):
            if (i % j == 0):
                 flag1 = True
        if(flag1 == False):
            n = i
            num = 0
            if(n >= 10):
                while (n != 0):
                    d = n % 10
                    num = num * 10 + d
                    n = n // 10
                b = num * num
                num1 = 0
                n1 = b
                # reverse of the reverse num's square
                while (n1 != 0):
                    d = n1 % 10
                    num1 = num1 * 10 + d
                    n1 = n1 // 10
                a = i * i
                n2 = a
                num2 = 0
                # reverse of num's square
                while (n2 != 0):
                    d = n2 % 10
                    num2 = num2 * 10 + d
                    n2 = n2 // 10
                if (a == num1):
                    primadam.append(i)
                    freq = freq + 1
else:
    print("INVALID INPUT ")
print("PRIME - ADAM INTEGERS ARE ")

for k in range(len(primadam)):
     print(primadam[k], end = ' ')
print()
print("FREQUENCY OF PRIME ADAM INTEGERS IS: " , freq)




