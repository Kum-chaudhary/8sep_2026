class Student:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id 

obj = Student()
obj.setId(101)
print(obj.getId())       