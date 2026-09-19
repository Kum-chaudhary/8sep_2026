"""
control statement :
 there are mainly 3 types of control statement.
  1) conditional 
  2) looping
  3) jumping

1) conditional statement: 
   mainly used for condition.

   there are 5 type of conditional.

   1)if statement 
     syntax :
         if condition:
          statement

   2)if..else:

          if condition:
          statement
          else:
          statement
   3)elif :
   
        if condition:
        statement
        elif condition:
        statement
        elif condition:
        statement
        else:
        statement

   4)nested if
   5)match  
"""

age = int(input("Enter your age:"))
if age >= 18 :
    print("you are elligible for votting")

num = int(input("Enter the number:"))
if num>=50:
    print("number is abouve 50")
else:
    print("nuber is below 50")   

   