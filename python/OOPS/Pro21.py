class Address:
    def __init__(self,city,state):
        self.city = city
        self.state = state

class Emp:
    def __init__(self,Emp_name,address):
        self.Emp_name = Emp_name
        self.address = address


a1 = Address("Ahmedabad","Gujarat")
e1 = Emp("Kumkum",a1)

print(e1.Emp_name)
print(e1.address.city)