import mysql.connector as sqltor
mycon = sqltor.connect(host = 'localhost',user='root',passwd='thuli@4132')
if mycon.is_connected == False:
    print("Error connecting ")
cursor = mycon.cursor()
cursor.execute("create Database Student32")
mycon.commit()
mycon.close()
mycon=sqltor.connect(host='localhost',user='root',passwd='thuli@4132',database='Student32')
if mycon.is_connected == False:
    print("Error connecting ")
cursor = mycon.cursor()
st = "create Table Stud(Slno Integer Primary Key, Dname varchar(100),Age Integer)"
cursor.execute(st)
mycon.commit()
cursor.execute("DESC STUD")
for row in cursor:
    print(row)
mycon.close()


mycon=sqltor.connect(host='localhost',user='root',passwd='thuli@4132',database='Tuteesio')
if mycon.is_connected == False:
    print("Error connecting ")
cursor = mycon.cursor()
cursor.execute("DESC STUD")
for row in cursor:
    print(row)
mycon.close()
