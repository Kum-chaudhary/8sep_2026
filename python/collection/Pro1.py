"""
list : list is a collection of data type 
      which is contain similer dis-similer data element.

    list is a orderable,indexable,mutable data types.

    mutable: means we can change element after creation.

    list which is represent by [] braces.  
"""

l1 = []
print(l1)

shopping_list = ["fruits","bread","milk","vegs"]
print(shopping_list)


# define list sequence
for item in shopping_list:
    print(item)

# find length of list

print(len(shopping_list))

# len withount using value

count = 0

for item in shopping_list:
    count+=1
    print(count)

"""
acess list or list indexing
"""    
l1 = [10,20,45,67,90,70]
"""
0   1   2   3   4   5   (+) positive indexing
10  20  45  67  90  70
-6 -5  -4  -3   -2  -1  (-) negative indexing
"""

print(l1[0])  # 10

print(l1[3]) # 67

print(l1[2])  #45

print(l1[-4]) #20
