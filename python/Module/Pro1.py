import random 

print("random between 0 - 1 :")
print(random.random())

print("random number 1 to 10 :")
print(random.randint(1, 10))

print("now generate 4 digit number :")
print(random.randint(1111,9999))

print("random choice for string :")
s1 = "Python"
print(random.choice(s1))