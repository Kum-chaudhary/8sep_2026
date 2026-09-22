fruit_list = []

status = True

while status:
    fruit_name = input("Enter fruit name :")
    fruit_list.append(fruit_name)

    choice = input("do you want to add more fruits ? press y for yes and press n for no :").lower()
    if choice == 'n' or choice =='no':
        status = False
    else:
        status = True
print(fruit_list)        