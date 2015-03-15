The original version of Adventure was developed by William Crowther.
Many others contributed improvements over time.  Rick Adam's web site
has a fascinating [A  history of 'adventure'](http://www.rickadams.org/adventure/a_history.html) page that is worth a click.

This version is a port of the C version of Adventure 5 to Python and
the Google App Engine.  The C code includes an interpreter for a
custom language in which the game is coded.  I wrote a "compiler" that
translates the custom language into Python.  Another option would have
been to port the interpreter to Python.

The interface is a simple teletype emulator, written in JavaScript,
that tries to provide the experience of typing at a slow terminal.

http://colossal-cave.appspot.com