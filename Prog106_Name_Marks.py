class student:
    def get_data(self):
        self.name=input("Enter name ")
        self.marks=int(input("Enter marks "))
    def show_data(self):
        print(self.name)
        print(self.marks)
obj1 = student()
obj1.get_data()
obj1.show_data()
