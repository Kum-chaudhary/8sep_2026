f = open("myfile.txt","r")

data = f.readlines()

for line in data:       # line by line iterate
    print(line) 