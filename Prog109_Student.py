class Student:
    def get_data(self):
        self.name = input("Enter the name of the student ")
        self.rno = int(input("Enter the roll number "))
        self.mark1 = int(input("Enter mark of subject 1 "))
        self.mark2 = int(input("Enter mark of subject 2 "))
        self.mark3 = int(input("Enter mark of subject 3 "))
    def calc_total(self):
        self.total = self.mark1 + self.mark2 + self.mark3
    def show_data(self):
        print("Name : " , self.name)
        print("Roll Number : ",self.rno)
        print("Total marks : ",self.total)
    def __del__(self):
        print("Destructor invoked")
obj1 = Student()
obj1.get_data()
obj1.calc_total()
obj1.show_data()
