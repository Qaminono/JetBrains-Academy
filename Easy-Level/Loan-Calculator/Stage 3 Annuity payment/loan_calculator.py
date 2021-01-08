import math


def main():
    def number_of_month():
        print("Enter the loan principal:")
        loan_principal = float(input())
        print("Enter the monthly payment:")
        montly_payment = float(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        i = loan_interest / 100 / 12
        num_of_month = math.ceil(math.log(montly_payment / (montly_payment - i * loan_principal), 1 + i))
        in_years = num_of_month // 12
        in_month = num_of_month - in_years * 12
        str_years = ("" if in_years == 0 else str(in_years) + " year") + "s" if in_years > 1 else ""
        str_month = ("" if in_month == 0 else str(in_month) + " month") + "s" if in_month > 1 else ""
        if in_years and in_month:
            str_res = f"It will take {str_years} and {str_month} to repay this loan!"
        elif in_years:
            str_res = f"It will take {str_years} to repay this loan!"
        elif in_month:
            str_res = f"It will take {str_month} to repay this loan!"
        else:
            str_res = f"The loan is already repay!"
        return str_res

    def payment_amount():
        print("Enter the loan principal:")
        loan_principal = float(input())
        print("Enter the number of periods:")
        number_of_periods = float(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        i = loan_interest / 100 / 12
        annuity_payment = loan_principal * ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1))
        return f"Your monthly payment = {math.ceil(annuity_payment)}!"

    def loan_principal():
        print("Enter the annuity payment:")
        annuity_payment = float(input())
        print("Enter the number of periods:")
        number_of_periods = float(input())
        print("Enter the loan interest:")
        loan_interest = float(input())
        i = loan_interest / 100 / 12
        loan_principal = annuity_payment / ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1))
        return f"Your loan principal = {math.ceil(loan_principal)}!"




    print(""""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
    case = input("")
    cases = {"n": number_of_month,
             "a": payment_amount,
             "p": loan_principal}

    print(cases[case]())

main()
