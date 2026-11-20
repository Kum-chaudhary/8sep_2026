class Parent:
    def display(self):
        print("this is parent class method")

class Child(Parent):
    def display(self):
        Parent.display(self)
        print("This is child class method")

obj = Child()
obj.display()                