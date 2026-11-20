# overridding 
class Parent:
    def __init__(self):
        print("parent contructor is here...")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("This is child constructor is here...")

obj = Child()