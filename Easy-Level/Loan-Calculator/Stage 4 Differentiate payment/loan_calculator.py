import math
import argparse


def main():
    parser = argparse.ArgumentParser(description="Loan calculator")
    parser.add_argument("--type")
    parser.add_argument("--payment")
    parser.add_argument("--periods")
    parser.add_argument("--principal")
    parser.add_argument("--interest")
    args = parser.parse_args()

    def diff(arguments):
        m = 1
        p = float(arguments.principal)
        i = float(arguments.interest) / 1200
        n = float(arguments.periods)
        summary = 0
        while m <= n:
            d = p / n + i * (p - p * (m - 1)/n)
            summary += math.ceil(d)
            print(f"Month {m}: payment is {math.ceil(d)}")
            m += 1
        overpayment = math.ceil(summary - p)
        return f"Overpayment = {overpayment}"

    def number_of_month(arguments):
        principal = float(arguments.principal)
        monthly_payment = float(arguments.payment)
        loan_interest = float(arguments.interest)
        i = loan_interest / 100 / 12
        num_of_month = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), 1 + i))
        in_years = num_of_month // 12
        in_month = num_of_month - in_years * 12
        str_years = ("" if in_years == 0 else str(in_years) + " year") + ("s" if in_years > 1 else "")
        str_month = ("" if in_month == 0 else str(in_month) + " month") + ("s" if in_month > 1 else "")
        if in_years and in_month:
            str_res = f"It will take {str_years} and {str_month} to repay this loan!"
        elif in_years:
            str_res = f"It will take {str_years} to repay this loan!"
        elif in_month:
            str_res = f"It will take {str_month} to repay this loan!"
        else:
            str_res = f"The loan is already repay!"
        print(str_res)
        overpayment = monthly_payment * num_of_month - principal
        return f"Overpayment = {overpayment}"

    def payment_amount(arguments):
        principal = float(arguments.principal)
        number_of_periods = float(arguments.periods)
        loan_interest = float(arguments.interest)
        i = loan_interest / 100 / 12
        annuity_payment = principal * ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1))
        print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
        overpayment = math.ceil(annuity_payment) * number_of_periods - principal
        return f"Overpayment = {math.ceil(overpayment)}"

    def loan_principal(arguments):
        annuity_payment = float(arguments.payment)
        number_of_periods = float(arguments.periods)
        loan_interest = float(arguments.interest)
        i = loan_interest / 100 / 12
        principal = annuity_payment / ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1))
        print(f"Your loan principal = {round(principal)}!")
        overpayment = annuity_payment * number_of_periods - math.ceil(principal)
        return f"Overpayment = {math.ceil(overpayment)}"

    is_diff = args.type == "diff" and args.payment is None and args.interest and args.periods and args.principal
    if is_diff:
        print(diff(args))
    else:
        annuity_args = [args.payment, args.interest, args.periods, args.principal]
        is_annuity = args.type == "annuity" if annuity_args.count(None) == 1 else False
        calculate = {args.payment: payment_amount,
                     args.periods: number_of_month,
                     args.principal: loan_principal}
        if is_annuity:
            print(calculate[None](args))
        else:
            print("Incorrect parameters")


main()
