subject = ["java","python","C++"]

it = iter(subject)
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it)) #StopIteration error

print(next(it,"Finished"))
print(next(it,"Finished"))
print(next(it,"Finished"))  
print(next(it,"Finished"))