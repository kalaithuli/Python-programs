# DD / MM / YY / MM / SS
yrs = float(input("How many years? "))
dys = yrs * 365
hrs = dys * 24
mins = hrs * 60
secs = mins * 60
print(yrs , " Years is :")
print(dys , " Days")
print(hrs , " Hours")
print(mins , " Minutes")
print(secs , " Seconds")

dys = int(input("How many days? "))
yrs = dys // 365
dys = dys % 365
mnth = dys // 30
dys = dys % 30
print(yrs , " Years ")
print(mnth , " Months ")
print(dys , " Days ")