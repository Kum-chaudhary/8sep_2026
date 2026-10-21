# json file read
import json

with open("Myfile.json","r") as file:
    data = json.load(file)

print(data)    