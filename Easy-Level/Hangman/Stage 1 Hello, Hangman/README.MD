Hangman is a popular yet grim intellectual game. A cruel computer hides a word from you. Letter by letter you try to guess it. If you fail, you'll be hanged, if you win, you'll survive. See also: Wikipedia

You probably played the game at least once in your life; now you can actually create this game yourself!

#  Description
Let's have a brief overview of what you are going to build during this project. Here is what the gameplay should look like:

In the main menu, a player can choose to either play or exit the game;
If the user chooses to play, the computer picks a word from a list: this will be the riddle;
The computer asks the player to enter a letter that (s)he thinks is in the word;
If there's no such letter in the word and this letter hasn't been tried before, the computer counts it as a miss. A player can afford only up to 8 misses before the game is over;
If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
When the entire word is uncovered, it's a victory! The game calculates the final score and goes back to the main menu.
It may sound complex, but the project is split into small stages with hints to see you through. The final product is sure to be replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print something using Python: try to apply your knowledge to intrigue your friends with your game announcement!

#  Objectives
In this stage you should write a program that prints the lines as shown in the example below:

#  Example
Output:

    H A N G M A N
    The game will be available soon.
