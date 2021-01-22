#  Description

Okay, it seems like your program translates as expected. However, there’s a problem you should always keep in mind: something can break your program.

Up to this stage, you were thinking about things that should be in your code. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? That can break your program.

All these situations are called exceptions because you didn’t expect them to happen, and now you have to handle them.
#  Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Notify users that they cannot translate to or from some languages.

    > python translator.py english korean hello
    Sorry, the program doesn't support korean

Example 2

Check and notify if there’s a problem with the user’s internet connection.

    > python translator.py english all hello
    Something wrong with your internet connection

Example 3

Tell the user that you can’t translate jabberwocky.

    > python translator.py english all brrrrrrrrrrr
    Sorry, unable to find brrrrrrrrrrr