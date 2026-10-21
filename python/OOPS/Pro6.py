class Student:
    def __init__(self,name,subject,score):
        self.name = name
        self.subject = subject
        self.score = score

    def display(self):
            print(self.name)
            print(self.subject)
            print(self.score)

name = input("Enter Your Name :")
subject = input("Enter Subject :")
score = input("Enter Score :")

student = Student(name,subject,score)

student.display()