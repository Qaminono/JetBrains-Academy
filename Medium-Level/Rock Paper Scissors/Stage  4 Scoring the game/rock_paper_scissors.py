import random


class Game:

    def __init__(self):
        self.options = ["paper", "scissors", "rock"]
        self.win_options = {"paper": "rock", "scissors": "paper", "rock": "scissors"}
        self.is_game = True
        self.username = input("Enter your name: ")
        print(f"Hello, {self.username}")
        self.user_choice = ""
        self.computer_choice = ""
        self.commands = {"!exit": self._exit,
                         "!rating": self._show_rating}
        self.rating = {}
        try:
            with open("rating.txt") as file:
                for line in file.readlines():
                    username, score = line.split(" ")
                    self.rating[username] = int(score)
        except FileNotFoundError:
            with open("rating.txt", "a+") as file:
                pass
        self.rating.setdefault(self.username, 0)

    def main_menu(self):
        while self.is_game:
            self.user_choice = input()
            if self.user_choice in self.commands:
                self.commands[self.user_choice]()
            elif self.user_choice in self.options:
                print(self.game())
            else:
                print("Invalid input")
        return

    def game(self):
        self.computer_choice = random.choice(self.options)
        results = {self._is_draw(): f"There is a draw({self.computer_choice})",
                   self._is_user_win(): f"Well done. The computer chose {self.computer_choice} and failed",
                   self._is_computer_win(): f"Sorry, but the computer chose {self.computer_choice}"}
        if self._is_user_win():
            self.rating[self.username] += 100
        if self._is_draw():
            self.rating[self.username] += 50
        return results[True]

    def _is_draw(self):
        return self.user_choice == self.computer_choice

    def _is_user_win(self):
        return self.win_options[self.user_choice] == self.computer_choice

    def _is_computer_win(self):
        return self.win_options[self.computer_choice] == self.user_choice

    def _exit(self):
        with open("rating.txt", "w") as file:
            for name in self.rating:
                print(f"{name} {self.rating[name]}", file=file)
        print("Bye!")
        self.is_game = False
        return self.main_menu()

    def _show_rating(self):
        print(f"Your rating: {self.rating.get(self.username, 0)}")
        return self.main_menu()


game = Game()
game.main_menu()
