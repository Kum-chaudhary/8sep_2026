class Vehicle:
    def setVehicle(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def getVehicle(self):
        print("Color:", self.color)
        print("Wheels:", self.wheels)


class Car(Vehicle):
    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        print("Brand:", self.brand)


class ElectricCar(Car):
    def showDetails(self):
        self.getVehicle()
        self.getBrand()


obj = ElectricCar()

obj.setVehicle("Black", 4)
obj.setBrand("Tesla")

obj.showDetails()