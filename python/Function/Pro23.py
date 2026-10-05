"""
generator : generator is a special function which is iterate 
each element by yield keyword.
"""

def numbers():
    return 10
print(numbers()) # 10

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()
print(next(gen)) # 10
print(next(gen))  #20
print(next(gen)) #30
#print(next(gen)) #StopIteration error