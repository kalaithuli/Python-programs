fin = open("Envi.txt",'r')
line = fin.readline()
while line:
    if(line[0] == 'A' or line[0] == 'E'):
        print(line)
        print('*'.join(line))
    line = fin.readline()
fin.close()