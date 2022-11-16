N = int(input("Enter the number of planets "))
hgt=[]
time=[]
g = []
gr = 0
for i in range(N):
    h,t = map(float, input("Enter the height of the tree and time taken for the apple to fall ").split())
    hgt.append(h)
    time.append(t)
for j in range(N):
    gr = (2 * hgt[j])/t**2
    g.append(gr)
maxg = max(g)
maxindex = g.index(maxg)
print("Planet number ",maxindex+1, "has the maximum gravity")

