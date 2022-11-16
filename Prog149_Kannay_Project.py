import mysql.connector
# GLOBAL VARIABLES DECLARATION
myConnnection =""
cursor=""
userName=""
password =""
pcode=""
#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():
    global myConnection
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")

myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password , auth_plugin='mysql_native_password' )
if myConnection:
    print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
    cursor=myConnection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS EMIRATESI")
    cursor.execute("COMMIT")
    cursor.close()
    return myConnection
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection ():
    global userName
    global password
    global myConnection
    global cid
    global pcode
    myConnection = mysql.connector.connect(host="localhost", user=userName, passwd = password, database = "EMIRATESI",
                                   auth_plugin = 'mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()

#MODULE FOR MEN'S SECTION
def menSection():
    global pcode
    if myConnection:
        cursor = myConnection.cursor()
        print("ITEMS UNDER THE MENS SECTION ARE : ")
        sql = "SELECT * FROM PRODUCT WHERE PRODUCT_CATEGORY = % s"
        cursor.execute(sql, ("Men",))
        data = cursor.fetchall()
        if data:
            print(data)

while True:
    print(""" ENTER 1 TO BUY ENTER 0 TO RETURN TO MAIN MENU """)
    choice = int(input("Please Enter Your Choice : "))
    if choice == 1:
        item = searchItem()
        if item:
            cursor = myConnection.cursor()
            createTable = """ CREATE TABLE IF NOT EXISTS
                    BILL(BILL_CODE VARCHAR(10) PRIMARY KEY ,
                    PRODUCT_CODE VARCHAR(10),
                    CID VARCHAR(10),
                    CNAME VARCHAR(30),
                    PRICE INT,
                    QUANTITY INT ,
                    DISCOUNT INT ,TOTAL INT ); """
            cursor.execute(createTable)
            bnumber = input("\n Enter BILL Number : ")
            cid = input("\n Enter Customer Identification No. : ")
            cname = input("\n Enter Customer Name : ")
            price = int(input("\n Enter Price : "))
            quantity = int(input("\n Enter Quantity : "))
            discount = int(input("\n Enter Discount Amount, If any: "))
            total = (price * quantity) - discount
            sql = "INSERT INTO BILL VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (bnumber, cid, pcode, cname, price, quantity, discount, total)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\n ITEM ADDEDD SUCCESSSFULLY IN YOUR CART !")
            cursor.close()
        elif choice == 0:
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

# MODULE FOR WOMEN'S SECTION
def womenSection():
    global pcode
    if myConnection:
            cursor = myConnection.cursor()
            print("ITEMS UNDER THE WOMEN SECTION ARE : ")
            sql = "SELECT * FROM PRODUCT WHERE PRODUCT_CATEGORY = % s"
            cursor.execute(sql, ("Women",))
            data = cursor.fetchall()
            if data:
                print(data)
            while True:
                print("""ENTER 1 TO BUY ENTER 0 TO RETURN TO MAIN MENU """)
                choice = int(input("Please Enter Your Choice : "))
                if choice == 1:
                    item = searchItem()
                    if item:
                        cursor = myConnection.cursor()
                        createTable = """CREATE TABLE IF NOT EXISTS
                        BILL(BILL_CODE VARCHAR(10) PRIMARY KEY ,
                        PRODUCT_CODE VARCHAR(10),
                        CID VARCHAR(10),
                        CNAME VARCHAR(30),
                        PRICE INT,
                        QUANTITY INT ,
                        DISCOUNT INT ,
                        TOTAL INT );"""
                        cursor.execute(createTable)
                        bnumber = input("\n Enter BILL Number : ")
                        cid = input("\n Enter Customer Identification No. : ")
                        cname = input("\n Enter Customer Name : ")
                        price = int(input("\n Enter Price : "))
                        quantity = int(input("\n Enter Quantity : "))
                        discount = int(input("\n Enter Discount Amount, If any: "))
                        total = (price * quantity) - discount
                        sql = "INSERT INTO BILL VALUES( % s, % s, % s, % s, % s, % s, % s, % s)"
                        values =(bnumber, cid, pcode, cname, price, quantity, discount, total)
                        cursor.execute(sql, values)
                        cursor.execute("COMMIT")
                        print("\n ITEM ADDEDD SUCCESSSFULLY IN YOUR CART !")
                        cursor.close()
                    elif choice == 0:
                        break;
                    else:
                        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                else:
                    print("\nSomthing Went Wrong ,Please Try Again !")
# MODULE FOR KIDS'S SECTION
def kidsSection():
    global pcode
    if myConnection:
        cursor = myConnection.cursor()
        print("ITEMS UNDER THE KIDS SECTION ARE : ")
        sql = "SELECT * FROM PRODUCT WHERE PRODUCT_CATEGORY = % s"
        cursor.execute(sql, ("Kids",))
        data = cursor.fetchall()
        if data:
            print(data)
        while True:
            print(""" ENTER 1 TO BUY
            ENTER 0 TO RETURN TO MAIN MENU
            """)
            choice = int(input("Please Enter Your Choice : "))
            if choice == 1:
                item = searchItem()
                if item:
                    cursor = myConnection.cursor()
                    createTable = """CREATE TABLE IF NOT EXISTS
                                    BILL(BILL_CODE VARCHAR(10) PRIMARY KEY ,
                                    PRODUCT_CODE VARCHAR(10),
                                    CID VARCHAR(10),
                                    CNAME VARCHAR(30), 
                                    PRICE INT,
                                    QUANTITY INT ,
                                    DISCOUNT INT ,            
                                    TOTAL INT );"""
                    cursor.execute(createTable)
                    bnumber = input("\n Enter BILL Number : ")
                    cid = input("\n Enter Customer Identification No. : ")
                    cname = input("\n Enter Customer Name : ")
                    price = int(input("\n Enter Price : "))
                    quantity = int(input("\n Enter Quantity : "))
                    discount = int(input("\n Enter Discount Amount, If any: "))
                    total = (price * quantity) - discount
                    sql = "INSERT INTO BILL VALUES( % s, % s, % s, % s, % s, % s, % s, % s)"
                    values = (bnumber, cid, pcode, cname, price, quantity, discount, total)
                    cursor.execute(sql, values)
                    cursor.execute("COMMIT")
                    print("\n ITEM ADDEDD SUCCESSSFULLY IN YOUR CART !")
                    cursor.close()
                elif choice == 0:
                    break;
                else:
                    print("Sorry ,May Be You Are Giving Me Wrong Input,Please Try Again !!! ")
            else:
                print("\nSomthing Went Wrong ,Please Try Again !")

# MODULE FOR ADDING NEW ITEM
def addItem():
    global pcode
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS PRODUCT
        (PRODUCT_CODE VARCHAR(10) PRIMARY KEY,
        PRODUCT_CATEGORY VARCHAR(20),
        PRODUCT_BRAND VARCHAR(30) ,
        PRODUCT_NAME VARCHAR(30))"""
        cursor.execute(createTable)
        pcode = input("\nEnter Product Code : ")
        pcategory = input("\nEnter Product Category [MEN / WOMEN / KIDS]: ")
        pbrand = input("\nEnter Brand Name : ")
        pname = input("\nEnter Product Name : ")
        sql = "INSERT INTO PRODUCT VALUES(%s,%s,%s,%s)"
        values = (pcode, pcategory, pbrand, pname)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\nNEW ITEM ADDEDD SUCCESSSFULLY !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

# MODULE FOR SEARCH AN ITEM
def searchItem():
    global pcode
    if myConnection:
        cursor = myConnection.cursor()
        pcode = input("PLEASE ENTER PRODUCT CODE : ")
        sql = "SELECT * FROM PRODUCT WHERE PRODUCT_CODE=% s"
        cursor.execute(sql, (pcode,))
        data = cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            return False
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

# MODULE FOR MODIFY AN ITEM
def modifyItem():
    global pcode
    item = searchItem()
    if item:
        if myConnection:
            cursor = myConnection.cursor()
            print("PRESS 1 FOR PRODUCT NAME : ")
            print("PRESS 2 FOR PRODUCT CATEGORY : ")
            print("PRESS 3 FOR PRODUCT BRAND : ")
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                name = input("ENTER NEW PRODUCT NAME : ")
                sql = "UPDATE PRODUCT SET PRODUCT_NAME= %s WHERE PRODUCT_CODE = % s"
                cursor.execute(sql, (name, pcode))
                cursor.execute("COMMIT")
                print("PRODUCT NAME UPDATED SUCCESSFULLY ")
            elif choice == 2:
                category = input("ENTER NEW CATEGORY :")
                sql = "UPDATE PRODUCT SET PRODUCT_CATEGORY= %s WHERE PRODUCT_CODE = % s"
                cursor.execute(sql, (category, pcode))
                cursor.execute("COMMIT")
                print("PRODUCT CATEGORY UPDATED SUCCESSFULLY ")
            elif choice == 3:
                brand = input("ENTER NEW BRAND NAME :")
                sql = "UPDATE PRODUCT SET PRODUCT_BRAND= %s WHERE PRODUCT_CODE = % s"
                cursor.execute(sql, (brand, pcode))
                cursor.execute("COMMIT")
                print("BARND UPDATED SUCCESSFULLY ")
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
        else:
            print("\nSomthing Went Wrong ,Please Try Again !")
    else:
        print("Item Record Not Found , Please Try Again !")

# MODULE FOR DISPLAY INVENTORY
def showInventory():
    if myConnection:
        cursor = myConnection.cursor()
        sql = "SELECT * FROM PRODUCT GROUP BY PRODUCT_CATEGORY "
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            return False
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

# MODULE TO REMOVE AN ITEM
def removeItem():
    global pcode
    item = searchItem()
    if item:
        if myConnection:
            cursor = myConnection.cursor()
            sql = "SELECT * FROM PRODUCT WHERE PRODUCT_CODE=% s"
            cursor.execute(sql, (pcode,))
            data = cursor.fetchall()
            if data:
                print("\n** Item Removed Successfully !!! ***")
                sql = "DELETE FROM PRODUCT WHERE PRODUCT_CODE=%s"
                cursor.execute(sql, (pcode,))
                cursor.execute("COMMIT")
                cursor.close()
            else:
                print("\nSomthing Went Wrong ,Please Try Again !")
        else:
            print("Record Not Found , Please Try Again !")

# MODULE TO LIST ALL BILLS
def allBills():
    if myConnection:
        cursor = myConnection.cursor()
        sql = "SELECT * FROM BILL GROUP BY CID"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            for bill in data:
                print(bill)
            return True
        else:
            return False
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

# MODULE TO GENERATE PARTICULAR CUSTOMER'S BILL
def generateBill():
    global pcode
    if myConnection:
        cursor = myConnection.cursor()
        cid = input("\nEnter Customer Identification No. : ")
        sql = "SELECT CNAME , SUM(TOTAL) AS 'TOTAL AMOUNT' FROM BILL GROUP BY % s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        if data:
            print("###################################")
            print("NAME AMOUNT")
            print(data)
            return True
        else:
            print("\nCustomer Not Found !")
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

# MAIN SCREEN OF THE SOFTWARE
print("#******KENDRIYA VIDYALAYA PALAMPUR ****")
print("#******WELCOME TO THE MALL OF EMIRATES*")
print("################## THE MALL OF EMIRATESI ##########")
print("#***Designed and Maintained By:")
print("#***AANCHAL - CLASS XII A - ROLL NO - 4 [ 2019-2020]")
print("#***ARSI - CLASS XII A - ROLL NO - 6 [ 2019-2020 ]")
print("#***RITIKA - CLASS XII A - ROLL NO - 18 [ 2019-2020 ]")
print("#***SHAMBHVI - CLASS XII A - ROLL NO - 21 [ 2019-2020]")
print("*******PROUD TO BE KAVIAN *****")
# MYSQL CONNECTION CHECK
myConnection = MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection()
    while (True):
        print("""
             1---->FOR NEW ITEM
             2---->FOR WOMEN SECTION
             3---->FOR MEN SECTION
             4---->FOR KID SECTION
             5---->FOR MODIFY ITEM
             6---->FOR SEARCH ITEM
             7---->FOR SHOW ALL INVENTORY ITEM WISE
             8---->FOR REMOVE ITEM
             9---->LIST ALL BILLS
             10--->GENERATE CUSTOMER BILL
             11--->EXIT""")
        choice = int(input("Please Enter Your Choice : "))
        if choice == 1:
            addItem()
        elif choice == 2:
            womenSection()
        elif choice == 3:
            menSection()
        elif choice == 4:
            kidsSection()
        elif choice == 5:
            modifyItem()
        elif choice == 6:
            item = searchItem()
            if item:
                print("**Record Found !!!**")
            else:
                print("Record Not Found , Please Try Again !")
        elif choice == 7:
            showInventory()
        elif choice == 8:
            removeItem()
        elif choice == 9:
            allBills()
        elif choice == 10:
            generateBill()
        elif choice == 11:
            print("Thanks for visitng THE MALL OF EMIRATESI \n * We are eagerly waititng for your next visit !!! ** ")
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print(" \n ERROR ESTABLISHING MYSQL CONNECTION !")
# END OF THE PROJECT