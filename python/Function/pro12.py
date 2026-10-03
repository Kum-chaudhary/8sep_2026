state = ["Gujarat","Maharashtra","Rajasthan","Karnataka"]

result = dict(map(lambda item: (item[0], item[1] + "1"), enumerate(state)))
print(result)