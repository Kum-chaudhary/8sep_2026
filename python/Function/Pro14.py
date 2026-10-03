l1 = [12,56,23,78,4,3,9,25]

even_list = []

def findEven(element):
    if element % 2 == 0:
        return element
even_list = list(filter(findEven,l1))
print(even_list)


# filter with lambda function

even_list = list(filter(lambda element: element % 2 == 0,l1))
print(even_list)
