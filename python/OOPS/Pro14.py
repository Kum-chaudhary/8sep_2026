class A:
    def __init__(self):
        self.num1 = 10
        self.num2 = 20

class B:
    def __init__(self):
        self.num3 = 30
        self.num4 = 40


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def display(self):
        self.addition = self.num1 + self.num2
        self.mult = self.num3 * self.num4 

        print(self.addition)
        print(self.mult)

c = C()
c.display()

