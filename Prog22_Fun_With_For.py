#Even numbers between 100 and 200
for i in range(100 , 201 , 2) :
    print(i , end =' ')
print()
#Numbers in descending order from 10 to 1
for j in range (10 , 0 , -1) :
    print(j , end =' ')
print()
#Squares of numbers from 1 to 10
for k in range (1 , 11 ) :
    print(k**2 , end =' ')
print()
#Just a random series
for l in range(1 , 41 , 3) :
    if(l%2 == 0):
        print(-l,end=' ')
    else :
        print(l , end =' ')
print()
#Sum of even numbers
sum=0
for m in range(1 , 5 , 2) :
    sum=sum+m
print(sum)