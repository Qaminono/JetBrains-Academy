#  Description

There’s a faster way to translate a word without being asked by the program every time. To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.

At this stage, you should add command-line argument handling in your code. This is possible via Python sys package.

You'll see some significant changes in the usability of the app!
#  Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

    > python translator.py english french hello
    French Translations:
    bonjour
    allô
    ohé
    coucou
    salut
    
    French Examples:
    Well, hello, freedom fighters.:
    Et bien, bonjour combattants de la liberté.
    
    Goodbye England and hello the Netherlands...:
    Au revoir l'Angleterre et bonjour les Pays-Bas...
    
    Yes, hello. Jackson speaking.:
    Oui, allô, Jackson à l'appareil.
    
    Hello, hello, hello, hello.:
    Allô, allô, allô, allô.
    
    And began appearing hello kitty games online.:
    Et a commencé à apparaître bonjour Kitty jeux en ligne.

Example 2

Don’t forget to take a zero-argument, which means translating to all languages in the list and saving the output to a file.

    > python translator.py english all hello