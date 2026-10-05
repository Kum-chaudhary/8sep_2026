student_list = ["Arav","Anvesha","Aditya,","keya","rima"]

a_name_student_list = list(filter(lambda student : student.startwith("A"),student_list))
print(a_name_student_list)