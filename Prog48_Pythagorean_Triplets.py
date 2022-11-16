for i in range (1,101):
    a=i
    for j in range (i,21):
        b=j
        for k in range(j,21):
            c=k
            if (c ** 2 == a ** 2 + b ** 2):
                print(a, b, c)

