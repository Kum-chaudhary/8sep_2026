student = {
    "Name" : "Kumkum",
    "Subject" : "Python"
}

try:
    print(student)
    print(student["Name"])
    print(student["Email"])
except KeyError:
    print("Key does not exist !")