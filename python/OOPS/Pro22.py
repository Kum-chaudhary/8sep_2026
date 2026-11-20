class Sample:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"object created {self.name}"
obj = Sample("Kumkum")
print(obj)        