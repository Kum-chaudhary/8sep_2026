class Parent:
    def displayA(self):
        print("A class is here")

class Child(Parent):
    def displayB(self):
        print("B class is here")

obj = Child()

obj.displayA()
obj.displayB()
