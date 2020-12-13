# Description
The recent version of the game is not as fun until we don't handle the player's victory. A player has 8 attempts to guess letters and its number is reduced even if the letter was correct.

Now a player will have a lot of attempts and is limited only by the number of mistakes they make. A player can be mistaken 8 times and wins when all the letters are guessed and there are still some tries left. If the player uses the last try and actually guesses the word, they are lucky then!

# Objectives
The player starts the game with 8 "lives", that is our player can input the wrong letter 8 times.

1. Print No such letter in the word and reduce the attempts count if the word guessed by the program doesn't contain this letter.

2. Print No improvements and reduce the attempts count if the guessed word contains this letter but the user tried this letter before.

3. The attempts count should be decreased only if there are no letters to uncover.

Please, make sure that your program's output formatting precisely follows the example output formatting. Pay attention to the empty lines between tries and in the end.
# Examples
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

Example 1

    H A N G M A N

    ------
    Input a letter: > t

    --t---
    Input a letter: > z
    No such letter in the word

    --t---
    Input a letter: > t
    No improvements

    --t---
    Input a letter: > t
    No improvements

    --t---
    Input a letter: > y

    -yt---
    Input a letter: > x
    No such letter in the word

    -yt---
    Input a letter: > y
    No improvements

    -yt---
    Input a letter: > p

    pyt---
    Input a letter: > p
    No improvements

    pyt---
    Input a letter: > q
    No such letter in the word

    pyt---
    Input a letter: > p
    No improvements
    You are hanged!
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
    Input a letter: > g
    No such letter in the word

    j---
    Input a letter: > g
    No such letter in the word

    j---
    Input a letter: > g
    No such letter in the word

    j---
    Input a letter: > a

    ja-a
    Input a letter: > v

    java
    You guessed the word!
    You survived!
