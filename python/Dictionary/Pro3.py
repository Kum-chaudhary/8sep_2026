student = {
    "name" : "kumkum",
    "subject" : "Python",
    "score": 89,
    "city" : "Ahmedabad"
}

print(student)

for key in student.keys():
    print(key)

print("------------------")

for value in student.values():
    print(value)

print("---------------")

for key,value in student.items():  # keys and value both print
    print(f"{key} = {value}")