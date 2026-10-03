subject_list = ["Maths","Science","English","Hindi"]
print(subject_list)

l1 = []

# without using map function
def convertUpper():
    for subject in subject_list:
        l1.append(subject.upper())
convertUpper()
print(l1)

# with using map function

def convertUpper(subject):
    return subject.upper()
l1 = list(map(convertUpper,subject_list))
print(l1)

# with using map and lambda function

l1 = list(map(lambda subject: subject.upper(),subject_list))
print(l1)