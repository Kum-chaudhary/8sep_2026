class Sample:
    def __init__(self,value):
        self.value = value

    def __add__(self, obj):
        return self.value + obj.value

obj1 = Sample(10)
obj2 = Sample(20)

print(obj1 + obj2)