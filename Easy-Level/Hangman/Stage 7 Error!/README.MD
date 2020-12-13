# Description
Now that we are done with the basics, let's work on some details.

In the previous stage if the user entered the same letter twice or typed a cyrillic letter, the program reduced the number of attempts regardless if this was a correct letter or not. But it is not fair to the user, isn't it? He gains no additional information about the situation on the field yet the program still reduces his attempts count. Let's fix it!

# Objectives
1. If the user enters the same letter twice then the program should output ``You already typed this letter ``.

2. Also, you should check if the user prints an English lowercase letter or not. If not, the program should print ``It is not an ASCII lowercase letter`` .

3. Also, you should check if the user printed exactly one letter. If not, the program should print ``You should input a single letter`` . Remember that zero is also not one!

4. Note that all these three errors should not reduce attempts count!

Please, make sure that your program's output formatting precisely follows the example output formatting. Pay attention to the empty lines between tries and in the end.
#  Examples
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
    Input a letter: > o
    You already typed this letter

    -a-a---i--
    Input a letter: > p

    -a-a---ip-
    Input a letter: > p
    You already typed this letter

    -a-a---ip-
    Input a letter: > h
    No such letter in the word

    -a-a---ip-
    Input a letter: > k
    No such letter in the word

    -a-a---ip-
    Input a letter: > a
    You already typed this letter

    -a-a---ip-
    Input a letter: > z
    No such letter in the word

    -a-a---ipt
    Input a letter: > t

    -a-a---ipt
    Input a letter: > x
    No such letter in the word

    -a-a---ipt
    Input a letter: > b
    No such letter in the word

    -a-a---ipt
    Input a letter: > d
    No such letter in the word

    -a-a---ipt
    Input a letter: > w
    No such letter in the word
    You are hanged!
Example 2

    H A N G M A N

    ----
    Input a letter: > j

    j---
    Input a letter: > i
    No such letter in the word

    j---
    Input a letter: > +
    It is not an ASCII lowercase letter

    j---
    Input a letter: > A
    It is not an ASCII lowercase letter

    j---
    Input a letter: > ii
    You should input a single letter

    j---
    Input a letter: > ++
    You should input a single letter

    j---
    Input a letter: >
    You should input a single letter

    j---
    Input a letter: > g
    No such letter in the word

    j---
    Input a letter: > a

    ja-a
    Input a letter: > v
    You guessed the word java!
    You survived!
