"""
 *args :
      arguments : tuple as a parameter.

 **kwargs : key with arguments or dictionary as a parameter.     
"""
def add(num1,num2):
    print(num1)
    print(num2)
  #  add(10,34,56)

def addition(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum
print(addition(10,45,34,67,78))