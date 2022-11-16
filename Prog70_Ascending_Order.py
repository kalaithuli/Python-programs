a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
d , e , f = 0 , 0 , 0
if (a<b and a<c):
    if(b<c):
        d , e , f = a , b , c
    else:
        d , e , f = a , c , b
if (b<a and b<c):
    if(a<c):
        d , e , f = b , a , c
    else:
        d , e , f = b , c , a
if (c<b and c<a):
    if(b<a):
        d , e , f = c , b , a
    else:
        d , e , f = c , a , b
print(d,e,f)