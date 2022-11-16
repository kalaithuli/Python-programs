#26
L = eval(input("Enter the list L "))
M = eval(input("Enter the list M "))
a = len(L)
N = ['']*a
for i in range(a):
    N[i]=L[i]+M[i]
print("The new list N =", N)
