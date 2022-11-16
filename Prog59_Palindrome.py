#palindrome if len is > 4
a = input("Enter a string ")
if(len(a)>4):
    for i in range(-1 ,(-len(a)-1),-1):
        print(a[i],end='')

