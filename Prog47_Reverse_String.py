S = input("Enter a string ")
L = len(S)
for i in range(L-1 , -1 , -1):
    print(S[i] , end='')
    