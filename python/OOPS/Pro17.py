from abc import ABC,abstractmethod

class Vehicles(ABC):
    def wheels(self):
        print("Wheecles has 4 wheels")

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def model(self):
        pass

class car(Vehicles):
    def engine(self):
        print("car engine : petrol")

    def model(self):
        print("Car model : BMW")

obj = car()
obj.wheels()
obj.engine()
obj.model()                            