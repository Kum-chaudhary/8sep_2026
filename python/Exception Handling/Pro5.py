l1 = [1,2,3,4]
try:
    print(l1[0])
    print(l1[1])

    print(l1[6])

except IndexError:
    print("Index does not exist .")