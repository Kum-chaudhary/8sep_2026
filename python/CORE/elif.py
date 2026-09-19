score = int(input("Enter score:(1-100)"))

if score>=90:
    grade = 'A'
elif score>=75:
    grade = 'B'
elif score>=50:
    grade = 'C'
else:print('fail')

print(f"grade:{grade}")