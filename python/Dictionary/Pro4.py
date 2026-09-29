student = {
    "name" : "kumkum",
    "subject" : "Python",
    "score": 89,
    "city" : "Ahmedabad"
}

print(student)

print(student.get("city"))

# student clear
#student.clear()

print(student)

student.update(
    {
        "department": "IT",
        "state" : "Guj"
    }
)

print(student)