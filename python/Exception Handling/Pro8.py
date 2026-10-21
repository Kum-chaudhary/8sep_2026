import sys

try: 
    print(a)
except:
    print(sys.exc_info()[0])   #<class 'NameError'>
    print(sys.exc_info()[1])  # proper error define :name 'a' is not defined 