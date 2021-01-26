import random

options = ["paper", "scissors", "rock"]
win_options = {"paper": "rock", "scissors": "paper", "rock": "scissors"}
user = input("")
computer = random.choice(options)
if user == computer:
    print(f"There is a draw({computer}")
elif win_options[user] == computer:
    print(f"Well done. The computer chose {computer} and failed")
elif win_options[computer] == user:
    print(f"Sorry, but the computer chose {computer}")
