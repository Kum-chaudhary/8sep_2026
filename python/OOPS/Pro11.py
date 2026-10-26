class A:
    def displayA(self):
        print("A class is here")

class B(A):
    def displayB(self):
        print("B class is here")

class C(B):
    def displayC(self):
        print("C class is here")

c = C()

c.displayA()
c.displayB()
c.displayC()
                
        