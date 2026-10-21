"""
Json file :
     json file stands for javascript object notation.
"""

import json

user = {
    'name' : 'kumkum',
    'subject' : 'python',
    'score' : 87
}

with open("Myfile.json","w") as f:
    json.dump(user,f,indent=4)

print("Succesfully file created !")    