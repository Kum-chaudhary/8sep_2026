try:
    num1 = int(input("Enter number 1:"))
    num2 = int(input("Enter number 2:"))

    ans = num1 / num2
    print(ans)
except ZeroDivisionError:
    print("can not divide by zero")

except ValueError:
    print("Invalid value")    