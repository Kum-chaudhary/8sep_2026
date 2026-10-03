"""
calculator :
     sub multiplication addition division 

"""
def add(num1,num2):
    ans = num1 + num2 
    print(ans)
def mul(num1,num2):
    ans = num1 * num2
    print(ans) 
def div(num1,num2):
    ans = num1 / num2
    print(ans)
def sub(num1,num2):
    ans = num1 - num2
    print(ans)           
menu = """
       MENU 
    press 1 for add
    press 2 for mul
    press 3 for divi
    press 4 for sub
    press 5 for exit
"""
print(menu)
choice = int(input("Enter your choice :"))

if choice == 1:
    add(10,20)
elif choice == 2:
    mul(2,3)
elif choice == 3:
    div(10/2)
elif choice == 4:
    sub(45-34)   
else:
    print("Exit")