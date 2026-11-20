"""
method overloading not posible

note : pythod does not support method overloading concept
"""

class Student:
    def display(self):
        print("this is display 1")

    def display(self,num1):
        self.num1 = num1
obj = Student()
obj.display()            