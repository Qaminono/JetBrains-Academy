#  Description

Every browser accepts a string from the user and then displays a web page. The string from the user is a URL (Uniform Resource Locator) and looks something like this: https://www.google.com. After receiving the URL, the browser has a lot of work to do, but in a nutshell, this work can be described as finding the web page. The web page is located somewhere on the Internet, and the browser has to retrieve it. Since the https://www. part is always the same, it is often omitted and the link is shortened to [google.com](https://www.google.com).

In our first stage, we'll try to imitate this behavior.

Please, solve this task in IDE. The [instruction](https://support.hyperskill.org/hc/en-us/articles/360038635392-How-to-install-and-run-IDE-and-EduTools-Plugin-for-Python-) in our help center can help you with IDE installation.

#  Objectives

-    You should write a program that takes a string from the user (URL) and outputs a "hard-coded" website with news (just a header and some text below).
-    The websites are presented as two variables in source code; you can see them in the template. These are mock versions of the sites [bloomberg.com](https://www.bloomberg.com) and [nytimes.com](https://www.nytimes.com). You just need to output them as a response to the corresponding input URL.

-    Also, you should add the option to quit the browser by typing exit. Real browsers don’t finish their work when they output a single web page, they are ready to accept a new URL at any moment. You should implement this behavior, too. An endless loop can help you with that part.

#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

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
    > exit