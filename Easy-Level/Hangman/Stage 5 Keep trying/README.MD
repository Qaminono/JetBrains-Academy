# Description
Let's make the game iterative. It's time to make it resemble the classical Hangman a bit more: a player should guess letters in the word instead of typing the entire word at once. If the player guesses a letter, it should be uncovered in the word. For now, start with the defeat case and add 8 tries to guess a letter that appears in the word. When the player runs out of attempts, the game ends.

Later we will determine the winning conditions, but in this stage, let's see how well our player guesses the word on every attempt.

# Objectives
Now your game should work the following way:

1. A player has exactly 8 tries and enters letters. If a player has more tries but he actually guessed the word, it doesn't mean anything.

2. If the letter doesn't occur in the word, the computer takes one try away, even if the user already inputted this letter before.

3. If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.

4. Also, use our previous word list: 'python', 'java', 'kotlin', 'javascript' so that your program can be tested more reliably.

Please, make sure that your program's output formatting precisely follows the example output formatting. Pay attention to the empty lines between tries and in the end.
# Examples
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

Example 1

    H A N G M A N

    ----------
    Input a letter: > a

    -a-a------
    Input a letter: > i

    -a-a---i--
    Input a letter: > o
    No such letter in the word

    -a-a---i--
    Input a letter: > z
    No such letter in the word

    -a-a---i--
    Input a letter: > p
    No such letter in the word

    -a-a---ip-
    Input a letter: > p

    -a-a---ip-
    Input a letter: > h
    No such letter in the word

    -a-a---ip-
    Input a letter: > k
    No such letter in the word

    Thanks for playing!
    We'll see how well you did in the next stage
Example 2

    H A N G M A N

    ----
    Input a letter: > j

    j---
    Input a letter: > i
    No such letter in the word

    j---
    Input a letter: > g
    No such letter in the word

    j---
    Input a letter: > o
    No such letter in the word

    j---
    Input a letter: > a

    ja-a
    Input a letter: > v

    java
    Input a letter: > a

    java
    Input a letter: > j

    Thanks for playing!
    We'll see how well you did in the next stage
