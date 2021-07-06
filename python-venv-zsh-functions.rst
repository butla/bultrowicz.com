Some shell functions for working with Python virtualenvs
========================================================

.. post:: 2021-03-31
   :author: Michal Bultrowicz
   :tags: Python, Linux, CLI, ZSH

Finally doing some scripting today.
I noticed that there are some python-virtualenv-related commands I run often (in my tmux-based "IDE"),
so I automated them away to shave off some keystrokes.

Small incremental improvements compound over time, after all.

.. code-block:: zsh

    # Gets the name of the current directory.
    # I couldn't find a satisfactorily readable method for doing that with just the shell.
    function current_directory()
    {
        echo $(python3 -c "from pathlib import Path; print(Path('.').absolute().name)")
    }

    # create a virtualenv for the current directory, which should be a python project
    function mkvirt()
    {
        # uses mkvirtualenv from https://pypi.org/project/virtualenvwrapper/
        mkvirtualenv $(current_directory)
    }

    # Enters a virtualenv for the current project.
    # Assumes that the virtualenv is created by virtualenvwrapper
    # and is called the same as the current directory/project.
    # EDIT from 2021-07-06: changing the function name from venventer to workonc.
    # That's easier to remember, because I already go for "workon" to enter a virtualenv.
    function workonc()
    {
        workon $(current_directory)
    }


You can follow `this repo <https://github.com/butla/configs_and_scripts>`_
to get updates about small automations I make for myself.

I won't dedicate the time to document all the bits like above on this blog,
but I'll try to keep my commit messages and code understandable.

PS. spring is in the air, it's nice to enjoy the sun :)
