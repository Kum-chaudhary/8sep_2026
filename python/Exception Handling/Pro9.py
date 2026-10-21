""" Exception : is a parent class which we can import or inherite
    in our own exception class.
"""

class AgeNotValid(Exception):  # here, AgeNotValid is an userdefine Exception
    pass
age = int(input("Enter Your Age :"))
if age < 18 :
    raise("You are below 18 :")
