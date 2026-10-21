import os

#os.mkdir("Hello") # create folder

if os.path.exists("Hello"):
    print("Already exist")
else:
    os.mkdir("Hello")
    print("Folder Created !")
