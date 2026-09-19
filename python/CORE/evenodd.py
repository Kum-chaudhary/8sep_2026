even_count = 0
odd_count = 0

for i in range(1,6):
 number = int(input("Enter a number:"))
if number % 2 == 0:
    even_count+=1
else:
    odd_count+=1
print(F"even count :{even_count}")
print(F"odd count :{odd_count}")

