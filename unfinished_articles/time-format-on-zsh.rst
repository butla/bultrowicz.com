Using formatted `time` for quick program measurements
=====================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Linux, CLI

Wanted to see how much resources will a program take without some fancy tools,
just initial quick rough measurements without nice graphs
or going into the stages or patterns in program's execution.

I noticed with ``man time`` that ``time`` has a format option.
But that wasn't working. It turned out the help is for the time command, not the shell built-in.

https://stackoverflow.com/questions/15261588/time-format-on-zsh

The package is called ``time`` both on Ubuntu and Manjaro.
After installing it you will be able to run ``/usr/bin/time -f "<format>" <command>``


Side note about builtin help
----------------------------

Builtins should display help and usage if asked.
Maybe the benefit of learnability and discoverability is worth not being able to easily time programs called
``-h`` and ``--help``.

Or you can pair CLI utilities with help ones like ``<program's or builtin's command>-help``,
e.g. ``time-help``.
I wonder how easy or complicated it would be to contribute that and get it to my main distro (Manjaro).
