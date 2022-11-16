fin = open("Envi.txt",'r')
line = fin.readline()
c = 0
while line:
    line1 = line.split()
    n = len(line1)
    for i in range(0,n):
        if(line1[i][0].isupper()):
            c = c+1
    line = fin.readline()
print("Count = " , c)
fin.close()
