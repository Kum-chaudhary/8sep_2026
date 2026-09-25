age_group_list = [23,56,12,78,36]
filter_group_list = [(age,"eligible") if age>18 else (age,"not eligible") for age in age_group_list]
print(age_group_list)
print(filter_group_list)