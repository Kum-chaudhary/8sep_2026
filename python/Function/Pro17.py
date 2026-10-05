employee_list = [
    { "id" : 1,"Name" :"Kumkum","salary" : 140000,
     "id" :  2,"Name" :"Krina","salary" : 40000,
     "id" : 3,"Name" :"mina","salary" : 45000,
     "id" : 4,"Name" :"aakash","salary" : 56000,
     "id" : 5,"Name" :"hina","salary" : 58000,
}
]

#print(employee_list)

highest_employee_salary = list(filter(lambda employee : employee["salary"] >= 50000,employee_list))

print(highest_employee_salary)