
 # year ko month me convert
year = int(input("Enter year: "))
ans = year * 12
print("month :",ans)

# days ko year aur month me convert kiya 
days = int(input("Enter total days : "))

# Years calculate karein
years = days // 365
remaining_days = days % 365

# Months calculate karein
months = remaining_days // 30
final_days = remaining_days % 30

print(f"{years} Years, {months} Months, {final_days} Days")