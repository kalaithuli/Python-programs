import random
ans = 'y'
dice =[]
while(ans == 'y'):
    num = random.randint(1,6)
    print(num)
    dice.append(num)
    ans =  input("Do you want to continue? y or n? ")
for i in range(1,7):
    print("Frequency of ", i , "is " , dice.count(i))

