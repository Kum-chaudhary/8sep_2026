class Sample:
    def __init__(self,data):
        self.data = data

    def __len__(self):
        return len(self.data)


obj = Sample([34,56,34,24,89,65])   
print(len(obj))     