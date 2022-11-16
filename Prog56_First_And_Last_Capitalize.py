a = input("Enter a sentence ")
b = ' ' + a.strip() + ' '
d = 0
c = 0
while(c != -1):
    d = c
    c = b.find(' ', d+1)
    e = b[d+1:c-1].capitalize() + b[c-1].capitalize()
    print(e, end=' ')

