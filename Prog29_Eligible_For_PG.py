#Are you eligible for Post Graduation?
a = float(input("Enter X examination marks : "))
b = float(input("Enter XII examination marks : "))
c = float(input("Enter graduation marks : "))
d = input("Enter the course opted for graduation ")
e = input("Enter the course opted for PG ")
if(d == e):
    if(a>=80 and b>=80 and (c-5)>=70):
        print("Eligible for PG")
    else:
        print("Not eligible for PG")
else:
    if (a >= 80 and b >= 80 and c>= 70):
        print("Eligible for PG")
    else:
        print("Not eligible for PG")
