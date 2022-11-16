a = input("Enter a string ").strip()
b = ' ' + a
flag = True
d = -1
while(flag == True):
    c = b.find(' ',d+1)
    if(b.find(' ' , c+1) != -1):
        print(b[c+1].capitalize() , end =' ')
    else :
        print(b[c+1:len(b)].capitalize())
        flag = False
    d = c



