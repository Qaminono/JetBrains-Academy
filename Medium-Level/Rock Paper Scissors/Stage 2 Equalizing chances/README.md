#  Description

Well, now let's do something real. Nobody wants the game where you always lose.
Using the power of the random module, we'll make a truly interesting game.

You should write a program that reads input from the user, chooses a random option and then says who won, the user or the computer.
There are a few examples below, providing output for any outcome (<option> is the option chosen by your program):

1.    Lose -> Sorry, but the computer chose <option>
2.    Draw -> There is a draw (<option>)
3.    Win -> Well done. The computer chose <option> and failed

#  Objectives

Your program should:

1.    Read user's input specifying the option that user has chosen
2.    Choose a random option
3.    Compare the options and determine the winner
4.    Output a line depending on the result of the game:
        - Lose -> Sorry, but the computer chose <option>
        - Draw -> There is a draw (<option>)
        - Win -> Well done. The computer chose <option> and failed

#  Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

    > rock
    Well done. The computer chose scissors and failed

Example 2

    > scissors
    There is a draw (scissors)

Example 3

    > paper
    Sorry, but the computer chose scissors