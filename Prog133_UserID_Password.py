def check(uid):
    fin = open("Security.txt" , 'r')
    line = fin.readline()
    flag = False
    while line:
        list = line.split()
        if uid in list:
            flag = True
        line = fin.readline()
    if flag == True:
        return 1
    else:
        return 0
ans = 'y'
while ans == 'y':
    fin = open("Security.txt" , 'a')
    uid = input("Enter the User Name: ")
    pw = input("Enter the password: ")
    rec = "User Name: " + uid + "\nPassword: " + pw + "\n"
    exist = check(uid)
    nc = 0
    cc = 0
    if exist == 0:
        if(len(pw)>= 8):
            for i in range(len(pw)):
                if pw[i] in ['1','2','3','4','5','6','7','8','9','0']:
                    nc = nc + 1
                elif pw[i] in ['@','$','%']:
                    cc = cc + 1
            if nc > 0  and cc > 0 :
                fin.write(rec)
                nc = 0
                cc = 0
            else:
                print("Password should contain a digit and a special character ")
                nc = 0
                cc = 0
        else:
            print("Password must be at least 8 characters long ")
    else:
        print("User name already exists ")
    ans = input("Do you want to continue? y or n? ")
