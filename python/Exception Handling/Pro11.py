try:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))

    ans = num1 / num2

except ZeroDivisionError:
    print("can not Devide by zero.")
except ValueError:
    print("Invalid Input")
else:
    print(ans)
finally:
    print("THANK YOU FOR USING APPLICATION !")