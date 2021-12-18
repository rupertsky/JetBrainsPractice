import math

# write your code here
option = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

payment = 0
p = 0
l_p = 0
m = 0

if option == "n":
    loan_P = int(input("Enter the loan principal: "))
    m_p = int(input("Enter the monthly payment: "))
    i = float(input("Enter the loan interest:"))
    nom_i = i / (12 * 100)

    m = math.log(m_p / (m_p - nom_i * loan_P), 1 + nom_i)
    m = math.ceil(m)
    years = m // 12
    months = m - (12 * years)

    if years != 0 and months != 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif years != 0 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 1 and months == 0:
        print(f"It will take {years} year to repay this loan!")
    else:
        print(f"It will take {months} months to repay this loan!")

elif option == "a":
    loan_P = int(input("Enter the loan principal: "))
    n_p = int(input("Enter the number of periods:"))
    i = float(input("Enter the loan interest:"))
    nom_i = i / (12 * 100)

    m_p = loan_P * ((nom_i * pow(1 + nom_i, n_p)) / (pow(1 + nom_i, n_p) - 1))
    m_p = math.ceil(m_p)
    print(f"Your monthly payment = {m_p}!")

elif option == "p":
    a_p = float(input("Enter the annuity payment: "))
    n_p = int(input("Enter the number of periods:"))
    i = float(input("Enter the loan interest:"))
    nom_i = i / (12 * 100)

    loan_P = a_p / ((nom_i * pow(1 + nom_i, n_p)) / (pow(1 + nom_i, n_p) - 1))

    print(f"Your loan principal = {loan_P}!")
else:
    print("¡Not a valid option!")
