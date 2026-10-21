import os

try:
    os.mkdir("Hello")

except FileExistsError:
    print("Folder already Exist")