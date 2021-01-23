#  Description

Now we should bring our browser closer to resembling a real one by adding an address bar. In this stage, you need to leave your hard-coded variables behind and show your user some real pages. Make the browser request real input URLs and display the results.

You might find that you suddenly don't have permission to visit certain websites. That’s because of the user-agent, which is just a string that all browsers use to mark the request. Browsers have different user-agents, and since yours doesn’t have one, it may encounter problems. Frankly, browsers add a lot of additional information to the requests. All this info can be set using the request library. For this task, it's optional, but feel free to experiment.
#  Objectives

Keep the functionality from the previous stages and follow the same guidelines for file names. You don't need to keep the predefined variables with the content of web pages. Instead, add new features to the browser:

-    Your program should read the URL from the input as before, but now it should show the real web page.
-    Since the user can input the URL without https:// in the beginning, your browser should append this string if it is not there.

#  Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

    > python browser.py dir-for-files
    > docs.python.org
    
    <!DOCTYPE html>
    
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <meta charset="utf-8" /><title>3.7.4 Documentation</title>
        <link rel="stylesheet" href="_static/pydoctheme.css" type="text/css" />
        <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    
        <script type="text/javascript" id="documentation_options" data-url_root="./" src="_static/documentation_options.js"></script>
        <script type="text/javascript" src="_static/jquery.js"></script>
        <script type="text/javascript" src="_static/underscore.js"></script>
        <script type="text/javascript" src="_static/doctools.js"></script>
        <script type="text/javascript" src="_static/language_data.js"></script>
    
        <script type="text/javascript" src="_static/sidebar.js"></script>
    
        <link rel="search" type="application/opensearchdescription+xml"
              title="Search within Python 3.7.4 documentation"
              href="_static/opensearch.xml"/>
        <link rel="author" title="About these documents" href="about.html" />
        <link rel="index" title="Index" href="genindex.html" />
        <link rel="search" title="Search" href="search.html" />
        <link rel="copyright" title="Copyright" href="copyright.html" />
        <link rel="shortcut icon" type="image/png" href="_static/py.png" />
        <link rel="canonical" href="https://docs.python.org/3/index.html" />
    
        <script type="text/javascript" src="_static/copybutton.js"></script>
        <script type="text/javascript" src="_static/switchers.js"></script>
    
       …  (More than 200 such terrifying strings)
    > exit