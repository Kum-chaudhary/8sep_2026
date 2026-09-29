t1 = (1,2,3)
t2 = t1 * 3
print(t1)
print(t2)  #(1, 2, 3, 1, 2, 3, 1, 2, 3)

t1 = (10,20,30,40,68,2,3)
print(sum(t1)) #173 

print(min(t1)) #2
print(max(t1)) #68

print(len(t1)) #7
print(tuple(sorted(t1))) #(2, 3, 10, 20, 30, 40, 68)
print(sorted(t1)) # list : [2, 3, 10, 20, 30, 40, 68]

t1 = (10,20,30,40,10,2,3) 
print(t1.count(10)) #2
print(t1.index(20)) #1