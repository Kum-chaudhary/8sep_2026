subject_list = ["Python","Java","C++","C#","JavaScript"]
print(subject_list)

def findlen(subject):
    return len(subject)
l2 = list(map(findlen,subject_list))

print(l2)