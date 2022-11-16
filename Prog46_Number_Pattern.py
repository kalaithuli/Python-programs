for i in range(5,0,-1):
    for j in range(1,i+1):
        if j == 1:
            print(((5 - i) * ' '),j,end='')
        else:
            print(j,end='')
    print()
