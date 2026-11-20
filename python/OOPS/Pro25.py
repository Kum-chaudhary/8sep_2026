class Sample:
    def __init__(self,products):
        self.products = products

    def __getitem__(self, index):
        return self.products[index]

obj = Sample(["iphone","135000"])

print(obj[0])
print(obj[1])
