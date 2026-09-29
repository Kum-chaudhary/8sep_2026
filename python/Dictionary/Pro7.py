products = {}

menu = """
          Menu
        Press 1 for Product
        Press 2 for Customer
"""

status = True

while status:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:

        manager_menu = """
          Manager Menu
        Press 1 for Add Product
        Press 2 for View Products
        Press 3 for Exit
        """

        m_status = True

        while m_status:
            print(manager_menu)
            m_choice = int(input("Enter your choice: "))

            if m_choice == 1:
                sub_dict = {}

                product_name = input("Enter product name: ")
                qty = int(input("Enter quantity: "))
                price = int(input("Enter price: "))

                if product_name in products.keys():
                    sub_dict["qty"] = qty + products[product_name]["qty"]
                    sub_dict["price"] = price

                    products[product_name] = sub_dict

                else:
                    sub_dict["qty"] = qty
                    sub_dict["price"] = price

                    products[product_name] = sub_dict

                print("Product added successfully!")
                print(products)

            elif m_choice == 2:

                print("-------- Product ------------")

                for product in products:
                    print(f"Product Name: {product}")
                    print(f"Qty: {products[product]['qty']}")
                    print(f"Price: {products[product]['price']}")
                    print("-----------------------------")

            elif m_choice == 3:
                m_status = False

            else:
                print("Invalid choice!")

    elif choice == 2:
        print("Customer section")

    else:
        print("Invalid choice!")

    exit_choice = input(
        "Do you want to logout? 'y' for yes and 'n' for no: "
    )

    if exit_choice == "y" or exit_choice == "yes":
        status = False
    else:
        status = True

print("Program exited successfully.")