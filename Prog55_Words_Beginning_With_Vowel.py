a = input("Enter a sentence ")
b =' ' + a.strip() + ' '
d = 0
c = 0
while(c != -1):
    c = b.find(' ', d+1)
    if (b[d+1:d+2] in 'AaEeIiOoUu'):
        print(b[d+1:c])
    d = c








