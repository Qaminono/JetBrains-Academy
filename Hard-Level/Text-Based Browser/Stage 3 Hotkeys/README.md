#  Description

Every browser has a “back” button. If the user presses this button, the browser shows the previous web page. This feature can be implemented using a stack. This will allow the browser to save the pages visited by the user – google, wikipedia, bloomberg, … – but when the user types back, you will see the pages in the reverse order – … bloomberg, wikipedia, google.
#  Objectives

The result of this task is the same as in the previous one, but now the program has a new feature:

-    The program should show the previous web page saved to a file if the user types back. Note that the last page you saved to a file is actually the current page; when the user types back, you should output the page that was before the current one. You can implement a stack to do this, but note that the current page should not be in that stack. For example, if the user inputs bloomberg.com, then nytimes.com, and then back, the user should see the content of bloomberg.com.
-    If there are no more pages in the browser history, don’t output anything. For example, if the first input of the user is the string back, your program shouldn't output anything.

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
    
    > nytimes.com
    This New Liquid Is Magnetic, and Mesmerizing
    
    Scientists have created “soft” magnets that can flow
    and change shape, and that could be a boon to medicine
    and robotics. (Source: New York Times)
    
    
    Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
    
    Jessica Wade has added nearly 700 Wikipedia biographies for
    important female and minority scientists in less than two
    years.
    
    > back
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