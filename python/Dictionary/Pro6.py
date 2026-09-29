products = {}

menu = """
          Menu 
        press 1 for product
        press 2 for customer
"""
status = True
while status:
    print(menu)
    choice = int(input("Enter your choice :"))
    if choice == 1:
        maneger_menu = """
          Menu 
        press 1 for product
        press 2 for customer
        press 3 for exit
""" 
    m_status = True
    while m_status:
            print(maneger_menu)
            m_choice = int(input("Enter your choice:"))
            if m_choice == 1:
                sub_dict = {}

                product_name = input("Enter product name:")
                qty = int(input("Enter quantity:"))
                price = int(input("enter price:"))

                if product_name in products.keys():
                    sub_dict["qty"] = qty + products[product_name]["qty"]
                    sub_dict["price"] = price
                    print(products)
                else:
                    sub_dict["qty"] = qty
                    sub_dict["price"] = price

                    products[product_name] = sub_dict
                    print(products)
            elif m_choice == 2:
                print("--------Product------------")
                for product in products:
                        print(f"product name :{product}")
                        print(f"qty: {products[product]["qty"]}")
                        print(f"price: {products[product]["price"]}")
                        print("-------------")

                else:
                    m_status = False
            elif choice == 2:
                pass
            else:
                print("invalid logout")
                    
    exist_choice = input("do you want to logout ? 'y' for yes and 'n' for no:") 
    if exist_choice == 'y' or exist_choice == 'yes':
        status = False
    else:
        status = True


