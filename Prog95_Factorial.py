def fact_num(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
n = int(input("Enter a number "))
print(fact_num(n))