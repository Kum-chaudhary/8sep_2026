# fetch even and odd number lists.
l1 = [12,56,23,78,4,3,9,25]

even_list = []
odd_list = []

def findEven():
    for element in l1:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)    

print(l1)
findEven()
print(even_list)  
print(odd_list)          