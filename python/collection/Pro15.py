subject_list =[]
status = True

while status:
    subject = input("Enter your subject : ")
    if subject not in subject_list:
        subject_list.append(subject)
        print(f" '{subject}' Added !!")
    else:
        print(f" '{subject}' Already exists !")

    choice = input("Do you want to add more subject : (press y for yes press n for no)")
    if choice == 'n' or choice == 'no':
        status = False 
print(subject_list)        