class Student:
    def __init__(self):
        marklist1 = []
        name1 = ""
        marklist2 = []
        name2 = ""
        marklist3 = []
        name3 = ""

    def get_data(self):
        self.name1 = input("Enter the name of the student 1 ")
        self.marklist1 = eval(input("Enter marks of student 1 "))
        self.name2 = input("Enter the name of the student 2 ")
        self.marklist2 = eval(input("Enter marks of student 2 "))
        self.name3 = input("Enter the name of the student 3 ")
        self.marklist3 = eval(input("Enter marks of student 3 "))

    def show_data(self):
        print("Name : " , self.name1)
        print("Marks : ",self.marklist1 )
        print("Name : ", self.name2)
        print("Marks : ", self.marklist2)
        print("Name : ", self.name3)
        print("Marks : ", self.marklist3)
    def __del__(self):
        print("Destructor invoked")
obj1 = Student()
obj1.get_data()
obj1.show_data()