import os
#os.remove("Hello.txt")

if os.path.exists("Hello"):
    os.rmdir("Hello")
else:
    print("Folder does not exists")
   