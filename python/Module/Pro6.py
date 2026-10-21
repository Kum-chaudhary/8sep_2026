import os

print("CWd:",os.getcwd())

os.chdir("C:\\Users\\pramukh\\Desktop\\sql")
print("Change directory :",os.getcwd())
print(os.listdir())
os.mkdir("Hello")

