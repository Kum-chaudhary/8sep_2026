l1 = [1,2,3,4,5]
l2 = []

def add(element):
    return element + 10
        
l2 = list(map(add,l1))
print(l1)
print(l2)