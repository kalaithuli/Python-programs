class Rectangle:
    def get_data(self):
        self.length=int(input("Enter the length "))
        self.breadth=int(input("Enter the breadth "))
    def show_data(self):
        print("Length= " , self.length)
        print("Breadth= " , self.breadth)
        print("Area= " , self.length * self.breadth)
obj1 = Rectangle()
obj1.get_data()
obj1.show_data()
