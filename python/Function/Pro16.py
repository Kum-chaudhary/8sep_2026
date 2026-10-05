age_validate = [2,63,76,34,23,22,5,57,15]

user_validate = list(filter(lambda age : age >= 18,age_validate))

print(user_validate)