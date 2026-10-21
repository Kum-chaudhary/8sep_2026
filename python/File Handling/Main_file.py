import datetime

f = open("Vaccination_report.txt","a")

name = input("Enter Your Name :")
age = input("Enter Your Age:")
gender = input("Enter Your gender:")
contact = input("Enter Your Contact No:")
vaccination_status = input("Enter Vaccination status : Yes / No :")

current_time = datetime.datetime.now()

f.write("\n-----------------------------\n")
f.write("\n"+str(current_time)+"\n")
f.write("\n Name :"+name)
f.write("\n age :"+age)
f.write("\n gender :"+gender)
f.write("\n contact :"+contact)
f.write("\n Vaccination status :"+vaccination_status)

print("Record saved successfully !!")

f.close()