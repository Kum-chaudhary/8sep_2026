"""
nested if statement:
 syntax:
  if condition:
  statement
     if condition:
      statement
     else:
     statement
  else:
     if condition:
     statement
  else:
  statement
"""

email = "admin@gmail.com"
password = "123456"

u_email = input("Enter your Email:")
u_password = input("Enter your password:")

if u_email == email:
    if u_password == password:
        print("login sucessfully.")
    else:
        print("invalid password")
else:
    print("invalid email")