import math

# write your code here

loan_P = int(input("Enter the loan principal: "))
option = input("What do you want to calculate?")

payment = 0
last_pay = 0
months = 0

if option == "p":
    months = int(input("Enter the number of months: "))
    payment = math.ceil((loan_P / months))
    last_pay = loan_P - (months - 1) * payment
    print(f"Your monthly payment = {payment} and the last payment = {last_pay}.")

elif option == "m":
    month_pay = int(input("Enter the monthly payment: "))
    months = loan_P / month_pay
    if months == 1:
        print(f"It will take {months} month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")
else:
    print("¡Not a valid option!")
