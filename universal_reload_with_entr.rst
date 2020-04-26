Universal app reload with entr
==============================

.. post:: 2020-02-18
   :author: Michal Bultrowicz
   :tags: Python, Linux, CLI

A useful feature many web frameworks have is auto-reload.
Your app is running in the background, you change the code,
and the app is restarted with those changes, so you can try them out immediately.
What if you wanted that behavior for everything that you're writing?
And without any coding to implement it over and over in every little project?

Then you can use `entr`_. It's a nice little UNIXy [#1]_ tool.
It really just does one thing - running commands when files change.
And it has a simple, usable interface.
You just pass it the names of the files it needs to watch, and give it the command to run.

When I'm developing a script nowadays I usually run

.. code-block:: bash

    ls script.py | entr -c python3 script.py

in a `tmux`_ pane next to my editor, so I immediately see what it produces after every change.
Printing or logging in the script helps me to see where I'm going, of course :)

Anatomy of the command
----------------------

``entr`` needs to get the names of the files to watch on its input stream.
That's what ``ls script.py`` does. ``echo script.py`` would do the same thing.

Everything after ``entr`` and its options like ``-c``
(check other options in the manual: ``man entr``) is the command that it will run after any of the
watched files changes.

Reloading a web app
-------------------

Let's say you have a web app that's run with ``python app.py``
(or ``gunicorn``, ``uvicorn``, or whatever).
It probably consists of multiple files. You just have to find them and pass them to ``entr``.
With a nice modern alternative to ``find`` like `fd`_ it could look like this::

    fd .py$ | entr -rc python app.py

You want to use ``-r`` if your command is long-lived (like a web server).

Python's equivalent
-------------------

Entr is written C. But there is a Python project that does file-watching: `watchdog`_

You can use its ``watchmedo shell-command`` script pretty much from like ``entr``, but you can
also, of course, use ``watchdog`` to give your Python code the ability to react to file changes.

A command that I found myself putting in Makefiles of small scripts I'm playing with is

Parting words
-------------

``entr`` really is a tool I'm finding myself using more and more.
It's not much having to hit a couple of keys to rebuild or rerun something, but it's still so nice
when it *just* happens.

Hell, I even used ``entr`` to keep rebuilding this post :)
(sadly still had to press F5 on the browser, but I'm sure this can be automated as well)

.. rubric:: Footnotes

.. [#] "Do one thing and do it well"

.. _entr: https://github.com/clibs/entr
.. _tmux: https://github.com/tmux/tmux/wiki
.. _watchdog: https://github.com/gorakhargosh/watchdog
.. _fd: https://github.com/sharkdp/fd
