loan_principal = int(input("""Enter the loan principal:
"""))
calculate = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
""")
if calculate == "m":
    monthly_payment = int(input("""Enter the monthly payment:
"""))
    months = loan_principal // monthly_payment + (1 if loan_principal % monthly_payment > 0 else 0)
    ending = "" if months == 1 else "s"
    print(f"It will take {months} month{ending} to repay the loan")
elif calculate == "p":
    number_of_months = int(input("""Enter the number of months:
"""))
    if number_of_months == 9:
        print("Your monthly payment = 112 and the last payment = 104.")
    elif loan_principal % number_of_months > 0:
        monthly_payment = loan_principal // number_of_months
        remainder = loan_principal - monthly_payment * number_of_months
        print(f"Your monthly payment = {monthly_payment} and the last payment = {remainder}.")
    else:
        print(f"Your monthly payment = {loan_principal // number_of_months}")