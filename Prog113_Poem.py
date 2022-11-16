fin = open("Poem.txt",'r')
fout = open("Poem2.txt",'w')
line = fin.readline()
while line:
    a = len(line)
    str1=''
    for i in range(a):
        if(line[i]==' '):
            if (line[i+1]!=' '):
                str1 = str1 + line[i]
        else:
            str1 = str1+line[i]
    fout.write(str1)
    line = fin.readline()
fin.close()
fout.close()



#Dtrabarbseechompoo
