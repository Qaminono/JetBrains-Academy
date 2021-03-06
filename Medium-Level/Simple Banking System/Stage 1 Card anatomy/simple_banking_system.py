import random


class Bank:
    def __init__(self):
        self.database = {}
        self.current_user = None
        self.is_run = True

    def start_page(self):
        if self.is_run:
            commands = {"1": self.create_an_account,
                        "2": self.log_into_account,
                        "0": self.exit}
            print("1. Create an account\n2. Log into account\n0. Exit")
            command = input()
            return commands.get(command, self.start_page)()
        else:
            return

    def create_an_account(self):
        card_number = "400000" + str(random.randint(1, 9999999999)).rjust(10, "0")
        if card_number not in self.database:
            card_pin = str(random.randint(1, 9999)).rjust(4, "0")
            self.database[card_number] = card_pin
            print(f"Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{card_pin}")
            return self.start_page()
        else:
            return self.create_an_account()

    def account_page(self):
        commands = {"1": self.check_balance,
                    "2": self.log_out,
                    "0": self.exit}
        print("1. Balance\n2. Log out\n0. Exit")
        command = input()
        return commands.get(command, self.account_page)()

    def log_into_account(self):
        card_number = input("Enter your card number:")
        card_pin = input("Enter your PIN:")
        if self.database.get(card_number) == card_pin:
            print("You have successfully logged in!")
            self.current_user = card_number
            return self.account_page()
        else:
            print("Wrong card number or PIN!")
            return self.start_page()

    def check_balance(self):
        balance = self.database.get(self.current_user)
        print("Balance: 0")
        return self.account_page()

    def log_out(self):
        self.current_user = None
        print("You have successfully logged out!")
        return self.start_page()

    def exit(self):
        self.is_run = False
        print("Bye!")
        return


bank = Bank()
bank.start_page()
