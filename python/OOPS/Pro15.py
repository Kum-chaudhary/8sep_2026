from abc import ABC,abstractmethod

class Sample(ABC):
    @abstractmethod
    def display(self):
        pass

class Child(Sample):
    def display(self):
        print("use properties child")

obj = Child()
obj.display()        
