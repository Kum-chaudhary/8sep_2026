f = open("Myfile3.txt","w")

name = input("Enter name:")
age = input("Enter your age:")

f.write(name)
f.write(str(age))

f.close()    