#  Description

Let's allow our browser to store web pages in a file and show them if the user types a shortened request (for example, wikipedia instead of [wikipedia.org](https://www.wikipedia.org)). You can store each page as a separate file or find another way to do this. Your program should accept one command-line argument, which is a directory to store the files, and the web pages should be saved inside this directory.
Objectives

In this stage, your program should:

-    Accept a command-line argument which is a directory for saved tabs. For example, if the argument is dir, then you need to create a folder with the name dir and save all the web pages that the user downloads in this folder.
-    Check if the user has entered a valid URL. It must contain at least one dot, for example, bloomberg.com. If the URL is incorrect, the browser should output an error message (it should contain the word error) and wait for another URL.
-    In this task, your program can only access two web pages: bloomberg.com and nytimes.com. If the URL isn't either of these two, your program should output an error message.
-    If the URL is valid, print the content of the web page and save it to a file in the aforementioned directory. You have two predefined variables with the content of the web pages that you should save: bloomberg_com and nytimes_com. The name of the file should correspond to the name of the web page. To get the name of the file, remove the last dot and everything that comes after it. This way, the file for the page bloomberg.com will be named bloomberg.
-    Read the next input. If this input is the string exit, the program should stop running. If not, check if the string corresponds to the name of any file with a web page you saved before. If it does, print the content of this file. If it doesn't, check if the string is a new valid URL. If it is, repeat step 4. If it isn't, output an error message.

#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    > python browser.py dir-for-files
    > bloomberg.com
    The Space Race: From Apollo 11 to Elon Musk
    
    It's 50 years since the world was gripped by historic images
    of Apollo 11, and Neil Armstrong -- the first man to walk
    on the moon. It was the height of the Cold War, and the charts
    were filled with David Bowie's Space Oddity, and Creedence's
    Bad Moon Rising. The world is a very different place than
    it was 5 decades ago. But how has the space race changed since
    the summer of '69? (Source: Bloomberg)
    
    
    Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
    
    Twitter and Square Chief Executive Officer Jack Dorsey
    addressed Apple Inc. employees at the iPhone maker’s headquarters
    Tuesday, a signal of the strong ties between the Silicon Valley giants.
    
    > bloomberg
    The Space Race: From Apollo 11 to Elon Musk
    
    It's 50 years since the world was gripped by historic images
    of Apollo 11, and Neil Armstrong -- the first man to walk
    on the moon. It was the height of the Cold War, and the charts
    were filled with David Bowie's Space Oddity, and Creedence's
    Bad Moon Rising. The world is a very different place than
    it was 5 decades ago. But how has the space race changed since
    the summer of '69? (Source: Bloomberg)
    
    
    Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
    
    Twitter and Square Chief Executive Officer Jack Dorsey
    addressed Apple Inc. employees at the iPhone maker’s headquarters
    Tuesday, a signal of the strong ties between the Silicon Valley giants.
    
    > nytimes
    Error: Incorrect URL
    
    > exit