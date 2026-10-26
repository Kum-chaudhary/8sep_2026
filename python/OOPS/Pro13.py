class A:
    def displayA(self):
        print("A class is here")

class B:
    def displayB(self):
        print("B class is here")


class C(A,B):
    def displayC(self):
        print("C class is here")

obj = C()
obj.displayA()
obj.displayB()        
