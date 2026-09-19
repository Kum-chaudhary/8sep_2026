"""
string indexing :
    there are two types of index :
    0  1  2  3  4  5     (+ Positive index)
    P  y  t  h  o  n
   -6 -5 -4 -3  -2 -1     (- negative index) 

   by default string index always start from 0

   syntax : [start:end:step] 

"""

name = "python"
print(name[0])  #p

print(name[5])  #o

print(name[-4]) #t

# slicing : 

print(name[0:3]) # start from 0 and end with 3-1

name = "programing"
print(name[0:6]) # 0 to 5 progr

print(name[0:6:2])  # ending 0 to 2 pro


