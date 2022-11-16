a = input("Enter the string ")
if(len(a)>= 3):
    if (a.endswith('ing')):
        b = a + 'ly'
    else:
        b = a + 'ing'
    print(b)
else:
    print(a)



