ACCOUNT_BALANCE = 5000

class InsuffiecentBalance(Exception):
    pass

menu = """
          MENU
          1) DEPOSITE
          2) WITHDRAW
"""
status = True
while status:
    print(menu)

    choice = int(input("Enter Your Choice :"))
    if choice == 1:
        amount = int(input("Enter Your Deposite Amount :"))
        ACCOUNT_BALANCE += amount
        print("TOTAL AMOUNT : ",ACCOUNT_BALANCE)
    elif choice == 2:
        amount = int(input("Enter Your WithDraw Amount :"))
        try:
            if amount > ACCOUNT_BALANCE:
                raise InsuffiecentBalance("Insuffiecient Balance - Please Enter Below Amount")
        except InsuffiecentBalance as e:
            print(e)
        else:
            ACCOUNT_BALANCE -= amount
            print("TOTAL BALANCE :",ACCOUNT_BALANCE)
    else:
        pass

    exit_choice = input("Are You Sure You Want To Exit ? Press y For yes And n For No:")

    if exit_choice == 'y':
        status = False
    
