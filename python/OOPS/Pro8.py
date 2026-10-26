class Amount:
    def setAmount(self,amount):
        self.amount = amount

    def getAmount(self):
        return self.amount 

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name 

obj = Amount()

name = input("Enter Your Name:")
amount = int(input("Enter Amount:"))

obj.setName(name)
obj.setAmount(amount)

print(obj.getName())
print(obj.getAmount())