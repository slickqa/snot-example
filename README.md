Slick - Nose - Snot example project
===================================

This is an example project using nose (python testing tool) to run tests
and submit the results to slick.  This should be a fairly thorough example
that allows you to base your own projects off of a similar hierarchy.

Setup
-----

To setup you will need virtualenv installed on your system.  You can follow
the instructions from [here](http://www.virtualenv.org/en/latest/virtualenv.html#installation).

Then create a virtual environment with all the tools installed:

    virtualenv vpython
    vpython/bin/pip install -r requirements.txt


Running the Example Tests
-------------------------

First you want to adjust your configuration for where slick is installed on your system.
You can adjust this in the `config.ini`.  Then to run do:

    vpython/bin/nosetests -c config.ini testlauncher.grouping.suitea

to run the tests.  Have fun!

Code Structure
--------------

There are 3 levels of packages in the code to help you see how you can group your
many test suites, and setup for those suites.  In this example I use functions
for tests (which is allowed using nose).  However if you want to use the unittest
module from python, that's ok.  Just realize that if you use unittest module, your
tests will not run in the order you define them (they are sorted by name).
