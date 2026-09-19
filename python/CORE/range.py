"""
 range :
      ([start],stop,[step])

   range(4) : by default it will start from 0

   range(1,7) : it will be start 1 to 6 

   step: by default increment by +1.

"""

for i in range(1,6,3):
    print(i)

num = int(input("Enter the number:"))
for num in range(num):
    print(num)    

"""
output:
1
4
Enter the number:5
0
1
2
3
4
"""