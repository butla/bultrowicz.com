Universal app reload with entr
==============================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

# TODO short first paragraph for the summary

If you work with web frameworks you might be used to having some sort of auto reload running,
that restarts your app when you change a file, so you can try out the changes immediately.
Flask has TODO, Django has,
Gunicorn (which is not a web framework but a WSGI server) has ``--reload`` flag.

What if you wanted that feature for everything that you're writing?
And without any coding?
Then you can use `entr`_. It's a nice little UNIXy tool.
It really just does one thing - running stuff when files change - and does it well.
And it has a nice, usable interface.
You just pass it the names of the files it needs to watch, and give it the command to run.

# TODO
E.g. to watch a single file

.. code-block:: bash

    ls blabla | entr

TODO with ls, with find, with fd

I use this when I'm prototyping some script or a tool. Using tmux, coding in one pane,
seeing the output in another one.

# TODO
Entr is C, but on the Python side you have watchdog (TODO link),
so you can integrate reacting to file changes to your project.

# TODO
A command that I found myself putting in Makefiles of small scripts I'm playing with is

.. code-block:: make

    run:
        ls test.py | entr -rc python3.8 test.py

.. _entr: https://github.com/clibs/entr
