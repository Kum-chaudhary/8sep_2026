class Student:
    def __init__(self):
        self.subject = "Python"
        self.marks = 78
        self.__Score = 56   # this is private class not access student class


    def getScore(self):
        return self.__Score
s1 = Student()

print(s1.subject)
print(s1.marks)
print(s1.getScore()) 